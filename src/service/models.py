from dataclasses import dataclass
from typing import Generic, List, Tuple, TypeVar

Coordinate = TypeVar('Coordinate', int, float)


@dataclass
class Point(Generic[Coordinate]):
    x: Coordinate
    y: Coordinate

    @property
    def as_tuple(self) -> Tuple[Coordinate, Coordinate]:
        return self.x, self.y


@dataclass
class Box:
    center_x: int
    center_y: int
    box_width: int
    box_height: int

    @property
    def point_1(self) -> Point:
        return Point(int(self.center_x - self.box_width / 2),
                     int(self.center_y - self.box_height / 2))

    @property
    def point_2(self) -> Point:
        return Point(int(self.center_x + self.box_width / 2),
                     int(self.center_y + self.box_height / 2))

    @property
    def box_center(self) -> Point:
        return Point(self.center_x, self.center_y)


Boxes = List[Box]
