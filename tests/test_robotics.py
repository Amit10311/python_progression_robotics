import math

from python_progression_robotics import NavigationController, Point, Robot, clamp, distance_between, normalize_angle


def test_point_distance_and_normalization():
    a = Point(0, 0)
    b = Point(3, 4)

    assert distance_between(a, b) == 5.0
    assert normalize_angle(450.0) == 90.0
    assert normalize_angle(-45.0) == 315.0
    assert clamp(5.0, 0.0, 3.0) == 3.0


def test_robot_moves_and_turns():
    robot = Robot(x=0, y=0, heading=0)
    robot.forward(10)
    assert robot.position() == Point(10.0, 0.0)

    robot.turn_left(90)
    robot.forward(10)
    assert robot.position() == Point(10.0, 10.0)

    assert robot.distance_to((10.0, 10.0)) == 0.0
    assert robot.heading == 90.0


def test_navigation_controller_reaches_target():
    robot = Robot(x=0, y=0, heading=0, name="test-robot")
    controller = NavigationController(robot)
    controller.move_to(4, 3, step_size=1.0)

    assert math.isclose(robot.x, 4.0, abs_tol=1e-9)
    assert math.isclose(robot.y, 3.0, abs_tol=1e-9)
