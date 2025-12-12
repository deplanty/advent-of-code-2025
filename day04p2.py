from copy import deepcopy

from src import Debug, Reader
from src.utils import iter_index_in_field


def remove_rolls(field: list[list[str]]):
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
        # If there are fewer than 4 (< 4) rolls of paper, it can be moved
        if count < 4:
            index.set(field, "x")


day = 4
example = True

debug = Debug()

# Day 4 Part 2
debug.disable()

with Reader(4, example=False) as reader:
    field = reader.get_field("")
    debug("State initial")
    debug.show_field(field)
    debug("")
    # Avoid using a while loop
    for index in range(100):
        previous = deepcopy(field)
        debug("State", index)
        remove_rolls(field)
        debug.show_field(field)
        debug("")

        if previous == field:
            break
    else:
        print("Loop stoped itself")

total = sum(sum(int(x == "x") for x in line) for line in field)

print("Day", day, "part 2:", total)
