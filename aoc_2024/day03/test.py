#!/usr/bin/env python3

import sys

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def part1():
    total = 0

    data = get_data("input.txt")
    for item in data:
        l = item.split()

    return total

def part2():
    total = 0

    data = get_data("input.txt")
    for item in data:
        l = item.split()

    return total

def main():
    # 252
    total = part1()
    print ("Part 1:", total)
    
    # 324
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
