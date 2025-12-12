from src import Debug, Reader


def merge_ranges(ranges: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = list()
    merged.append(ranges[0])
    for a, b in ranges[1:]:
        add = True
        for i, (ma, mb) in enumerate(merged):
            # If the range starts in a merged range (and ends after)
            # Then update the upper range
            if ma <= a <= mb and b > mb:
                merged[i][1] = b
                break
            # If the range ends in a merged range (and starts before)
            # Then update the lower range
            elif ma <= b <= mb and a < ma:
                merged[i][0] = a
                break
            # If the range fully contains a merged range
            # Then update the merged range
            elif a < ma and b > mb:
                merged[i][0] = a
                merged[i][1] = b
            # If the range is in a merged range
            # Then ignore it
            elif ma <= a <= mb and ma <= b <= mb:
                add = False
                continue
        else:
            if add:
                merged.append([a, b])
    return merged


day = 5
example = True

debug = Debug()

# Day 5 Part 2
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

    # Merge the ranges
    merged = merge_ranges(ranges)
    debug(merged)
    for _ in range(1000):
        prev = merge_ranges(merged)
        if prev == merged:
            break
        merged = prev
    else:
        debug("Loop ended itself")
    debug(merged)

    # Compute the size of the merged ranges
    for a, b in merged:
        total += b - a + 1

print("Day", day, "part 2:", total)
