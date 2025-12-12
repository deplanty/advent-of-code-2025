from src import Debug, Reader


def batteries_value(batteries: list[int]) -> int:
    return int("".join(str(x) for x in batteries))


day = 3
example = True

debug = Debug()

# Day 3 Part 2
debug.disable()

total = 0

links = 12
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

print("Day", day, "part 2:", total)
