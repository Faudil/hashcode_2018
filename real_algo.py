
from hashcode import *

def sort_rides(rides, car, step):
    sort = rides[:]
    tv = None
    sorted = False
    while (sorted == False):
        sorted = True
        for i in range(0, len(sort) - 1):
            tv = car.total_ride_length(sort[i]) + sort[i]._start - step
            if tv > car.total_ride_length(sort[i + 1]) + sort[i + 1]._start - step:
                tmp = sort[i]
                sort[i] = sort[i + 1]
                sort[i + 1] = tmp
                sorted = False
    return sort

def get_best_ride(rides, car, step):
    ld = 100000000000
    best = -1
    for i in range(0, len(rides)):
        v = car.total_ride_length(rides[i]) + rides[i]._start + step
        if rides[i]._taken == False and ld >= v:
            best = i
            ld = v
    return best

def fastest_car(vehicules):
    return min(vehicules, key=lambda x: x._steps)._steps

def real_solve(vehicles, rides, max_step):
    step = 0
    for remain in range(len(rides), 0, -1):
        for vehicle_i in range(0, len(vehicles)):
            if vehicles[vehicle_i]._steps == fastest_car(vehicles):
                best_ride = get_best_ride(rides, vehicles[vehicle_i], vehicles[vehicle_i]._steps)
                if best_ride < 0:
                    continue
                vehicles[vehicle_i]._rides.append(best_ride)
                vehicles[vehicle_i]._steps += vehicles[vehicle_i].total_ride_length(rides[best_ride])
                vehicles[vehicle_i].pos = rides[best_ride]._end
                rides[best_ride]._taken = True
    for i in range(0, len(vehicles)):
        print(len(vehicles[i]._rides), end=" ")
        for j in range(0, len(vehicles[i]._rides)):
            print(vehicles[i]._rides[j], end=" ")
        print()
