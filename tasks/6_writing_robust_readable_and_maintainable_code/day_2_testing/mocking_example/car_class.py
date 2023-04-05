from random import randint
from enum import Enum

KM_TO_MI_CONVERSION_RATE = 0.621371


class Unit(Enum):
    KMPH = 1
    MPH = 2


class Car:
    def get_speed(self, unit=Unit.KMPH):
        """Returns car speed in a given unit (km/h or mi/h)."""
        speed_in_kmph = float(randint(30, 120))
        if unit == Unit.KMPH:
            return speed_in_kmph
        return speed_in_kmph * KM_TO_MI_CONVERSION_RATE
