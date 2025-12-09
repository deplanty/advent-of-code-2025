from typing import TYPE_CHECKING

# if TYPE_CHECKING:
from src import Vector2, Rect2


SVG_TEMPLATE = """<svg viewBox="{view_box.x} {view_box.y} {view_box.width} {view_box.height}" height="{view_box.height}" width="{view_box.width}" xmlns="http://www.w3.org/2000/svg">
  <polygon points="{points}" style="fill:#80a1e100;stroke:black;stroke-width:1" />
</svg>"""


def export_polygon(filename: str, points: list[Vector2]):
    inf = float("inf")
    x = [inf, -inf]
    y = [inf, -inf]
    for point in points:
        # Find min and max x
        if point.x < x[0]:
            x[0] = point.x
        if point.x > x[1]:
            x[1] = point.x
        # Find min and max y
        if point.y < y[0]:
            y[0] = point.y
        if point.y > y[1]:
            y[1] = point.y

    width = x[1] - x[0]
    height = y[1] - y[0]

    view_box = Rect2(Vector2(x[0], y[0]), Vector2(width, height))
    points_str = " ".join(f"{pt.x},{pt.y}" for pt in points)

    svg = SVG_TEMPLATE.format(view_box=view_box, points=points_str)
    with open(filename, "w") as fid:
        fid.write(svg)
