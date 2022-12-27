#!/usr/bin/env python3
import subprocess
import argparse
import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "../../lib"))
import visutil

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
        self.bmp = visutil.Bitmap((x0,y0), (x1,y1))
        self.rate = rate
        self.timeout = rate
        self.resting = 0
        self.falling = []

    def isempty(self, x,y):
        return not any(self.bmp.get(x,y))

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
                    self.bmp.put(x, y, Colors.Empty)
                    x, y = nx, ny
                    self.bmp.put(x, y, Colors.Falling)
                    self.falling[grain_index] = (x, y)
                    grain_index += 1
                else:
                    self.resting += 1
                    self.bmp.put(x, y, Colors.make_resting(self.resting))
                    del self.falling[grain_index]

            # produce new grain of sand at source
            self.timeout -= 1
            if self.timeout <= 0:
                self.timeout = self.rate
                if self.isempty(*SourcePos):
                    self.falling.append(SourcePos)
                    self.bmp.put(*SourcePos, Colors.Falling)
                else:
                    return False  # final state reached
        return True


def extra_args(parser):
    parser.add_argument("-d", "--drop", metavar="N", type=int, default=3,
                        help="sand grain drop rate in cycles per grain [default: %(default)s]")
    parser.add_argument("-s", "--dps", metavar="DPS", type=float, default=1,
                        help="simulation speed in drops per second [default: %(default)s]")
    parser.add_argument("-a", "--accel", metavar="N", type=float, default=0.5,
                        help="accelerate by N drops per second for every resting grain [default: %(default)s]")


if __name__ == "__main__":
    vis = visutil.Visualizer(input_arg=True, extra_args=extra_args)
    args = vis.args

    lines = []
    all_coords = [SourcePos]
    for line in open(vis.input):
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
        sim.bmp.put(x, y, Colors.Rock)
        for tx, ty in line:
            while (x != tx) or (y != ty):
                x += (x < tx) - (x > tx)
                y += (y < ty) - (y > ty)
                sim.bmp.put(x, y, Colors.Rock)

    cpf = min(1, int(args.dps * args.drop / vis.fps))
    while args.drop > 1:
        mod = cpf % args.drop
        if mod and (mod <= args.drop / 2): break
        cpf += 1
    def get_real_dps(cpf_override=None):
        return (cpf_override or cpf) * vis.fps / args.drop
    real_dps = get_real_dps()
    print(f"image size: {sim.bmp.width}x{sim.bmp.height} cells -> {sim.bmp.width*args.zoom}x{sim.bmp.height*args.zoom} pixels")
    print(f"timing: {cpf} cycle(s)/frame x {vis.fps} frames/sec = {cpf * vis.fps} cycles/sec = {args.drop} cycle(s)/drop x {real_dps:.1f} drops/second")

    vis.start(sim.bmp)
    try:
        # generate 1/2 second of initial state (or 1 frame if just viewing)
        vis.write(n=((vis.fps // 2) if args.output else 1))
        while sim.step(cpf):
            vis.write()
            expect_dps = args.dps + args.accel * sim.resting
            speed_changed = False
            while expect_dps >= get_real_dps(cpf + args.drop):
                cpf += args.drop
                speed_changed = True
            if speed_changed:
                real_dps = get_real_dps()
                print(f"timing changed: {cpf} cycle(s)/frame -> {real_dps:.1f} drops/second")
        vis.write(n=vis.fps*2)  # generate 2 second of final state
    except (EnvironmentError, KeyboardInterrupt):
        pass
    vis.stop()
    print(f"simulation ended at {sim.resting} resting grains")
