from __future__ import annotations

"""Create points using the Point class."""
from CQs.cq03.point import Point
"""Instantiate the Point Class."""

point1: Point = Point(1.0, 2.0)
print(point1.x)
print(point1.y)
point2 = Point.scale

#Use the scale_by method to scale point1 by a factor of 2
point1.scale_by(2)
print(point1.x)
print(point1.y)

