#!/usr/bin/env python3

import sys
import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def permute(n, l1):

    if n == 1:
        l1.append(1)
    else:
        l2 = permute(n//2, l1)
        l1.extend(l2)

    return l1

def get_operations(l):
    nl = []
    return nl

def part1():
    total = 0

    data = get_data("input_small.txt")

    for item in data:
        line = item.split(':')
        answer = line[0]
        numbers = line[1].split()
        print (answer)
        print (numbers)
        if len(numbers) == 4:
            vals = len(numbers)
            l = permute(vals, numbers)
            print(l)
            sys.exit()

    return total

def part2():
    total = 0

    data = get_data("input_small.txt")

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
