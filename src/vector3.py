from dataclasses import dataclass
import math


@dataclass
class Vector3:
    x: int = 0
    y: int = 0
    z: int = 0

    def __str__(self) -> str:
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def distance_to(self, point: "Vector3") -> float:
        return math.sqrt(
            (self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2
        )
