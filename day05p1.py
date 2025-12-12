from src import Debug, Reader


day = 5
example = True

debug = Debug()

# Day 5 Part 1
debug.disable()

total = 0

with Reader(5, example=False) as reader:
    # Get all the ranges
    ranges: list[list[int]] = list()
    for line in reader.iter_lines():
        if line == "":
            break
        a, b = line.split("-")
        ranges.append([int(a), int(b)])
    debug(ranges)

    # Check all the ingredients
    for uid in reader.iter_lines(int):
        for a, b in ranges:
            if a <= uid <= b:
                total += 1
                break

print("Day", day, "part 1:", total)
