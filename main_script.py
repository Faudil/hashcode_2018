#!/usr/bin/python3

import sys

from hashcode import *
<<<<<<< HEAD
from algo import *
=======
from real_algo import *
>>>>>>> a109ccf7b7f5d22d7c9b66db3a4674d12caa7fa8

def parse_file(file_name):
    with open(file_name, "r") as f:
        fl = str(f.readline()).split(" ")
        vehicles = [Vehicle() for i in range(0, int(fl[2]))]
        max_step = int(fl[-1])
        rides = []
        for line in f.readlines():
            lv = [int(i) for i in line.split(" ")]
            rides.append(Ride((lv[0], lv[1]), (lv[2], lv[3]), lv[4], lv[5]))
    return vehicles, rides, max_step

def main():
    if len(sys.argv) <= 1:
        return 0
    vehicles, rides, max_step = parse_file(sys.argv[1])
    solve_another(vehicles, rides)
    for car in vehicles :
        print(str(len(car._rides)), end='')
        for i in range(0, len(car._rides)) :
            print(" " + str(car._rides[i]), end='')
        print("")
    real_solve(vehicles, rides, max_step)

if __name__ == "__main__":
    main()