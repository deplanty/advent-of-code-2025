from src import Debug, Reader


day = 6
example = True

debug = Debug()

# Day 6 Part 2
debug.disable()

total = 0

# The files have no trailing whitespaces
with Reader(6, example=False) as reader:
    # Get the numbers and the operators
    lines = list()
    for line in reader.fid.readlines():
        line = line.rstrip("\n")
        lines.append(line)

# Add trailing spaces at the end of the lines if needed
sizes = [len(l) for l in lines]
size_max = max(sizes)
for i in range(len(sizes)):
    diff = size_max - len(lines[i])
    if diff > 0:
        lines[i] += " " * diff
debug("Input")
debug(*(repr(l) for l in lines), sep="\n")

debug("Extract operations")
col: int = size_max - 1
operations: list[list[str]] = list()
operation: list[str] = list()
find_operation: bool = False
op: str = ""
while col >= 0:
    # Get the numbers
    number: str = ""
    for row in range(len(lines)):
        char = lines[row][col]
        # The operation is the last char to read
        # Go to next column
        if char == "*" or char == "+":
            find_operation = True
            op = char
        elif char != " ":
            number += char

    if find_operation:
        operation.append(number)
        operation.insert(0, op)
        operations.append(operation)
        debug(operation)
        operation = list()
        col -= 1
        find_operation = False
    else:
        operation.append(number)

    col -= 1

debug("Process operations")
for op, *values in operations:
    if op == "*":
        column = 1
    else:  # == "+""
        column = 0

    numbers: list[int] = [int(x) for x in values]

    for x in numbers:
        column = eval(f"column {op} {x}")
    debug(op, numbers, column)
    total += column

print("Day", day, "part 2:", total)
