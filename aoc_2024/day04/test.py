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
    for s in data:
        # regex can cover part1 requirements
        muls = re.findall(r'mul\([0-9]+,[0-9]+\)', s)
        for mul in muls:
            line = mul.replace('mul(','').replace(')','')
            y = line.split(',')
            total += (int(y[0]) * int(y[1]))

    return total

def part2():
    total = 0

    data = get_data("input.txt")

    add_to_total = True
    for item in data:
        for i in range(len(item)):
            if item[i:i+4] == "do()":
                add_to_total = True
            elif item[i:i+7] == "don't()":
                add_to_total = False
            elif item[i:i+4] == "mul(":
                # get data from the mul( instruction to the next closing parens
                s = (item[i+4:item.index(')', i+4)])
                if s.count(',') == 1:
                    x = s.split(',')
                    if x[0].isnumeric() and x[1].isnumeric():
                        if add_to_total:
                            total += (int(x[0]) * int(x[1]))

    return total

def main():
    # 185797128
    total = part1()
    print ("Part 1:", total)
    
    # 89798695
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
