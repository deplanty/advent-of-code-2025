from itertools import combinations

from src import Debug, Reader, Vector2, Line2
from src import svg


day = 9
example = False

debug = Debug()

# Day 8 Part 1
# debug.disable()

with Reader(day, example) as reader:
    tiles = [Vector2(x, y) for x, y in reader.iter_split(",", int)]
svg.export_polygon("day09.svg", tiles)

# Here we keep the tiles [0 - 1] to connect start and end of the polygon
polygon: list[Line2] = [Line2(tiles[i - 1], tiles[i]) for i in range(len(tiles))]

total = 0
square: tuple[Vector2, Vector2] = (tiles[0], tiles[1])
for start, end in combinations(tiles, 2):
    # Find the greatest square
    width = abs(start.x - end.x) + 1
    height = abs(start.y - end.y) + 1
    area = width * height
    if area > total:
        # Get if the square is in the polygon
        borders: list[Line2] = [
            Line2(start, Vector2(end.x, start.y)),
            Line2(Vector2(end.x, start.y), end),
            Line2(end, Vector2(start.x, end.y)),
            Line2(Vector2(start.x, end.y), start),
        ]
        debug(total, area, borders)

        intersect = False
        for poly_line in polygon:
            for b_line in borders:
                if poly_line.intersect(b_line):
                    intersect = True
                    break
            if intersect:
                break

        if not intersect:
            total = area
            square = (start, end)

print("Day", day, "part X:", total)
