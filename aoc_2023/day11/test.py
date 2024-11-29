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

def get_ex_rows(data):
    empty_rows = []
    for i, line in enumerate(data):
        # print (line)
        if line.count('#') == 0:
            empty_rows.append(i)
    return empty_rows

def get_ex_cols(data):
    empty_cols = []

    transp = [[row[i] for row in data] for i in range(len(data[0]))]

    for i, line in enumerate(transp):
        if '#' not in line:
            empty_cols.append(i)
    return empty_cols

def expand_galaxy(exp, g, ex_rows, ex_cols):

    exp -= 1

    new_x = g.x
    for r in ex_rows:
        if g.x > r and r < g.x:
            new_x += exp
    g.x = new_x

    new_y = g.y
    for c in ex_cols:
        if g.y > c and c < g.y:
            new_y += exp
    g.y = new_y

def run(exp):
    total = 0

    data = get_data("input.txt")

    ex_rows = get_ex_rows(data)
    # print(ex_rows)

    ex_cols = get_ex_cols(data)
    # print(ex_cols)

    galaxies = []
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == '#':
                g = Point(i, j)
                expand_galaxy(exp, g, ex_rows, ex_cols)
                galaxies.append(g)
    x = 1             
    for i, g1 in enumerate(galaxies):
        for j, g2 in enumerate(galaxies[i+1:]):
            # print (x, g1, g2)
            x += 1
            total += (abs(g1.x - g2.x) + abs(g1.y - g2.y))

    return total

def part2():
    total = 0
    return total

def main():

    # 9536038
    total = run(2)
    print ("Part 1:", total)

    # 447744640566
    total = run(1000000)
    print ("Part 2:", total)

if __name__ == "__main__":
    main()