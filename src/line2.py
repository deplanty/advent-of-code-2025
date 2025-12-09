from dataclasses import dataclass

from .vector2 import Vector2


@dataclass
class Line2:
    start: Vector2 = Vector2()
    end: Vector2 = Vector2()

    def intersect(self, line: "Line2") -> Vector2 | None:
        xdiff = Vector2(self.start.x - self.end.x, line.start.x - line.end.x)
        ydiff = Vector2(self.start.y - self.end.y, line.start.y - line.end.y)

        def det(a: Vector2, b: Vector2):
            return a.x * b.y - a.y * b.x

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = Vector2(det(self.start, self.end), det(line.start, line.end))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div

        return Vector2(x, y)
