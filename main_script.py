#!/usr/bin/python3

import sys

class Ride:
    def __init__(self, begin, end, start, finish):
        _begin = begin
        _end = end
        _start = start
        _finish = finish

class Vehicle:
    def __init__(self):
        _avail = True

def parse_file(file_name):
    with open(file_name, "r") as f:
        fl = f.readlines().split(" ")
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

if __name__ == "__main__":
    main()