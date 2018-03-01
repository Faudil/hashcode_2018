#!/usr/bin/python3

import sys

from hashcode import *

def parse_file(file_name):
    with open(file_name, "r") as f:
        fl = str(f.readline()).split(" ")
        vehicles = [Vehicle() for i in range(0, int(fl[2]))]
        rides = []
        for line in f.readlines():
            lv = [int(i) for i in line.split(" ")]
            rides.append(Ride((lv[0], lv[1]), (lv[2], lv[3]), lv[4], lv[5]))
    return vehicles, rides


def main():
    if len(sys.argv) <= 1:
        return 0
    vehicles, rides = parse_file(sys.argv[1])
    for ride in rides:
        print(ride._begin)

if __name__ == "__main__":
    main()