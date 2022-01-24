#!/usr/bin/env python3
import heapq
import argparse

def SetPart(part):
    global Part2, Slots
    Part2 = (part == 2)
    Slots = part * 2

ParkX = [0,1,3,5,7,9,10]
RoomX = [2,4,6,8]
CostMul = [1, 10, 100, 1000]

class State:
    def __init__(self, base=None):
        if base:
            self.correct = base.correct[:]
            self.foreign = [r[:] for r in base.foreign]
            self.park = base.park[:]
            self.r_cost = base.r_cost
            self.w_cost = base.w_cost
        else:
            self.correct = [0] * 4
            self.foreign = [[] for r in (0,1,2,3)]
            self.park = 7 * [-1]
            self.r_cost = self.w_cost = 0
        self._invalidate()

    def __lt__(self, other): return self.w_cost < other.w_cost  # classic Dijkstra
#    def __lt__(self, other): return self.r_cost < other.r_cost  # A*

    def to_tuple(self):
        if self.as_tuple: return self.as_tuple
        l = self.park[:]
        for i, c, f in zip((0,1,2,3), self.correct, self.foreign):
            l += [i] * c + f + [-1] * (Slots - c - len(f))
        self.as_tuple = tuple(l)
        return self.as_tuple

    def _invalidate(self):
        self.as_tuple = None
        return self

    def check(self):
        # move "foreign" objects that are not, in fact, foreign, into the "correct" lists
        for i in (0,1,2,3):
            while self.foreign[i] and (self.foreign[i][0] == i):
                self.correct[i] += 1
                del self.foreign[i][0]
        return self._invalidate()

    def add_to_cost(self, weight, cost):
        self.r_cost += cost
        self.w_cost += weight * cost

    def __str__(self):
        return ' '.join(
            c * "ABCD"[i] + ':' + \
            ''.join("ABCD"[x] for x in f) + \
            '.' * (Slots - c - len(f))
        for i,c,f in zip(range(4),self.correct, self.foreign)) + " " + \
        ''.join("ABCD."[x] for x in self.park) + \
        f" ({self.w_cost})"

    def path_free(self, x1, x2):
        x1, x2 = min(x1, x2), max(x1, x2)
        return not any((self.park[i] >= 0) for i in range(7) if x1 < ParkX[i] < x2)

    def generate_moves(self):
        # generate moves for parked objects
        for i in range(7):
            r = self.park[i]
            # is the object valid, is the target room available, and the path free?
            if (r >= 0) and not(self.foreign[r]) and self.path_free(ParkX[i], RoomX[r]):
                s = State(self)
                s.add_to_cost(CostMul[r], abs(ParkX[i] - RoomX[r]) + (Slots - s.correct[r]))
                s.park[i] = -1
                s.correct[r] += 1
                yield s
        # generate moves for topmost foreign objects in rooms
        for i in range(4):
            if not self.foreign[i]: continue   # no foreign objects here
            r = self.foreign[i][-1]  # what kind of object do we have here?
            move_up_steps = Slots - self.correct[i] - len(self.foreign[i]) + 1
            # can we move right into our target room?
            if not(self.foreign[r]) and self.path_free(RoomX[i], RoomX[r]):
                s = State(self)
                s.add_to_cost(CostMul[r], abs(RoomX[i] - RoomX[r]) + move_up_steps + (Slots - s.correct[r]))
                s.foreign[i].pop()
                s.correct[r] += 1
                yield s
            # else move into one of the free parking spots
            park_idx_l = park_idx_r = ParkX.index(RoomX[i] + 1)
            while  park_idx_l      and (self.park[park_idx_l - 1] < 0): park_idx_l -= 1
            while (park_idx_r < 7) and (self.park[park_idx_r]     < 0): park_idx_r += 1
            for j in range(park_idx_l, park_idx_r):
                s = State(self)
                s.add_to_cost(CostMul[r], abs(RoomX[i] - ParkX[j]) + move_up_steps)
                s.foreign[i].pop()
                s.park[j] = r
                yield s

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", nargs='?', default="input.txt")
    parser.add_argument("-1", dest='part', const=1, action='store_const', default=1)
    parser.add_argument("-2", dest='part', const=2, action='store_const')
    args = parser.parse_args()
    SetPart(args.part)

    with open(args.infile) as f:
        sequence = [int(c, 16) - 10 for c in f.read() if c in "ABCD"]
    if Part2:
        sequence = sequence[:4] + [3,2,1,0, 3,1,0,2] + sequence[4:]

    initial = State()
    initial.foreign = [sequence[r::4][::-1] for r in (0,1,2,3)]
    initial.check()

    final = State()
    final.correct = 4 * [Slots]

    print(str(initial))
#    for s in initial.generate_moves(): print(str(s))

    open_states = [initial]
    cost_cache = { initial.to_tuple(): initial.w_cost }
    i = 0
    while open_states:
        i += 1
        if not(i & 1023):
            print(f"{i} iterations, {len(open_states)} open states, {open_states[0].w_cost} best cost")
        state = heapq.heappop(open_states)
        if state.w_cost > cost_cache.get(state.to_tuple(), 1e10):
            continue  # we found a better path here in the meantime
        if min(state.correct) == Slots: break
        for new_state in state.generate_moves():
            if new_state.w_cost < cost_cache.get(new_state.to_tuple(), 1e10):
                cost_cache[new_state.to_tuple()] = new_state.w_cost
                heapq.heappush(open_states, new_state)
    print(str(state))
#    print(cost_cache[final.to_tuple()])
