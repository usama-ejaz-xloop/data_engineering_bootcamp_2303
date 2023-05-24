from mocking_example import car_class, speed_check
from unittest.mock import Mock


def test_is_car_speeding_is_above_limit():
    car = car_class.Car()
    car.get_speed = Mock(return_value=61)

    speed_check_object = speed_check.SpeedCheck(car_class.Unit.KMPH, 60)

    assert speed_check_object.is_car_speeding(car)
