#!/usr/bin/env python3
"""
Visualization toolkit based on simple low-res RGB bitmaps.
Can save images to PNM (.ppm), or videos to .mp4 or .gif using FFmpeg,
or generate a live view using FFplay.
"""
import subprocess
import argparse
import math
import os

################################################################################

class ColorInterpolator:
    "Linear interpolation between two sRGB colors."

    def __init__(self, rgb0, rgb1, t0=1.0, t1=None, power=1.0):
        """
        Initialize the generator.
          - rgb0: 3-tuple of 8-bit sRGB colors that represent the start time
          - rgb1: 3-tuple of 8-bit sRGB colors that represent the end   time
          - t0: start time (if t1 is omitted, the end time, and start is 0)
          - t1: end time
          - power: power to apply to the interpolation coefficient;
                   if negative, the power will be applied to *reversed* time
        """
        self.rgb0 = rgb0
        self.rgb1 = rgb1
        if t1 is None:
            t0, t1 = 0, t0
        self.t0, self.t1 = t0, t1
        self.dt = float(t1 - t0)
        self.power = power

    def __call__(self, t):
        "Generate a color for a specified time."
        if t <= self.t0: return self.rgb0
        if t >= self.t1: return self.rgb1
        t = (t - self.t0) / self.dt
        if self.power < 0: t = 1.0 - t
        t = math.pow(t, abs(self.power))
        if self.power < 0: t = 1.0 - t
        return tuple(max(0, min(255, int((1.0 - t) * c0 + t * c1 + 0.5))) for c0, c1 in zip(self.rgb0, self.rgb1))

################################################################################

class Bitmap:
    "A single still frame."

    def __init__(self, c1, c2=None, border=0, init=None, background=None, exterior=None):
        """
        Initialize an RGB bitmap using one of the following syntaxes:
          - Bitmap(other) => copy everything from other bitmap
          - Bitmap(seq) => auto-detect bounding box from sequence (or dict) of
                           2-tuples or complex numbers
          - Bitmap(width, height) => valid coordinates 0,0 ... width-1, height-1
          - Bitmap((width,height)) => as above
          - Bitmap((x0,y0), (x1,y1)) => valid coordinates x0,y0 ... x1,y1;
                                        width = x1 - x0 + 1; height = y1 - y0 + 1
          - Bitmap(x0+y0*1j, x1+y1*1j) => as above
        Other parameters:
          - border: number of extra background pixels to add around the edges
                    of the image
          - init: bytes, bytearray, list or anything that has a tobytes()
                  method, to be used to initialize bitmap with
          - background: 3-tuple of 8-bit sRGB values for background;
                        defaults to black (or init if specified)
          - exterior: 3-tuple of 8-bit sRGB values that shall be returned
                      for out-of-range get() requests; defaults to background
        """
        if isinstance(c1, Bitmap):
            self.x0, self.y0, self.x1, self.y1 = c1.x0, c1.y0, c1.x1, c1.y1
            self.width, self.height = c1.width, c1.height
            self.exterior = c1.exterior
        if c2 and isinstance(c1, int) and isinstance(c2, int):
            c1, c2 = (c1, c2), None
        if (c2 is None) and not(isinstance(c1, int) or (isinstance(c1, tuple) and (len(c1) == 2))):
            keys = set(c1)
            any_item = keys.pop()
            cplx = isinstance(any, complex)
            keys.add(any_item)
            if cplx:
                xx = {int(p.real) for p in keys}
                yy = {int(p.imag) for p in keys}
            else:
                xx = {x for x,y in keys}
                yy = {y for x,y in keys}
            c1 = (min(xx), min(yy))
            c2 = (max(xx), max(yy))
        if isinstance(c1, complex):
            c1 = (int(c1.real), int(c1.imag))
        if isinstance(c2, complex):
            c2 = (int(c2.real), int(c2.imag))
        if c2 is None:
            self.width, self.height = c1
            self.x0, self.y0 = border, border
            self.x1, self.y1 = self.width - 1 + border, self.height - 1 + border
        else:
            self.x0, self.y0 = c1
            self.x1, self.y1 = c2
            self.x0, self.x1 = min(self.x0, self.x1), max(self.x0, self.x1)
            self.y0, self.y1 = min(self.y0, self.y1), max(self.y0, self.y1)
            self.x0 -= border
            self.y0 -= border
            self.x1 += border
            self.y1 += border
        self.width  = self.x1 - self.x0 + 1
        self.height = self.y1 - self.y0 + 1
        if not background:
            background = (0, 0, 0)
        self.exterior = tuple(exterior or background)
        if init:
            if hasattr(init, 'tobytes'):
                init = init.tobytes()
            self.data = bytearray(init)
            assert len(self.data) == (self.width * self.height * 3), "invalid initialization data size"
        else:
            self.data = bytearray(bytes(background) * (self.width * self.height))

    @property
    def size(self):
        return (self.width, self.height)

    def get(self, x,y=None):
        """
        Get a pixel, either by separate coordinates, 2-tuple or complex number.
        """
        if isinstance(x, complex):
            x, y = int(x.real), int(x.imag)
        elif y is None:
            x, y = x
        x -= self.x0
        y -= self.y0
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return self.exterior
        offset = 3 * (x + self.width * y)
        return tuple(self.data[offset : offset+3])

    def put(self, *args):
        """
        Put a pixel. Arguments are the following:
          - first: coordinate; either separate x,y integers, or (x,y) tuple,
                               or complex number
          - second: color; either r,g,b 8-bit sRGB integers, or (r,g,b) tuple,
                           or single 8-bit sRGB integer for grayscale
        """
        if isinstance(args[0], int):
            x, y = args[:2]
            n = 2
        elif isinstance(args[0], complex):
            x, y = int(args[0].real), int(args[0].imag)
            n = 1
        else:
            x, y = args[0]
            n = 1
        x -= self.x0
        y -= self.y0
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return
        if isinstance(args[n], int):
            if len(args) >= n + 3:
                r, g, b = args[n : n+3]
            else:
                r = g = b = args[n]
        else:
            r, g, b = args[n]
        offset = 3 * (x + self.width * y)
        self.data[offset]   = r
        self.data[offset+1] = g
        self.data[offset+2] = b

    def tobytes(self):
        return bytes(self.data)

    def tofile(self, f):
        f.write(self.data)

    def save(self, filename):
        ext = os.path.splitext(filename)[-1].strip(".").lower()
        assert ext in ("ppm", "pnm"), "unsupported file format"
        with open(filename, "wb") as f:
            f.write(f"P6\n{self.width} {self.height}\n255\n".encode())
            self.tofile(f)

################################################################################

class Visualizer:
    """Class for managing video output.

    This adds a command-line interface to the program using the argparse
    module. If the -o option is specified and points to an .mp4 or .gif file,
    output will be written to a video or animated GIF file. If it's omitted,
    a live preview will be shown instead.
    """

    def __init__(self, default_zoom=1, default_speed=None, source=None, extra_args=None, input_arg=False, title="Visualization"):
        """
        Read command-line options.
          - default_zoom: default zoom factor
          - default_speed: if present, offer a -s/--speed option and set
                           frameskip appropriately
          - source: source bitmap (if already known)
          - extra_args: function that is called with the argparse.ArgumentParser
                        instance, to add additional arguments
          - input_arg: set to nonzero to include the -i/--input argument;
                       if set to a string, this will be the default argument
                       (result will be available as Visualizer.input)
          - title: window title
        """
        parser = argparse.ArgumentParser()
        parser = argparse.ArgumentParser()
        if input_arg:
            parser.add_argument("-i", "--input", metavar="FILE", default=(input_arg if isinstance(input_arg, str) else "input.txt"),
                                help="input file name")
        parser.add_argument("-o", "--output", metavar="VIDEO.mp4",
                            help="save result into video file [default: show on screen]")
        parser.add_argument("-z", "--zoom", metavar="N", type=int, default=default_zoom,
                            help="scaling factor [integer; default: %(default)s]")
        parser.add_argument("-r", "--fps", metavar="FPS", type=int, default=30,
                            help="video speed in frames per second [default: %(default)s]")
        if default_speed:
            parser.add_argument("-s", "--speed", metavar="TPS", type=float, default=default_speed,
                                help="simulation speed in ticks per second [default: %(default)s]")
        if extra_args:
            extra_args(parser)
        parser.add_argument("-q", "--crf", metavar="CRF", type=int, default=26,
                            help="x64 CRF quality factor [default: %(default)s]")
        self.args = parser.parse_args()
        self.gif = self.args.output and (os.path.splitext(self.args.output)[-1].strip(".").lower() == "gif")
        self.source = self.bmp = source
        self.fps = self.args.fps
        if default_speed:
            self.speed = self.args.speed
            self.frameskip = max(1, int(self.speed / self.fps + 0.5))
        else:
            self.frameskip = 1
        self.input = self.args.input if input_arg else None
        self.proc = None
        self.title = title

    def start(self, source=None, frameskip=0, verbose=False):
        """
        Start the visualization (or encoding).
          - source: set source bitmap (if not already done so in the constructor)
          - frameskip: override frameskip value that's been set in the constructor
          - verbose: set to True to show the FFmpeg/FFplay command line
        """
        if source:
            self.source = self.bmp = source
        w, h = getattr(self.source, 'width', 0), getattr(self.source, 'height', 0)
        if not(w) or not(h):
            w, h = getattr(self.source, 'size', (0,0))
        assert w and h, "can't determine output size"

        if self.args.output: cmdline = ["ffmpeg", "-hide_banner", "-y"]
        else:                cmdline = ["ffplay", "-hide_banner", "-loglevel", "error"]
        cmdline += ["-f", "rawvideo", "-video_size", f"{w}x{h}", "-pixel_format", "rgb24", "-framerate", str(self.args.fps)]
        if self.args.output: cmdline += ["-i"]
        cmdline += ["-", "-vf", f"scale={w*self.args.zoom}x{h*self.args.zoom}:flags=neighbor"]
        if not self.args.output:
            cmdline += ["-window_title", self.title]
        elif self.gif:
            cmdline[-1] += ",split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse=dither=bayer"
            cmdline += ["-f", "gif", self.args.output]
        else:
            cmdline[-1] += ",format=yuv420p"
            cmdline += ["-c:v", "libx264", "-profile:v", "main", "-preset:v", "veryslow", "-tune:v", "animation", "-crf:v", str(self.args.crf), self.args.output]
        if verbose:
            print(os.getenv("PS4", "+ ") + ' '.join((f'"{a}"' if (' ' in a) else a) for a in cmdline))
        self.proc = subprocess.Popen(cmdline, stdin=subprocess.PIPE)

        if frameskip:
            self.frameskip = frameskip
        self.skipcount = self.frameskip
        self.frames = 0
        self.ticks = 0

    def write(self, source=None, n=0, initial=False, final=False):
        """
        Send a frame to the display or encoder. start() must have been called
        before that.
          - source: source bitmap (if not already set earlier)
          - n: number of times to repeat the frame;
               0 = automatic (depends on frameskip), larger = explicit count
          - initial: if set to True, override n to 1 (on preview) or fps/2
                     (on export), to visualize initial state
          - final: if set to True, override n to fps*2, to visualize final state
        EnvironmentErrors or KeyboardInterrupts may occur; those should be
        intercepted by the host application and be treated as if the output
        finished normally, i.e. stop()/close() should *still* be called.
        """
        assert self.proc, "no output running"
        if initial: n = max(1, (self.fps // 2)) if self.args.output else 1
        if final:   n = self.fps * 2
        if not n:
            self.ticks += 1
            self.skipcount -= 1
            if self.skipcount > 0:
                return
            self.skipcount = self.frameskip
            n = 1
        if not source:
            source = self.source
        if hasattr(source, 'tofile'):
            for i in range(n):
                source.tofile(self.proc.stdin)
        else:
            frame = source.tobytes()
            for i in range(n):
                self.proc.stdin.write(frame)
        self.frames += n

    def stop(self):
        "Stop the display or encoder."
        if not self.proc: return
        try: self.proc.stdin.close()
        except EnvironmentError: pass
        try: self.proc.wait()
        except EnvironmentError: pass
        self.proc = None
    def close(self):
        "alias for stop()"
        self.stop()
