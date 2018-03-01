class Ride:
    def __init__(self, begin, end, start, finish):
        self._begin = begin
        self._end = end
        self._start = start
        self._finish = finish

class Vehicle:
    def __init__(self):
        self._avail = True
        self._rides = []

    def total_ride_length(self, ride):
        x_b, y_b = ride._begin
        x_e, y_e = ride._end
        x_p, y_p = _pause
        sum = abs(x_p - x_b)
        sum += abs(y_p - y_b)
        sum += abs(x_b - x_e)
        sum += abs(y_b - y_e)
        return sum

