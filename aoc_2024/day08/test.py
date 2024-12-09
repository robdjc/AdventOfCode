#!/usr/bin/env python3

import sys
import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self): 
        return f'Point ({self.x}, {self.y})' 

def get_points_dict(data):

    all_point_types = {}

    # convert string to list for in place changes by index
    for i in range(len(data)):
        data[i] = list(data[i])
        for j in range(len(data[i])):
            c = data[i][j]
            if c != '.':
                p = Point(i, j)
                # print (c, p)
                if c in all_point_types.keys():
                    l = all_point_types[c]
                    l.append(p)
                else:
                    l = [p]
                    all_point_types[c] = l

    return all_point_types

def part1():
    total = 0

    data = get_data("input.txt")

    # get bounds
    b = len(data)
    r = len(data[0])

    all_point_types = get_points_dict(data)

    all_points = []

    for key, value in all_point_types.items():
        # print (key)
        # for p in value:
        #     print(p)

        count = len(value)
        lines = count * (count - 1)//2
        # print(lines)

        for i in range(count):
            for j in range(count):
                if i != j:
                    p1 = value[i]
                    p2 = value[j]
                    xdiff = p1.x - p2.x
                    ydiff = p1.y - p2.y
                    p3 = Point(p2.x - xdiff, p2.y - ydiff)
                    if (p3.x < 0) or (p3.y < 0) or (p3.x >= b) or (p3.y >= r):
                        pass
                    else:
                       # print(p1, p2, xdiff, ydiff, p3)
                       if p3 not in all_points:
                           all_points.append(p3)

    total = (len(all_points))

    return total

def part2():
    total = 0

    data = get_data("input.txt")

    # get bounds
    b = len(data)
    r = len(data[0])

    all_point_types = get_points_dict(data)

    all_points = []

    for key, value in all_point_types.items():
        # print (key)
        # for p in value:
        #     print(p)

        count = len(value)
        lines = count * (count - 1)//2
        # print(lines)

        for i in range(count):
            for j in range(count):
                if i != j:
                    p1 = value[i]
                    p2 = value[j]
                    xdiff = p1.x - p2.x
                    ydiff = p1.y - p2.y

                    p3 = Point(p2.x - xdiff, p2.y - ydiff)
                    while (p3.x >= 0) and (p3.y >= 0) and (p3.x < b) and (p3.y < r):
                        if p3 not in all_points:
                            all_points.append(p3)
                        p3 = Point(p3.x - xdiff, p3.y - ydiff)

    for key, value in all_point_types.items():
        for pt in value:
            if pt not in all_points:
                all_points.append(pt)

    total = (len(all_points))

    return total

def main():

    # 426
    total = part1()
    print ("Part 1:", total)
    
    # 
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
