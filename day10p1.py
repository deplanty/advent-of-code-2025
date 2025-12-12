from copy import deepcopy
from itertools import combinations

from src import Debug, Reader


day = 10
example = False

debug = Debug()

# Day 10 Part 1
debug.disable()


def toggle(lights: list[bool], indices: list[int]) -> list[bool]:
    for index in indices:
        lights[index] = not lights[index]
    return lights


total = 0

with Reader(day, example) as reader:
    line: list[str]
    for line in reader.iter_split(" ", str):
        lights: list[bool] = [l == "#" for l in line.pop(0)[1:-1]]
        joltage: str = line.pop(-1)
        wires: list[list[int]] = [[int(x) for x in wire[1:-1].split(",")] for wire in line]

        debug("Lights:", lights)
        for r in range(len(wires)):
            found = False
            for comb in combinations(wires, r):
                lights_test = [False] * len(lights)
                comb_ok = list()
                done = False
                for wire in comb:
                    toggle(lights_test, wire)
                    comb_ok.append(wire)
                    if lights_test == lights:
                        done = True
                        total += len(comb_ok)
                        debug("  ", len(comb_ok), comb_ok)
                        break
                if done:
                    found = True
                    break
            if found:
                break

print("Day", day, "part 1:", total)
