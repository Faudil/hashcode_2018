#!/usr/bin/python3

from hashcode import *

def solve(vehicles, rides) :
    i = 0
    for ride in rides :
        for car in vehicles :
            length = car.total_ride_length(ride)
#            print(str(length))
            if length + car._steps <= ride._finish :
                car._rides.append(i)
                car._pos = ride._end
                car._steps += length
                break
        i += 1

def find_best_car(vehicles, ride) :
    best = vehicles[0]
    length = vehicles[0].total_ride_length(ride)
    last_step = vehicles[0]._steps + length
    for car in vehicles :
        temp_len = car.total_ride_length(ride)
        if car._steps + temp_len < ride._finish and car._steps + temp_len < last_step:
            length = temp_len
            best = car
    return best, length

def solve_another(vehicles, rides) :
    i = 0
    for ride in rides :
        temp, length = find_best_car(vehicles, ride)
        temp._rides.append(i)
        temp._pos = ride._end
        temp._steps += length
        i += 1
