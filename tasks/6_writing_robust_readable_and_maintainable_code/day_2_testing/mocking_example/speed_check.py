class SpeedCheck:
    def __init__(self, unit, limit):
        self.unit = unit
        self.limit = limit

    def is_car_speeding(self, car):
        return car.get_speed(self.unit) > self.limit
