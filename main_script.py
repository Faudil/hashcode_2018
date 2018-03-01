#!/usr/bin/python3

import sys

from hashcode import *

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
    real

if __name__ == "__main__":
    main()