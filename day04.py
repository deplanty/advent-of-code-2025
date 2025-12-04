from src import Debug, Reader, Index
from src.utils import iter_index_in_field

debug = Debug()


# Part 1

total = 0

with Reader(4, example=False) as reader:
    field = reader.get_field("")
    debug.show_field(field)
    # For all the index in the field
    for index in iter_index_in_field(field):
        # Consider only the paper rolls
        if index.get(field) != "@":
            continue
        # Count the number of rolls around this one
        count = 0
        for neig in index.get_neighbours_8():
            if not neig.is_in(field):
                continue
            if neig.get(field) == "@":
                count += 1
            if count >= 4:
                break
        debug(index, count)
        # If there are fewer than 4 (< 4) rolls of paper, it can be moved
        if count < 4:
            total += 1


print("Part 1:", total)


# Part 2

total = 0

print("Part 2:", total)
