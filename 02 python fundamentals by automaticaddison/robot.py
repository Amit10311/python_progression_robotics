from __future__ import annotations

import math

from .core import Point, distance_between, normalize_angle


class Robot:
    """A simple robot that moves in a 2D plane."""

    def __init__(
        self,
        x: float = 0.0,
        y: float = 0.0,
        heading: float = 0.0,
        battery: float = 100.0,
        name: str = "robot",
    ) -> None:
        self.x = x
        self.y = y
        self.heading = normalize_angle(heading)
        self.battery = battery
        self.name = name

    def position(self) -> Point:
        return Point(self.x, self.y)

    def turn(self, angle_degrees: float) -> float:
        self.heading = normalize_angle(self.heading + angle_degrees)
        return self.heading

    def turn_left(self, angle_degrees: float = 90.0) -> float:
        return self.turn(angle_degrees)

    def turn_right(self, angle_degrees: float = 90.0) -> float:
        return self.turn(-angle_degrees)

    def move(self, distance: float) -> Point:
        """Move forward (positive distance) or backward (negative distance)."""
        if distance == 0:
            return self.position()

        self.battery = max(0.0, self.battery - abs(distance) * 0.1)
        angle_radians = math.radians(self.heading)
        self.x += math.cos(angle_radians) * distance
        self.y += math.sin(angle_radians) * distance
        return self.position()

    def forward(self, distance: float) -> Point:
        return self.move(distance)

    def backward(self, distance: float) -> Point:
        return self.move(-distance)

    def distance_to(self, other: Point | tuple[float, float]) -> float:
        point = Point(*other) if isinstance(other, tuple) else other
        return distance_between(self.position(), point)

    def report(self) -> dict[str, float | str]:
        return {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "heading": self.heading,
            "battery": self.battery,
        }


class NavigationController:
    """Utility class for moving a robot to a target point."""

    def __init__(self, robot: Robot | None = None) -> None:
        self.robot = robot

    def set_robot(self, robot: Robot) -> Robot:
        self.robot = robot
        return robot

    def move_to(self, target_x: float, target_y: float, step_size: float = 1.0) -> Robot:
        if self.robot is None:
            raise ValueError("No robot is attached to this navigation controller.")

        target = Point(target_x, target_y)
        while self.robot.position().distance_to(target) > step_size:
            dx = target.x - self.robot.x
            dy = target.y - self.robot.y
            desired_heading = math.degrees(math.atan2(dy, dx))
            delta = desired_heading - self.robot.heading
            self.robot.turn(delta)
            self.robot.forward(step_size)

        return self.robot
