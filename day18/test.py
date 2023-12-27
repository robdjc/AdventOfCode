#!/usr/bin/env python3

import sys

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def create_grid(x, y):
    l = []
    # plus 1 for now, not sure
    for _ in range(x + 1):
        tl = []
        for _ in range(y + 1):
            tl.append(".")
        l.append(tl)
    return l

def update_grid(grid, p):
    grid[p.x][p.y] = '#'
    # for line in grid:
    #     print (line)
    # print ()
    return

def get_area(perimeter, all_points):
    n = len(all_points) # of corners
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += all_points[i].x * all_points[j].y
        area -= all_points[j].x * all_points[i].y
    area = ((abs(area) + perimeter) // 2) + 1
    return area

def get_area_old(perimeter, all_points):

    s1 = 0
    s2 = 0
    print (len(all_points))
    for i, p in enumerate(all_points):
        ## print ("Found point ({}, {})".format(p.x, p.y))

        if i == len(all_points) - 1:
            s1 += abs(all_points[i].x * all_points[0].y)
            s2 += abs(all_points[i].y * all_points[0].x)
        else:
            s1 += abs(all_points[i].x * all_points[i+1].y)
            s2 += abs(all_points[i].y * all_points[i+1].x)

        # perimeter
        # print ("RD", s1, s2)
    return (abs(s1 - s2) + perimeter) / 2

def part1():
    total = 0

    data = get_data("input.txt")

    # pt = Point(0, 0)
    # pt_max = Point(0, 0)
    # pt_min = Point(0, 0)
    '''
    for line in data:
        direction = line.split()[0]
        length = int(line.split()[1])
        color = line.split()[2]
        if direction == 'D':
            pt.x += length
        if direction == 'U':
            pt.x -= length
        if direction == 'R':
            pt.y += length
        if direction == 'L':
            pt.y -= length

        if pt.x > pt_max.x:
            pt_max.x = pt.x
        if pt.y > pt_max.y:
            pt_max.y = pt.y

        if pt.x < pt_min.x:
            pt_min.x = pt.x
        if pt.y < pt_min.y:
            pt_min.y = pt.y
    '''
    # print(pt, pt_min, pt_max)
 
    # grid = create_grid(abs(pt_min.x) + pt_max.x, abs(pt_min.y) + pt_max.y)

    all_points = []

    # pt = Point(abs(pt_min.x), abs(pt_min.y))
    pt = Point(0, 0)

    pt2 = Point(pt.x, pt.y)
    all_points.append(pt2)

    perimeter = 0
    
    for line in data:
        direction = line.split()[0]
        length = int(line.split()[1])
        color = line.split()[2]
        perimeter += length

        if direction == 'R':
            for _ in range(length):
                # update_grid(grid, pt)
                pt.x += 1
        elif direction == 'L':
            for _ in range(length):
                # update_grid(grid, pt)
                pt.x -= 1
        elif direction == 'U':
            for _ in range(length):
                # update_grid(grid, pt)
                pt.y -= 1
        elif direction == 'D':
            for _ in range(length):
                # update_grid(grid, pt)
                pt.y += 1

        pt3 = Point(pt.x, pt.y)
        all_points.append(pt3)
    
    # print (all_points)
        
    # S1 = x1*y2 + x2*y3 + x3*y1
    # S2 = y1*x2 + y2*x3 + y3*x1
    # A = 1/2 * |S1 - S2|

    x = get_area_old(perimeter, all_points)
    print("Test 1:", x)

    y = get_area(perimeter, all_points)
    print("Test 2:", y)

    return total

def part2():
    total = 0
    return total

def main():
    total = part1()
    print ("Part 1:", total)
    # 31,527 too low
    # 106459
    # total = part2()
    # print ("Part 2:", total)

if __name__ == "__main__":
    main()
