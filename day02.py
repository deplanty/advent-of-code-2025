from src import Debug, Reader


debug = Debug()

# Part 1

debug.disable()
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

print("Part 1:", total)


# Part 2

debug.disable()
with Reader(2, example=False) as reader:
    total = 0
    for element in reader.get_line(","):
        # Get range
        start, end = (int(v) for v in element.split("-"))
        # debug([start, end])

        # Find invalid in the range
        invalid: list[int] = list()
        for iid in range(start, end + 1):
            iid_str = str(iid)
            n = len(iid_str)

            # Repeated from "every digit" to "repeated twice"
            for size in range(1, n // 2 + 1):
                # Check if the size can divide the string in equal parts
                if n / size != n // size:
                    continue
                # The first part of the string = base to check other parts
                first = iid_str[:size]
                n_sub = n // size
                for i in range(n_sub):
                    # debug(iid_str, size, first, iid_str[i * size : (i + 1) * size])
                    if first != iid_str[i * size : (i + 1) * size]:
                        # debug("BREAK")
                        break
                else:
                    # debug(iid_str, "invalid")
                    invalid.append(iid)
                    break

        debug([start, end], "->", invalid)
        total += sum(invalid)

print("Part 2:", total)
