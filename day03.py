from src import Debug, Reader


def batteries_value(batteries: list[int]) -> int:
    return int("".join(str(x) for x in batteries))


debug = Debug()

# Part 1

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

print("Part 1:", total)


# Part 2

debug.disable()
links = 12
total = 0
with Reader(3, example=False) as reader:
    for bank in reader.iter_split("", int):
        # The biggest starts with the greater digit
        # The biggest can't be after the max number of links (enough batteries left after the first)
        # first = 0  # index
        # for index in range(1, len(bank) - links):
        #     if bank[index] > bank[first]:
        #         first = index
        # debug(bank, first)

        # bank = bank[first:]
        debug(bank)
        index = 0
        while len(bank) > links and index + 1 < len(bank):
            if bank[index] < bank[index + 1]:
                debug(index, bank[index], bank[index + 1], "POP")
                bank.pop(index)
                index -= 1
                if index < 0:
                    index = 0
            else:
                debug(index, bank[index], bank[index + 1])
                index += 1
        debug(len(bank), bank)
        total += batteries_value(bank[:links])


print("Part 2:", total)
