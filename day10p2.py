import numpy as np

from src import Debug, Reader


day = 10
example = True

debug = Debug()

# Day 10 Part 2
# debug.disable()

total = 0

with Reader(day, example) as reader:
    line: list[str]
    for line in reader.iter_split(" ", str):
        lights: list[bool] = [l == "#" for l in line.pop(0)[1:-1]]
        joltage: list[int] = [int(x) for x in line.pop(-1)[1:-1].split(",")]
        wires: list[list[int]] = [[int(x) for x in wire[1:-1].split(",")] for wire in line]

        matrix = np.zeros((len(joltage), len(wires)), dtype="uint")
        for row in range(len(wires)):
            for column in wires[row]:
                matrix[column, row] = 1

        target = np.array(joltage, dtype="uint")
        result = np.linalg.lstsq(matrix, joltage, 1)[0]
        debug(joltage)
        debug(matrix)
        debug(result)
        debug(np.sum(result), int(np.sum(result)))
        debug(matrix.dot(result))
        debug()

        total += int(np.sum(result))


print("Day", day, "part 2:", total)
