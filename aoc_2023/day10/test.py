#!/usr/bin/env python3

import sys
from dataclasses import dataclass

opposite_direction = { 'n': 's', 's': 'n', 'e': 'w', 'w': 'e',}

@dataclass
class Point:
    x: int
    y: int
    d: str  # direction
    pd: str  # previous direction
    c: str  # char at this location
    stop: bool


def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def create_grid(data):
    l = []
    for line in data:
        tl = []
        for _ in range(len(line)):
            tl.append(".")
        l.append(tl)
    return l

def update_grid(grid, p):
    grid[p.x][p.y] = p.c
    return

def get_start(data):
    p = Point(0, 0, "", "", "", False)
    for x, line in enumerate(data):
        if 'S' in line:
            p.x = x
            p.y = line.find('S')
            p.c = data[p.x][p.y]
    return p

def get_first_directions(pt, data):
    top = 0
    bottom = len(data) - 1
    left = 0
    right = len(data[0]) - 1

    direction = ""

    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.

    if pt.x > top:
        c = data[pt.x - 1][pt.y]
        if c in "|7F":
            direction += 'n'

    if pt.x < bottom:
        c = data[pt.x + 1][pt.y]
        if c in "|LJ":
            direction += 's'

    if pt.y > left:
        c = data[pt.x][pt.y - 1]
        if c in "-LF":
            direction += 'w'

    if pt.y < right:
        c = data[pt.x][pt.y + 1]
        if c in "-J7":
            direction += 'e'

    return direction

def get_next_direction(pt, data):

    top = 0
    bottom = len(data) - 1
    left = 0
    right = len(data[0]) - 1

    direction = ""

    # | is a vertical pipe connecting north and south.
    if pt.c in "|":
        if pt.pd != 'n' and pt.x > top:
            c = data[pt.x - 1][pt.y]
            direction += 'n'
        elif pt.pd != 's' and pt.x > top:
            c = data[pt.x + 1][pt.y]
            direction += 's'

    # - is a horizontal pipe connecting east and west.
    if pt.c in "-":
        if pt.pd != 'w' and pt.y > left:
            c = data[pt.x][pt.y - 1]
            direction += 'w'
        elif pt.pd != 'e' and pt.y < right:
            c = data[pt.x][pt.y + 1]
            direction += 'e'

    # L is a 90-degree bend connecting north and east.
    if pt.c in "L":
        if pt.pd != 'n' and pt.y > left:
            c = data[pt.x - 1][pt.y]
            direction += 'n'
        elif pt.pd != 'e' and pt.y < right:
            c = data[pt.x][pt.y + 1]
            direction += 'e'

    # J is a 90-degree bend connecting north and west.
    if pt.c in "J":
        if pt.pd != 'n' and pt.y > left:
            c = data[pt.x - 1][pt.y]
            direction += 'n'
        elif pt.pd != 'w' and pt.y < right:
            c = data[pt.x][pt.y - 1]
            direction += 'w'

    # 7 is a 90-degree bend connecting south and west.
    if pt.c in "7":
        if pt.pd != 's' and pt.y > left:
            c = data[pt.x + 1][pt.y]
            direction += 's'
        elif pt.pd != 'w' and pt.y < right:
            c = data[pt.x][pt.y - 1]
            direction += 'w'
    # F is a 90-degree bend connecting south and east.
    if pt.c in "F":
        if pt.pd != 's' and pt.y > left:
            c = data[pt.x + 1][pt.y]
            direction += 's'
        elif pt.pd != 'e' and pt.y < right:
            c = data[pt.x][pt.y + 1]
            direction += 'e'

    return direction

def get_next_move(pt, data):

    pt2 = Point(0, 0, "", "", "", False)

    # north
    if pt.d == 'n':
        c = data[pt.x - 1][pt.y]
        pt2.x = pt.x - 1
        pt2.y = pt.y
        pt2.c = c
        pt2.d = "n"
        pt2.pd = opposite_direction["n"]

    # south
    elif pt.d == 's':
        c = data[pt.x + 1][pt.y]
        pt2.x = pt.x + 1
        pt2.y = pt.y
        pt2.c = c
        pt2.d = "s"
        pt2.pd = opposite_direction["s"]

    # west
    elif pt.d == 'w':
        c = data[pt.x][pt.y - 1]
        pt2.x = pt.x
        pt2.y = pt.y - 1
        pt2.c = c
        pt2.d = "w"
        pt2.pd = opposite_direction["w"]

    # east
    elif pt.d == 'e':
        c = data[pt.x][pt.y + 1]
        pt2.x = pt.x
        pt2.y = pt.y + 1
        pt2.c = c
        pt2.d = "e"
        pt2.pd = opposite_direction["e"]

    return pt2

def part1():
    data = get_data("input.txt")
    # for line in data:
    #     print (line)
    # print()

    grid = create_grid(data)

    total = 0

    pt = get_start(data)
    # print("Start", pt)

    directions = get_first_directions(pt, data)
    pt.d = directions[0]
    total += 1
    update_grid(grid, pt)
    pt = get_next_move(pt, data)

    while not pt.stop:
        total += 1
        update_grid(grid, pt)
        direction = get_next_direction(pt, data)

        if len(direction) > 0:
            pt.d = direction[0]
            pt.pd = opposite_direction[direction[0]]
            pt = get_next_move(pt, data)
        else:
            pt.stop = True

    total = int(total/2)

    # for line in grid:
    #     print (line)
    # print ()

    return total

def part2():
    total = 0
    return total

def main():
    total = part1()
    print ("Part 1:", total)
    # total = part2()
    # print ("Part 2:", total)

if __name__ == "__main__":
    main()