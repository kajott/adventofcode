#!/usr/bin/env python3
import subprocess
import argparse
import os
import re

SourcePos = (500, 0)
ExpectedGrainCount = 25000

class Colors:
    Empty    = (  0,   0,   0)  # must be zero
    Rock     = (160, 160, 160)
    Falling  = (240, 224,  64)
    Resting0 = (160, 128,  48)
    Resting1 = ( 64,  48,   8)

    @classmethod
    def make_resting(self, grains):
        t = 1.0 - min(1, max(0, grains / ExpectedGrainCount))
        t *= t
        t *= t
        return tuple(int(a * t + b * (1.0 - t)) for a,b in zip(self.Resting0, self.Resting1))

class LandOfSand:
    def __init__(self, x0,y0, x1,y1, rate=3):
        self.x0, self.y0 = x0, y0
        self.width  = x1 - x0 + 1
        self.height = y1 - y0 + 1
        self.bmp = bytearray(self.width * self.height * 3)
        self.rate = rate
        self.timeout = rate
        self.resting = 0
        self.falling = []

    def isempty(self, x,y):
        x -= self.x0
        y -= self.y0
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return False
        offset = 3 * (x + self.width * y)
        return not(self.bmp[offset] or self.bmp[offset + 1] or self.bmp[offset + 2])

    def put(self, x,y, color):
        x -= self.x0
        y -= self.y0
        if (x < 0) or (y < 0) or (x >= self.width) or (y >= self.height):
            return
        offset = 3 * (x + self.width * y)
        self.bmp[offset]     = color[0]
        self.bmp[offset + 1] = color[1]
        self.bmp[offset + 2] = color[2]

    def tofile(self, f):
        f.write(self.bmp)

    def save(self, filename):
        with open(filename, "wb") as f:
            f.write(f"P6\n{self.width} {self.height}\n255\n".encode())
            self.tofile(f)

    def step(self, n=1):
        for _ in range(n):
            # iterate over falling grains of sand
            grain_index = 0
            while grain_index < len(self.falling):
                # get position, evaluate where the grain moves
                x, y = self.falling[grain_index]
                keeps_falling = False
                ny = y + 1
                for nx in (x, x-1, x+1):
                    if self.isempty(nx, ny):
                        keeps_falling = True
                        break
                # update bitmap and falling grain state
                if keeps_falling:
                    self.put(x, y, Colors.Empty)
                    x, y = nx, ny
                    self.put(x, y, Colors.Falling)
                    self.falling[grain_index] = (x, y)
                    grain_index += 1
                else:
                    self.resting += 1
                    self.put(x, y, Colors.make_resting(self.resting))
                    del self.falling[grain_index]

            # produce new grain of sand at source
            self.timeout -= 1
            if self.timeout <= 0:
                self.timeout = self.rate
                if self.isempty(*SourcePos):
                    self.falling.append(SourcePos)
                    self.put(*SourcePos, Colors.Falling)
                else:
                    return False  # final state reached
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", metavar="FILE", default="input.txt",
                        help="input file name")
    parser.add_argument("-o", "--output", metavar="VIDEO.mp4",
                        help="save result into video file [default: show on screen]")
    parser.add_argument("-z", "--zoom", metavar="N", type=int, default=4,
                        help="scaling factor [integer; default: %(default)s]")
    parser.add_argument("-r", "--fps", metavar="FPS", type=int, default=30,
                        help="video speed in frames per second [default: %(default)s]")
    parser.add_argument("-d", "--drop", metavar="N", type=int, default=3,
                        help="sand grain drop rate in cycles per grain [default: %(default)s]")
    parser.add_argument("-s", "--dps", metavar="DPS", type=float, default=1,
                        help="simulation speed in drops per second [default: %(default)s]")
    parser.add_argument("-a", "--accel", metavar="N", type=float, default=0.5,
                        help="accelerate by N drops per second for every resting grain [default: %(default)s]")
    parser.add_argument("-q", "--crf", metavar="CRF", type=int, default=26,
                        help="x64 CRF quality factor [default: %(default)s]")
    args = parser.parse_args()
    gif = args.output and (os.path.splitext(args.output)[-1].strip(".").lower() == "gif")

    lines = []
    all_coords = [SourcePos]
    for line in open(args.input):
        coords = [tuple(map(int, c)) for c in re.findall(r'(\d+),(\d+)', line)]
        all_coords.extend(coords)
        lines.append(coords)
    bottom = max(y for x,y in all_coords) + 2
    left   = min(x - (bottom - y) for x,y in all_coords)
    right  = max(x + (bottom - y) for x,y in all_coords)
    lines.append([(left, bottom), (right, bottom)])

    sim = LandOfSand(left,0, right,bottom, rate=args.drop)
    for line in lines:
        x, y = line[0]
        sim.put(x, y, Colors.Rock)
        for tx, ty in line:
            while (x != tx) or (y != ty):
                x += (x < tx) - (x > tx)
                y += (y < ty) - (y > ty)
                sim.put(x, y, Colors.Rock)

    cpf = min(1, int(args.dps * args.drop / args.fps))
    while args.drop > 1:
        mod = cpf % args.drop
        if mod and (mod <= args.drop / 2): break
        cpf += 1
    def get_real_dps(cpf_override=None):
        return (cpf_override or cpf) * args.fps / args.drop
    real_dps = get_real_dps()
    print(f"image size: {sim.width}x{sim.height} cells -> {sim.width*args.zoom}x{sim.height*args.zoom} pixels")
    print(f"timing: {cpf} cycle(s)/frame x {args.fps} frames/sec = {cpf * args.fps} cycles/sec = {args.drop} cycle(s)/drop x {real_dps:.1f} drops/second")

    if args.output: cmdline = ["ffmpeg", "-hide_banner", "-y"]
    else:           cmdline = ["ffplay", "-hide_banner"]
    cmdline += ["-f", "rawvideo", "-video_size", f"{sim.width}x{sim.height}", "-pixel_format", "rgb24", "-framerate", str(args.fps)]
    if args.output: cmdline += ["-i"]
    cmdline += ["-", "-vf", f"scale={sim.width*args.zoom}x{sim.height*args.zoom}:flags=neighbor"]
    if not args.output:
        cmdline += ["-window_title", "AoC Sand Simulation"]
    elif gif:
        cmdline[-1] += ",split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse=dither=bayer"
        cmdline += ["-f", "gif", args.output]
    else:
        cmdline[-1] += ",format=yuv420p"
        cmdline += ["-c:v", "libx264", "-profile:v", "main", "-preset:v", "veryslow", "-tune:v", "animation", "-crf:v", str(args.crf), args.output]
    print(os.getenv("PS4", "+ ") + ' '.join((f'"{a}"' if (' ' in a) else a) for a in cmdline))

    out = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
    try:
        for _ in range((args.fps // 2) if args.output else 1):
            sim.tofile(out.stdin)  # generate 1/2 second of initial state (or 1 frame if just viewing)
        while sim.step(cpf):
            sim.tofile(out.stdin)
            expect_dps = args.dps + args.accel * sim.resting
            speed_changed = False
            while expect_dps >= get_real_dps(cpf + args.drop):
                cpf += args.drop
                speed_changed = True
            if speed_changed:
                real_dps = get_real_dps()
                print(f"timing changed: {cpf} cycle(s)/frame -> {real_dps:.1f} drops/second")
        for _ in range(args.fps * 2):
            sim.tofile(out.stdin)  # generate 2 second of final state
    except (EnvironmentError, KeyboardInterrupt):
        pass
    try:
        out.stdin.close()
    except EnvironmentError:
        pass
    try:
        out.wait()
    except EnvironmentError:
        pass
    print(f"simulation ended at {sim.resting} resting grains")
