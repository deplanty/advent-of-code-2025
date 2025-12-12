from src import Debug, Reader


class Shape:
    def __init__(self, shape: list[str]):
        self._shape = shape
        self.size = (len(self._shape), len(self._shape[0]))

    def __repr__(self) -> str:
        return " ".join(self._shape)

    def __str__(self) -> str:
        return "\n".join(self._shape)

    @property
    def area(self) -> int:
        return sum(sum(1 for x in line if x == "#") for line in self._shape)

    def get(self, i, j) -> str:
        return self._shape[i][j]

    def rotate90(self) -> "Shape":
        """Return a new shape rotated 90° clockwise"""

        shape_new: list[str] = list()
        for index in range(self.size[0]):
            new_row = [line[index] for line in self._shape[::-1]]
            shape_new.append("".join(new_row))

        return Shape(shape_new)


day = 12
example = False

debug = Debug()

# Day 12 Part 1
debug.disable()

total = 0

with Reader(day, example) as reader:
    # 6 different present shapes (3x3)
    shapes: list[Shape] = list()
    for _ in range(6):
        reader.one_line()
        shape = Shape([reader.one_line() for _ in range(3)])
        shapes.append(shape)
        reader.one_line()

    debug("Shapes:")
    for i, shape in enumerate(shapes):
        debug(f"  {i}", repr(shape), shape.area)

    # Spaces
    debug()
    debug("Regions:")
    for size_str, quantities_str in reader.iter_split(": "):
        x, y = size_str.split("x")
        x, y = int(x), int(y)
        quantities = [int(x) for x in quantities_str.split(" ")]
        debug("  -", (x, y), quantities)

        total_area_shapes = 0
        for index, quantity in enumerate(quantities):
            total_area_shapes += 9 * quantity
        # Remove all regions too small to fit all the presents (3x3)
        if total_area_shapes > x * y:
            debug("Region too small")
        else:
            total += 1


print("Day", day, "part 1:", total)
