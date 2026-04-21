from __future__ import annotations
"""Create Point Class"""

#Write a class called Point
class Point:

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init
    #Write a method that belongs to then Point Class and mutates a Point

    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor
    # Write a method that creates a new Point without mutating the original Point
    def scale(self, factor: int)-> Point:
        return Point(self.x * factor, self.y * factor)
        

