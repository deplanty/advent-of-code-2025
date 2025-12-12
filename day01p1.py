from src import Debug, Reader


day = 1
example = True

debug = Debug()

# Day 1 Part 1
debug.disable()

total = 0

with Reader(1, example=False) as reader:
    total = 0
    current = 50
    for line in reader.iter_lines():
        rotation = line[0]
        delta = int(line[1:])
        match rotation.lower():
            case "r":
                current += delta
            case "l":
                current -= delta
            case _:
                debug(f"Unknown rotation {rotation}")

        current %= 100

        if current == 0:
            total += 1

print("Day", day, "part 1:", total)
