from src import Debug, Reader


day = 2
example = True

debug = Debug()

# Day 2 Part 1
debug.disable()

total = 0

with Reader(2, example=False) as reader:
    total = 0
    for element in reader.get_line(","):
        # Get range
        start, end = (int(v) for v in element.split("-"))

        # Find invalid in the range
        invalid: list[int] = list()
        for iid in range(start, end + 1):
            iid_str = str(iid)
            n = len(iid_str)
            # Only even length can be invalid
            if n % 2 == 1:
                continue

            left = iid_str[: n // 2]
            right = iid_str[n // 2 :]

            if left == right:
                invalid.append(iid)

        debug([start, end], "->", invalid)
        total += sum(invalid)

print("Day", day, "part 1:", total)
