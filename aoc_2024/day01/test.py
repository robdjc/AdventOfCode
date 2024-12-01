#!/usr/bin/env python3

import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def get_lists():
    pass

def part1():
    data = get_data("input.txt")

    l1 = []
    l2 = []

    total = 0
    for item in data:
        tp = item.split()
        l1.append(tp[0])
        l2.append(tp[1])

    l1.sort()
    l2.sort()

    print (l1)
    print (l2)
    j = 0
    for i in l1:
        # print (int(i))
        # print (int(l2[j]))
        print(abs(int(i) - int(l2[j])))
        total += abs(int(i) - int(l2[j]))
        j+= 1

    return total

def part2():
    total = 0

    data = get_data("input.txt")

    l1 = []
    l2 = []

    total = 0
    for item in data:
        tp = item.split()
        l1.append(tp[0])
        l2.append(tp[1])

    for i in l1:
        # print(i)
        # print(l2.count(i))
        j = int(i) * l2.count(i)
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
