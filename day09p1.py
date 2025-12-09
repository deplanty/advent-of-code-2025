from itertools import combinations

from src import Debug, Reader
from src import Vector2


day = 9
example = False

debug = Debug()

# Day 8 Part 1
debug.disable()

with Reader(day, example) as reader:
    tiles = [Vector2(x, y) for x, y in reader.iter_split(",", int)]

total = 0
square: tuple[Vector2, Vector2] = (tiles[0], tiles[1])
for start, end in combinations(tiles, 2):
    width = abs(start.x - end.x) + 1
    height = abs(start.y - end.y) + 1
    area = width * height
    if area > total:
        total = area
        square = (start, end)

debug(square)
print("Day", day, "part X:", total)
