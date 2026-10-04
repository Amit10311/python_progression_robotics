from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Two-dimensional coordinate for simple robotics exercises."""

    x: float = 0.0
    y: float = 0.0

    def move(self, heading_degrees: float, distance: float) -> "Point":
        """Return a new point after moving a given distance in a heading."""
        angle = math.radians(heading_degrees)
        dx = math.cos(angle) * distance
        dy = math.sin(angle) * distance
        return Point(self.x + dx, self.y + dy)

    def distance_to(self, other: "Point") -> float:
        return math.hypot(other.x - self.x, other.y - self.y)


def normalize_angle(angle: float) -> float:
    """Normalize an angle in degrees to the [0, 360) range."""
    normalized = angle % 360.0
    return normalized


def clamp(value: float, minimum: float, maximum: float) -> float:
    return min(max(value, minimum), maximum)


def distance_between(a: Point | tuple[float, float], b: Point | tuple[float, float]) -> float:
    """Compute Euclidean distance between two points."""
    point_a = Point(*a) if isinstance(a, tuple) else a
    point_b = Point(*b) if isinstance(b, tuple) else b
    return point_a.distance_to(point_b)
