from dataclasses import dataclass
import math


@dataclass
class Vector2:
    x: int = 0
    y: int = 0

    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def distance_to(self, point: "Vector2") -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
