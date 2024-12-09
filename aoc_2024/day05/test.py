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

    rule_pairs = []
    updates = []
    good_list = []

    pairs = True
    for line in data:
        if not line:
            pairs = False
            continue

        if pairs:
            rule_pairs.append(line)
        else:
            updates.append(line)

    # print (rule_pairs)
    # print (updates)

    for update in updates:
        found = True
        # print (update)
        l = update.split(',')
        for i in range(len(l) -1):
            key = l[i]+'|'+l[i+1]
            if key in rule_pairs:
                #print("Found")
                pass
            else:
                found = False
                break
        if found:
            good_list.append(l)
    
    # print (good_list)

    for good in good_list:
        middle = len(good)//2
        val = int(good[middle])
        total += val
    return total

def part2():
    total = 0

    data = get_data("input.txt")

    return total

def main():
    # 5955
    total = part1()
    print ("Part 1:", total)
    
    # 
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
