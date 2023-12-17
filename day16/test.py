#!/usr/bin/env python3

import sys

from dataclasses import dataclass

sys.setrecursionlimit(100000)

already_split = []

@dataclass
class Point:
    x: int
    y: int
    d: str  # direction
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
    grid[p.x][p.y] = '#'
    # for line in grid:
    #     print (line)
    # print ()
    return

def get_next_direction(c, d1):
    # (.) continues in the same direction
    # (-) e/w moving continues in the same direction
    # (|) n/s moving continues in the same direction
    d2 = d1

    # (-|) split into two beams going in each of the two directions
    if c != ".":
        if d1 in "ew" and c == "|":
            d2 = 'ns'

        elif d1 in "ns" and c == "-":
            d2 = 'ew'

        # (\) e moving continues s
        elif d1 == 'e' and c == "\\":
            d2 = 's'

        # (/) e moving continues n
        elif d1 == 'e' and c == "/":
            d2 = 'n'

        # (\) w moving continues n
        elif d1 == 'w' and c == "\\":
            d2 = 'n'

        # (/) w moving continues s
        elif d1 == 'w' and c == "/":
            d2 = 's'

        # (\) n moving continues w
        elif d1 == 'n' and c == "\\":
            d2 = 'w'

        # (/) n moving continues e
        elif d1 == 'n' and c == "/":
            d2 = 'e'

        # (\) s moving continues e
        elif d1 == 's' and c == "\\":
            d2 = 'e'

        # (/) s moving continues w
        elif d1 == 's' and c == "/":
            d2 = 'w'
    
    # print (c, "next", d2)
    return d2

def get_next_point(direction, p1, data):
    p2 = Point(0, 0, "", "", False)

    top    = 0
    bottom = len(data) - 1
    left   = 0
    right  = len(data[0]) - 1

    if direction == 'e':
        if p1.y < right:
            p2.y = p1.y + 1
            p2.x = p1.x
            p2.c = data[p2.x][p2.y]
        else:
            # print ("stop right edge")
            p2.stop = True

    elif direction == 'w':
        if p1.y > left:
            p2.y = p1.y - 1
            p2.x = p1.x
            p2.c = data[p2.x][p2.y]
        else:
            # print ("stop left edge")
            p2.stop = True

    elif direction == 'n':
        if p1.x > top:
            p2.x = p1.x - 1
            p2.y = p1.y
            p2.c = data[p2.x][p2.y]
        else:
            # print("stop top edge")
            p2.stop = True

    elif direction == 's':
        if p1.x < bottom:
            p2.x = p1.x + 1
            p2.y = p1.y
            p2.c = data[p2.x][p2.y]
        else:
            # print("stop bottom edge")
            p2.stop = True
    
    p2.d = direction
    return p2

def move_light_beam(p1, data, grid):

    update_grid(grid, p1)
    direction = get_next_direction(p1.c, p1.d)

    if len(direction) > 1:
        name = "X{}Y{}".format(p1.x, p1.y)
        if name not in already_split:
            already_split.append(name)
        else:
            # print ("stopping, hit splitter a second time")
            direction = ""

    for c in direction:
        # print("go", c)
        px = get_next_point(c, p1, data)
    
        if not px.stop :
            move_light_beam(px, data, grid)

    return

def part1():
    total = 0

    data = get_data("input.txt")
    # for line in data:
    #     print (line)
    # print()
    
    grid = create_grid(data)

    p1 = Point(0, 0, 'e', data[0][0], False)
    # update_grid(grid, p1) # move this code

    move_light_beam(p1, data, grid)

    for line in grid:
        total += line.count('#')
    #     print (line)
    # print()



    return total

def part2():
    total = 0

    data = get_data("input.txt")
    # for line in data:
    #     print (line)
    # print()
    
    top    = 0
    bottom = len(data) - 1
    left   = 0
    right  = len(data[0]) - 1

    # east
    for x in range(len(data)):
        already_split.clear()
        grid = create_grid(data)
        p1 = Point(x, left, 'e', data[x][left], False)
        # print (p1)
        move_light_beam(p1, data, grid)
        sub_total = 0
        for line in grid:
            sub_total += line.count('#')
        if sub_total > total:
            total = sub_total
        # print (sub_total)

    # west
    for x in range(len(data)):
        already_split.clear()
        grid = create_grid(data)
        p1 = Point(x, right, 'w', data[x][right], False)
        # print (p1)
        move_light_beam(p1, data, grid)
        sub_total = 0
        for line in grid:
            sub_total += line.count('#')
        if sub_total > total:
            total = sub_total
        # print (sub_total)

    # south
    for y in range(len(data[0])):
        already_split.clear()
        grid = create_grid(data)
        p1 = Point(top, y, 's', data[top][y], False)
        # print (p1)
        move_light_beam(p1, data, grid)
        sub_total = 0
        for line in grid:
            sub_total += line.count('#')
        if sub_total > total:
            total = sub_total
        # print (sub_total)

    # north
    for y in range(len(data[0])):
        already_split.clear()
        grid = create_grid(data)
        p1 = Point(bottom, y, 'n', data[bottom][y], False)
        # print (p1)
        move_light_beam(p1, data, grid)
        sub_total = 0
        for line in grid:
            sub_total += line.count('#')
        if sub_total > total:
            total = sub_total
        # print (sub_total)


    return total

def main():
    total = part1()
    print ("Part 1:", total)
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()