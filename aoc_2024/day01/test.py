#!/usr/bin/env python3

import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def get_lists(data):
    l1 = []
    l2 = []

    for item in data:
        tp = item.split()
        l1.append(int(tp[0]))
        l2.append(int(tp[1]))

    return l1, l2

def part1():


    
    data = get_data("input.txt")

    l1, l2 = get_lists(data)

    l1.sort()
    l2.sort()

    total = 0

    j = 0
    for i in l1:
        total += abs(i - l2[j])
        j+= 1

    return total

def part2():

    data = get_data("input.txt")

    l1, l2 = get_lists(data)

    total = 0

    all_lookups = {}

    for i in l1:

        # score = how many times l1 item appears in l2
        multiplier = all_lookups.get(i)
        if multiplier is None:
            multiplier = l2.count(i)
            all_lookups[i] = multiplier
        else:
            print("lookup worked")

        j = int(i) * multiplier
        total += j
    
    return total

def main():
    # 2264607
    total = part1()
    print ("Part 1:", total)
    
    # 19457120
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
