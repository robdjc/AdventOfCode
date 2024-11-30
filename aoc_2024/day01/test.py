#!/usr/bin/env python3

import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def part1():
    data = get_data("input.txt")

    total = 0
    for item in data:
        # print (item)
        i1 = re.search(r'[0123456789]', item).start()
        i2 = re.search(r'(?s:.*)[0123456789]', item).end()
        # print (item[i1] + item[i2 -1])
        total += int(item[i1] + item[i2 -1])

    return total

def part2():
    total = 0
    return total

def main():
    # 55971
    total = part1()
    print ("Part 1:", total)
    
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
