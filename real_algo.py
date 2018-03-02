
from hashcode import *

def get_best_ride(rides, car, step):
    ld = 100000000000
    best = -1
    for i in range(0, len(rides)):
        v = car.total_ride_length(rides[i]) + rides[i]._start - step
        if rides[i]._taken == False and ld >= v:
            best = i
            ld = v
    return best

def real_solve(vehicles, rides, max_step):
    step = 0
    for remain in range(len(rides), 0, -1):
        vehicle_i, ttt = min(enumerate(vehicles), key=lambda x: x[1]._steps)
        best_ride = get_best_ride(rides, vehicles[vehicle_i], vehicles[vehicle_i]._steps)
        if best_ride < 0:
            remain += 1
            continue
        vehicles[vehicle_i]._rides.append(best_ride)
        vehicles[vehicle_i]._steps += vehicles[vehicle_i].total_ride_length(rides[best_ride])
        vehicles[vehicle_i]._pos = rides[best_ride]._end
        rides[best_ride]._taken = True
    for i in range(0, len(vehicles)):
        print(len(vehicles[i]._rides), end=" ")
        for j in range(0, len(vehicles[i]._rides)):
            print(vehicles[i]._rides[j], end=" ")
        print()
