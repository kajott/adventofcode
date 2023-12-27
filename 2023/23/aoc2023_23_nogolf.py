#!/usr/bin/env python3
import time

Neighbors = (1, -1, 1j, -1j)

class Maze:
    def __init__(self, infile="input.txt"):
        self.free = {1-1j: 0}
        self.slopes = {}
        for y,l in enumerate(open(infile)):
            for x,c in enumerate(l.strip()):
                p = y*1j+x
                self.free[p] = (c != '#')
                if c=='<': self.slopes[p] = -1
                if c=='>': self.slopes[p] = 1
                if c=='^': self.slopes[p] = -1j
                if c=='v': self.slopes[p] = 1j
        self.goal = y*1j+x - 1
        self.free[self.goal + 1j] = 0

    def part1_dfs(self, pos=1, visited=None):
        if not visited: visited = set()
        while pos != self.goal:
            visited.add(pos)
            try:  # at slope?
                pos += self.slopes[pos]
                if pos in visited: return 0
            except KeyError:  # no slope
                dirs = {d for d in Neighbors if self.free[pos + d] and not((pos + d) in visited)}
                if not dirs: return 0
                if len(dirs) == 1:  # go straight on
                    pos += dirs.pop()
                else:  # junction
                    return max(self.part1_dfs(pos + d, set(visited)) for d in dirs)
        # goal reached
        return len(visited)

    def find_junctions(self):
        self.junctions = {1, self.goal} \
                       | {pos for pos in self.free if self.free[pos] \
                          and sum(self.free[pos + d] for d in Neighbors) > 2}
        self.dist = {j:[] for j in self.junctions}
        for j in self.junctions:
            t = 0
            queue = {j}
            visited = set()
            while queue:
                t += 1
                visited |= queue
                queue = {pos + d for pos in queue for d in Neighbors if self.free[pos + d]} - visited
                for pos in (queue & self.junctions):
                    self.dist[j].insert(0, (pos, t))
                queue -= self.junctions
        self.best_path = []
        self.best_dist = 0
        return len(self.junctions)

    def write_graph(self, outfile="graph.neato"):
        common_style = 'fontname="Segoe UI,FreeSans,Helvetica,Arial,sans-serif"'
        def node_id(pos):
            return f"y{pos.imag:03.0f}x{pos.real:03.0f}"
        path_edges = set()
        for a,b in zip(self.best_path, self.best_path[1:]):
            path_edges |= {(a,b), (b,a)}
        with open(outfile, 'w') as f:
            f.write('graph aoc2023_23 {\n')
            f.write(f'node [{common_style}, shape=box, width=0, height=0, style=filled, fillcolor=lightgray]\n')
            f.write(f'edge [{common_style}, color=darkgray]\n')
            for j in sorted(self.junctions, key=node_id):
                f.write(f'{node_id(j)} [label="{j.imag+1:.0f}:{j.real+1:.0f}", pos="{int(j.real)},{-int(j.imag)}"];\n')
            seen_edges = set()
            for a in self.dist:
                for b,d in self.dist[a]:
                    if (a,b) in seen_edges: continue
                    style = ', color=red, penwidth=5' if ((a,b) in path_edges) else ''
                    f.write(f'{node_id(a)} -- {node_id(b)} [label="{d}"{style}]\n')
                    seen_edges |= {(a,b), (b,a)}
            f.write('}\n')

    def search_path(self, dist=0, path=[1]):
        if not dist:
            self.total_paths = 0
        if path[-1] == self.goal:
            self.total_paths += 1
            if dist > self.best_dist:
                self.best_dist = dist
                self.best_path = path
                print("- new best path after", self.total_paths, "checked paths: length", self.best_dist)
        else:
            visited = set(path)
            for j,d in self.dist[path[-1]]:
                if not(j in visited):
                    self.search_path(dist + d, path + [j])


if __name__ == "__main__":
    m = Maze()
    print("part 1 result:", m.part1_dfs())
    print("number of junctions:", m.find_junctions())
    m.write_graph()
    print("searching longest path ...")
    t0 = time.time()
    try:
        m.search_path()
        print("search finished after", m.total_paths, "paths in", int(time.time() - t0), "seconds")
        print("part 2 result:", m.best_dist)
    except KeyboardInterrupt:
        print("<path search aborted after", m.total_paths, "paths>")
    m.write_graph()
