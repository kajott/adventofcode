#!/usr/bin/env python3
import argparse
import collections
import math
import sys
import time

Verbose = False

###############################################################################

class Problem:
    def __init__(self, line: str):
        self.buttons = [tuple(map(int,part[1:-1].split(','))) for part in line.split()[1:]]
        self.target = self.buttons.pop()
        if Verbose > 0:
            print("[Problem:Input]", str(self.target).replace(" ", ""), "from", str(self.buttons).replace(" ", "").replace("),(", "), ("))
        if Verbose > 0:
            self.dump_matrix()

    def dump_matrix(self, prefix="[Problem:Matrix]", matrix=None):
        for row, y in zip(matrix or self.get_matrix(), self.target):
            print(prefix, " ".join(map(str,row)), "|", y)

    def get_matrix(self, target=None, buttons=None):
        return [[int(r in btn) for btn in (buttons or self.buttons)] for r, y in enumerate(target or self.target)]

class AllSolvers:
    aliases = ["all"]
    solvers = []
    alias_map = {}
    @classmethod
    def add(cls, solver):
        cls.solvers.append(solver)
        for a in solver.aliases:
            cls.alias_map[a] = solver
AllSolvers.add(AllSolvers)

###############################################################################

class Stats:
    aliases = ["st", "stat", "stats"]
    perf = None

    def __init__(self):
        self.dims = collections.Counter()
        self.targets = collections.Counter()

    def __call__(self, prob: Problem):
        self.dims[(len(prob.target), len(prob.buttons))] += 1
        self.targets.update(prob.target)
        return None, None

    def __del__(self):
        print("[Stats] target dimension range:", min(t for t,b in self.dims),
                                           "..", max(t for t,b in self.dims))
        print("[Stats] button count range:", min(b for t,b in self.dims),
                                       "..", max(b for t,b in self.dims))
        print("[Stats]", sum((t == b) * f for (t,b),f in self.dims.items()), "square",
                         sum((t >  b) * f for (t,b),f in self.dims.items()), "overconstrained",
                         sum((t <  b) * f for (t,b),f in self.dims.items()), "underconstrained")
        print("[Stats] target value range:", min(self.targets), "..", max(self.targets),
                                  "average", sum(v*f for v,f in self.targets.items()) / self.targets.total())

AllSolvers.add(Stats)

###############################################################################

class Z3:
    aliases = ["z3"]
    perf = 0

    def __call__(self, prob: Problem):
        import z3
        vars = [z3.Int(f"v{i}") for i in range(len(prob.buttons))]
        opt = z3.Optimize()
        opt.add([z3.Sum([vars[i] for i, btn in enumerate(prob.buttons) if (r in btn)]) == y for r, y in enumerate(prob.target)])
        opt.add([var >= 0 for var in vars])
        opt.minimize(z3.Sum(vars))
        opt.check()
        model = opt.model()
        vector = [model[var].as_long() for var in vars]
        return None, vector

AllSolvers.add(Z3)

###############################################################################

class LinProg:
    aliases = ["linprog", "lp"]
    perf = 0

    def __call__(self, prob: Problem):
        import scipy.optimize
        res = scipy.optimize.linprog(
            [1] * len(prob.buttons),
            A_eq = prob.get_matrix(),
            b_eq = prob.target,
            integrality = 1)
        if Verbose > 1:
            print("[LinProg:Result]", res)
        assert res.success
        return round(res.fun), map(round, res.x)

AllSolvers.add(LinProg)

###############################################################################

class MILP:
    aliases = ["milp"]
    perf = 0

    def __call__(self, prob: Problem):
        import scipy.optimize
        ones  = [1] * len(prob.buttons)
        res = scipy.optimize.milp(
            c = ones,
            constraints = scipy.optimize.LinearConstraint(prob.get_matrix(), lb=prob.target, ub=prob.target),
            integrality = ones)
        if Verbose > 1:
            print("[MILP:Result]", str(res).replace("\n", "\n              "))
        assert res.success
        return round(res.fun), map(round, res.x)

AllSolvers.add(MILP)

###############################################################################

class IntGauss:
    aliases = ["intgauss", "int", "gauss"]
    perf = 0

    def __call__(self, prob: Problem):
        self.matrix = prob.get_matrix()
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        rank = min(rows, cols)
        self.matrix.append([min(y for row, y in zip(self.matrix, prob.target) if row[j]) for j in range(cols)])
        for row, y in zip(self.matrix, prob.target):
            row.append(y)
        self.dump_matrix(2, "Initial")

        # generate upper diagonal matrix
        for i in range(rank):
            prefix = f"UD{i}:"
            # find pivot row
            while True:  # this will iterate at most twice
                nonzero_rows = [j for j in range(i, rows) if abs(self.matrix[j][i])]
                if nonzero_rows: break
                # alas, we need to swap columns
                nonzero_cols = [j for j in range(i+1, cols) if any(abs(self.matrix[k][j]) for k in range(i, rows))]
                if not nonzero_cols:
                    self.dprint(2, prefix + "PivotCol", "NONE - aborting")
                    break
                pivot = nonzero_cols[0]
                self.dprint(2, prefix + "PivotCol", pivot)
                self.matrix = [row[:i] + row[pivot:pivot+1] + row[i:pivot] + row[pivot+1:] for row in self.matrix]
                self.dump_matrix(3, prefix + "SwapCol")
            if not nonzero_rows:
                break  # no zeros found at all -> stop here
            pivot = min(nonzero_rows, key=lambda j: abs(self.matrix[j][i]))
            self.dprint(2, prefix + "PivotRow", pivot)
            # swap pivot
            if pivot != i:
                self.matrix[pivot], self.matrix[i] = self.matrix[i], self.matrix[pivot]
                self.dump_matrix(3, prefix + "SwapRow")
            # scale other rows
            for j in range(i+1, rows):
                self.cancel_row(i, j, prefix + f"ScaleRow:{j}")
            self.dump_matrix(3, prefix + "ScaleRow")

        # truncate empty rows and ensure that the target column is always positive
        while not any(self.matrix[-2]):
            del self.matrix[-2]
            rows -= 1
        unknowns = cols - rows
        self.dprint(1, "Unknowns", unknowns)
        self.dump_matrix(2, "UDFinal")

        # create full diagonal matrix
        for i in range(rows-1, 0, -1):
            prefix = f"FD{i}:"
            for j in range(i):
                self.cancel_row(i, j, prefix + f"ScaleRow:{j}")
            self.dump_matrix(3, prefix + "ScaleRow")
        self.dump_matrix(2, "FDFinal")

        # ensure constant positive elements on the main diagonal
        self.norm = 1
        for i in range(rows):
            self.norm = math.lcm(self.norm, abs(self.matrix[i][i]))
        self.dprint(2, "Norm", self.norm)
        for i in range(rows):
            scale = self.norm // self.matrix[i][i]
            self.matrix[i] = [x * scale for x in self.matrix[i]]
        self.dump_matrix(1, "Final")

        # transpose the matrix to get the residual coefficients
        self.maxcount = self.matrix[-1][rows:]
        assert len(self.maxcount) == unknowns
        self.dprint(3, "MaxCount", self.maxcount)
        self.coeffs = [*zip(*self.matrix[:-1])][rows:]
        residual = self.coeffs.pop()
        assert len(self.coeffs) == unknowns
        if Verbose >= 2:
            for row, mc in zip(self.coeffs, self.maxcount):
                print("[IntGauss:Coeffs]  ", " ".join(f"{x:4d}" for x in row), f"| max {mc:3d}")
            print("[IntGauss:Residual]", " ".join(f"{x:4d}" for x in residual))

        # solve!
        sys.stdout.flush()
        sum, *res = self.search(unknowns - 1, residual)
        return sum, res

    def search(self, index: int, residual: list, fixed: list = []):
        if index < 0:
            if any((r % self.norm) or (r < 0) for r in residual):
                return [1E9]
            res = [r // self.norm for r in residual] + fixed
            return [sum(res)] + res
        return min(self.search(index - 1,
            [r - n * c for r, c in zip(residual, self.coeffs[index])],
            [n] + fixed)
        for n in range(self.maxcount[index] + 1))

    def cancel_row(self, pivot: int, target: int, prefix: str = "CancelRow"):
        a = self.matrix[pivot][pivot]
        b = self.matrix[target][pivot]
        if not b: return
        n = math.lcm(a, b)
        fa = n // a
        fb = n // b
        self.dprint(4, prefix, f"{pivot=} {target=} {a=} {b=} {n=} {fa=} {fb=}")
        self.matrix[target] = [xb * fb - xa * fa for xa, xb in zip(self.matrix[pivot], self.matrix[target])]

    def dprint(self, level: int, tag="Debug", *values):
        if Verbose >= level:
            print(f"[IntGauss:{tag}]", *values)

    def dump_matrix(self, level: int, tag="Matrix"):
        if Verbose >= level:
            cols = len(self.matrix[0]) - 1
            for row in self.matrix:
                print(f"[IntGauss:{tag}]", " ".join(f"{x:3d}" for x in row[:cols]), f"| {row[-1]:4d}" if len(row) > cols else "")
            print()

AllSolvers.add(IntGauss)

###############################################################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("solvers", metavar="SOLVER", nargs='*',
                        help="solver(s) to use; options: " + ", ".join("/".join(sorted(s.aliases)) for s in AllSolvers.solvers))
    parser.add_argument("-v", "--verbose", action='count', default=0,
                        help="trace everything")
    parser.add_argument("-i", "--input", metavar="FILE", default="input.txt",
                        help="input file (default: %(default)s)")
    parser.add_argument("-n", "--count", metavar="N", type=int, default=1E10,
                        help="maximum number of problems to solve (default: unlimited)")
    parser.add_argument("-s", "--start", metavar="N", type=int, default=1,
                        help="starting problem line number (default: 1)")
    parser.add_argument("-p", "--problem", metavar="N", type=int,
                        help="run single problem (equivalent to -s N -n 1)")
    args = parser.parse_args()

    try:
        solvers = [AllSolvers.alias_map[s.lower()] for s in args.solvers]
    except KeyError as e:
        parser.error(str(e))

    Verbose = args.verbose
    if AllSolvers in solvers:
        solvers = AllSolvers.solvers[1:]
    solvers = [s() for s in solvers] or [IntGauss()]
    if Verbose > 0:
        print("[Config:Solvers]", ", ".join(s.__class__.__name__ for s in solvers))
    if args.problem:
        start = args.problem
        end = start + 1
    else:
        start = args.start
        end = start + args.count

    grand_total = 0
    n = 0
    for line in open(args.input):
        n += 1
        if not(start <= n < end):
            continue
        if Verbose > 0:
            print()
            print("[Input:Line]", n)
        if Verbose >= 2:
            print("[Input:Raw]", line.strip())

        prob = Problem(line)
        res = set()
        for s in solvers:

            t = time.time()
            count, vector = s(prob)
            t = time.time() - t
            if not(s.__class__.perf is None):
                s.__class__.perf += t

            if vector:
                vector = tuple(vector)
            if not(count) and vector:
                count = sum(vector)
            if count:
                if Verbose > 0:
                    print(f"[{s.__class__.__name__}:Result]", count, vector or "")
                res.add(count)
        if res:
            if len(res) != 1:
                print("MISMATCH DETECTED: line", n, res)
                sys.exit(1)
            grand_total += res.pop()

    if Verbose > 0:
        print()
    perf = []
    while solvers:
        cls = solvers[0].__class__
        if cls.perf: perf.append(f"{cls.__name__}: {cls.perf*1000:.1f}ms")
        del solvers[0]
    if perf:
        print("[Perf]", " | ".join(perf))
    print("[Result:GrandTotal]", grand_total)
