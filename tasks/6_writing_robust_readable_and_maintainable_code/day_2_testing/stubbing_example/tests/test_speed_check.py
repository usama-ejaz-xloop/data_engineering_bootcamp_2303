from stubbing_example import car_class, speed_check


class CarStub:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self, unused_unit=car_class.Unit.KMPH):
        return self.speed


def test_is_car_speeding_is_above_limit():
    car = CarStub(61)

    speed_check_object = speed_check.SpeedCheck(car_class.Unit.KMPH, 60)

    assert speed_check_object.is_car_speeding(car)
