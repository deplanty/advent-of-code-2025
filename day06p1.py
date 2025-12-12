import re

from src import Debug, Reader


day = 6
example = True

debug = Debug()

# Day 6 Part 1
debug.disable()

total = 0

with Reader(6, example=False) as reader:
    numbers: list[list[int]] = list()
    operators: list[str] = list()
    line: str
    for line in reader.iter_lines():
        line = line.lstrip(" ")
        elements: list[str] = re.split(r"\s+", line)
        if elements[0].isnumeric():
            numbers.append([int(x) for x in elements])
        else:
            operators = elements

for index in range(len(operators)):
    op = operators[index]
    if op == "*":
        column = 1
    else:  # == "+""
        column = 0

    for i in range(len(numbers)):
        column = eval(f"column {op} {numbers[i][index]}")
    total += column

print("Day", day, "part 1:", total)
