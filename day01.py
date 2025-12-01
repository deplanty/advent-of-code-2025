from src import Debug, Reader


# Part 1

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
                print(f"Unknown rotation {rotation}")

        current %= 100

        if current == 0:
            total += 1

print("Part 1:", total)


# Part 2

debug = Debug()
debug.disable()

debug("Cur", "Instr", "Next", "n", "total", sep="\t")
with Reader(1, example=False) as reader:
    total = 0
    current = 50
    for line in reader.iter_lines():
        rotation = line[0]
        delta = int(line[1:])
        n, delta = divmod(delta, 100)

        current_next = 0
        match rotation.lower():
            case "r":
                current_next = current + delta
            case "l":
                current_next = current - delta
            case _:
                print(f"Unknown rotation {rotation}")

        if current_next >= 100:
            n += 1
            current_next -= 100
        elif current_next < 0:
            n += 1
            if current == 0:
                n -= 1
            current_next += 100
        elif current_next == 0:
            n += 1

        total += n
        debug(current, line, current_next, n, total, sep="\t")
        current = current_next

print("Part 2:", total)
