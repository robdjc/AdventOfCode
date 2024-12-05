#!/usr/bin/env python3

import sys
import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def check1(i, j, r, b, data):
    # print("Found X", i, j, r, b)

    total = 0

    # up
    if i >= 3:
        s = data[i][j] + data[i-1][j] + data[i-2][j] + data[i-3][j]
        # print ("Check up", s)
        if s == "XMAS":
            total += 1

    # up and left
    if i >= 3 and j >= 3:
        s = data[i][j] + data[i-1][j-1] + data[i-2][j-2] + data[i-3][j-3]
        # print ("Check up and left", s)
        if s == "XMAS":
            total += 1

    # up and right
    if i >= 3 and j <= (r - 4):
        s = data[i][j] + data[i-1][j+1] + data[i-2][j+2] + data[i-3][j+3]
        # print ("Check up and right", s)
        if s == "XMAS":
            total += 1

    # down
    if (i + 3) < b:
        s = data[i][j] + data[i+1][j] + data[i+2][j] + data[i+3][j]
        # print ("Check down", s)
        if s == "XMAS":
            total += 1

    # down and left
    if (i + 3) < b and j >= 3:
        s = data[i][j] + data[i+1][j-1] + data[i+2][j-2] + data[i+3][j-3]
        # print ("Check down and left", s)
        if s == "XMAS":
            total += 1

    # down and right
    if (i + 3) < b and j <= (r - 4):
        s = data[i][j] + data[i+1][j+1] + data[i+2][j+2] + data[i+3][j+3]
        # print ("Check down and right", s)
        if s == "XMAS":
            total += 1

    if j >= 3:
        s = data[i][j] + data[i][j-1] + data[i][j-2] + data[i][j-3] 
        # print ("Check left", s)
        if s == "XMAS":
            total += 1

    if j <= (r - 4):
        s = data[i][j:j+4]
        # print ("Check right", s)
        if s == "XMAS":
            total += 1

    return total

def part1():
    total = 0

    data = get_data("input.txt")

    r = len(data)
    b = len(data[0])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                total += check1(i, j, r, b, data)

    return total

def check2(i, j, r, b, data):
    # print("Found X", i, j, r, b)

    total = 0

    tl = ""
    tr = ""
    bl = ""
    br = ""

    # up and left
    if i >= 1 and j >= 1:
        tl = data[i-1][j-1]
        # print ("Check up and left", tl)

    # up and right
    if i >= 1 and j <= (r - 2):
        tr = data[i-1][j+1]
        # print ("Check up and right", s)

    # down and left
    if (i + 1) < b and j >= 1:
        bl = data[i+1][j-1]
        # print ("Check down and left", bl)

    # down and right
    if (i + 1) < b and j <= (r - 2):
        br = data[i+1][j+1]
        # print ("Check down and right", br)

    s1 = tl + "A" + br
    s2 = tr + "A" + bl
    if (s1 in ['SAM','MAS']) and (s2 in ['SAM','MAS']):
        total += 1

    return total

def part2():
    total = 0

    data = get_data("input.txt")

    r = len(data)
    b = len(data[0])

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'A':
                total += check2(i, j, r, b, data)

    return total

def main():
    # 2414
    total = part1()
    print ("Part 1:", total)
    
    # 1871
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
