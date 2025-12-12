from src import Debug, Reader


def batteries_value(batteries: list[int]) -> int:
    return int("".join(str(x) for x in batteries))


day = 3
example = True

debug = Debug()

# Day 3 Part 1
debug.disable()

total = 0

with Reader(3, example=False) as reader:
    for bank in reader.iter_split("", int):
        # Initialize with the first two batteries
        batteries = bank[:2]
        # Iterate from the third battery
        for battery in bank[2:]:
            check_1 = [batteries[0], battery]
            check_2 = [batteries[1], battery]
            if batteries_value(check_1) > batteries_value(batteries):
                batteries = check_1
            if batteries_value(check_2) > batteries_value(batteries):
                batteries = check_2
        debug(bank, batteries_value(batteries))
        total += batteries_value(batteries)

print("Day", day, "part 1:", total)
