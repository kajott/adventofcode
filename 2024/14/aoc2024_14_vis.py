#!/usr/bin/env python3
import os
import re
import sys
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "../../lib"))
import visutil

width, height = 101, 103

if __name__ == "__main__":
    def extra_args(parser):
        parser.add_argument("-t", "--start-time", type=int, default=0,
                            help="simulation start timestep")
    vis = visutil.Visualizer(
            default_zoom=8,
            extra_args=extra_args, input_arg="input.txt",
            title="AoC 2024 day 14")

    dots = [tuple(map(int, re.findall(r'-?\d+',line))) for line in open(vis.input)]
    t = vis.args.start_time

    bmp = visutil.Bitmap(width, height)
    vis.start(bmp)
    try:
        while True:
            bmp.clear()
            for px, py, dx, dy in dots:
                bmp.put((px + dx * t) % width, (py + dy * t) % height, 255)
            sys.stdout.write(f"\rt={t} ")
            sys.stdout.flush()
            for _ in range(vis.fps):
                vis.write()
            t += 1
    except (EnvironmentError, KeyboardInterrupt):
        print
    vis.stop()
