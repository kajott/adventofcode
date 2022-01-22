#!/usr/bin/env python3
import re

class Cube:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        assert all((self.a[axis] < self.b[axis]) for axis in (0,1,2))

    def split_axis(self, axis, pos):
        if self.a[axis] < pos < self.b[axis]:
            an, bn = list(self.a), list(self.b)
            an[axis] = bn[axis] = pos
            yield Cube(tuple(self.a), tuple(bn))
            yield Cube(tuple(an), tuple(self.b))
        else:
            yield self

    def split(self, other):
        if self.intersects(other):
            for sx0 in self.split_axis(0, other.a[0]):
                for sx1 in sx0.split_axis(0, other.b[0]):
                    for sy0 in sx1.split_axis(1, other.a[1]):
                        for sy1 in sy0.split_axis(1, other.b[1]):
                            for sz0 in sy1.split_axis(2, other.a[2]):
                                for sz1 in sz0.split_axis(2, other.b[2]):
                                    yield sz1
        else:
            yield self

    def intersects(self, other):
        return all((self.a[axis] <= other.b[axis]) and (other.a[axis] <= self.b[axis]) for axis in (0,1,2))

    def contains(self, other):
        return all((self.a[axis] <= other.a[axis]) and (other.b[axis] <= self.b[axis]) for axis in (0,1,2))

    @property
    def volume(self):
        return (self.b[0] - self.a[0]) * (self.b[1] - self.a[1]) * (self.b[2] - self.a[2])

    def __repr__(self):
        return f"Cube({self.a[0]}, {self.b[0]}, {self.a[1]}, {self.b[1]}, {self.a[2]}, {self.b[2]}, {self.state})"

def split_cube_list(cubes, pivot):
    for c in cubes:
        yield from c.split(pivot)

if __name__ == "__main__":
    cubes = []
    for line in open("input.txt"):
        nums = list(map(int, re.findall(r'-?\d+', line)))
        new = Cube((nums[0], nums[2], nums[4]), (nums[1]+1, nums[3]+1, nums[5]+1))

        cubes = [c for c in split_cube_list(cubes, new) if not new.contains(c)]
        if line.startswith("on"):
            cubes.append(new)

    print(sum(c.volume for c in cubes))
