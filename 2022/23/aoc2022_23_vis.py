#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "../../lib"))
import visutil

class Map:
    def __init__(self, infile):
        self.grid = set()
        self.elves = 0
        self.rounds = 0
        for y, r in enumerate(open(infile)):
            for x, c in enumerate(r):
                if c == '#':
                    self.grid.add((x,y))
                    self.elves += 1
        self.dirs = [
            ((0,-1), (-1,-1), (+1,-1)),  # N
            ((0,+1), (-1,+1), (+1,+1)),  # S
            ((-1,0), (-1,-1), (-1,+1)),  # W
            ((+1,0), (+1,-1), (+1,+1)),  # E
        ]
        self.bboxfile = os.path.join(os.path.dirname(sys.argv[0]), ".vis_bbox")
        self.vis = visutil.Visualizer(default_speed=100, default_zoom=4, novis_arg=True)
        if self.vis:
            self.bmp = visutil.Bitmap(*self.get_bbox(), border=1)
            print("bitmap size:", self.bmp.size)
            self.vis.start(source=self.bmp)
            self.update_bitmap()
            self.vis.write(initial=True)

    def get_bbox(self):
        try:
            with open(self.bboxfile) as f:
                return eval(f.read())
        except EnvironmentError:
            return visutil.get_extent(self.grid)

    def save_bbox(self):
        try:
            with open(self.bboxfile, 'w') as f:
                f.write(repr(visutil.get_extent(self.grid)))
        except EnvironmentError:
            pass

    def dump(self, title=None, with_map=True):
        if title:
            print(title + ":")
        x0 = min(x for x,y in self.grid)
        y0 = min(y for x,y in self.grid)
        x1 = max(x for x,y in self.grid) + 1
        y1 = max(y for x,y in self.grid) + 1
        if with_map:
            for y in range(y0, y1):
                print(''.join(".#"[(x,y) in self.grid] for x in range(x0, x1)))
        print((y1-y0) * (x1-x0) - self.elves)
        if with_map:
            print()

    def run_single(self):
        self.old2new = {}
        self.occupied = {}
        for x,y in self.grid:
            valid_dirs = []
            for dirspec in self.dirs:
                if not any(((x+dx, y+dy) in self.grid) for dx,dy in dirspec):
                    valid_dirs.append((x+dirspec[0][0], y+dirspec[0][1]))
            if not(valid_dirs) or (len(valid_dirs) == 4):
                tx,ty = x,y
            else:
                tx,ty = valid_dirs[0]
            try:
                occpos = self.occupied[(tx,ty)]
                self.old2new[occpos] = occpos
                self.old2new[(x,y)] = (x,y)
            except KeyError:
                self.old2new[(x,y)] = (tx,ty)
                self.occupied[(tx,ty)] = (x,y)
        oldgrid = self.grid
        self.grid = {*self.old2new.values()}
        assert len(self.grid) == self.elves
        self.dirs.append(self.dirs.pop(0))
        self.rounds += 1
        if self.vis:
            self.update_bitmap(oldgrid)
            self.vis.write()
        return not(self.grid == oldgrid)

    def run_to(self, end=1, verbosity=0):
        if verbosity >= 1:
            self.dump("initial")
        cont = True
        while self.rounds < end:
            cont = self.run_single()
            if not cont: break
            if verbosity >= 2:
                self.dump(f"after {self.rounds} rounds")
        if (verbosity == 1) or not(cont):
            self.dump(f"final state after {self.rounds} rounds")

    def update_bitmap(self, oldgrid=None):
        if oldgrid is None:
            oldgrid = self.grid
        self.bmp.clear()
        for x, y in (self.grid - oldgrid):
            self.bmp.put(x, y, 255, 255, 128)
        for x, y in (self.grid & oldgrid):
            self.bmp.put(x, y, 192, 192, 64)

    def close(self):
        if self.vis:
            try:
                self.vis.write(final=True)
            except (EnvironmentError, KeyboardInterrupt):
                pass
            self.vis.stop()

if __name__ == "__main__":
    m = Map("input.txt")
    try:
        while m.run_single():
            if m.rounds == 10:
                m.dump(with_map=False)
            # if not(m.rounds % 100): print(m.rounds, "...")
        print(m.rounds)
        m.save_bbox()
    except (EnvironmentError, KeyboardInterrupt):
        pass
    m.close()
