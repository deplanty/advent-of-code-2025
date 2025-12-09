from dataclasses import dataclass

from .vector2 import Vector2


@dataclass
class Rect2:
    position: Vector2 = Vector2()
    size: Vector2 = Vector2()

    @property
    def x(self) -> float:
        return self.position.x

    @property
    def y(self) -> float:
        return self.position.x

    @property
    def width(self) -> float:
        return self.size.x

    @property
    def height(self) -> float:
        return self.size.y

    def area(self) -> int:
        return self.size.x * self.size.y
