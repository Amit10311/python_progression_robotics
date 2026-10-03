"""Python progression robotics package."""

from .core import Point, clamp, distance_between, normalize_angle
from .robot import NavigationController, Robot

Rover = Robot
Vector = Point

distance = distance_between

__all__ = [
    "Point",
    "Vector",
    "Robot",
    "Rover",
    "NavigationController",
    "distance",
    "distance_between",
    "normalize_angle",
    "clamp",
]
