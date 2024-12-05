#!/usr/bin/env python3

import sys
import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def part1():
    total = 0

    data = get_data("input.txt")

    return total

def part2():
    total = 0

    data = get_data("input.txt")

    return total

def main():
    # 
    total = part1()
    print ("Part 1:", total)
    
    # 
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
