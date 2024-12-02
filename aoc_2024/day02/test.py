#!/usr/bin/env python3

import sys

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def is_valid(l):
    pass

def part1():
    data = get_data("input.txt")
    total = 0
    for item in data:
        l = item.split()
        # print(l)
        i = 1
        j = len(l) - 1

        valid = True

        initial_dir = 'D'
        if int(l[i+1]) > int(l[i]):
            initial_dir = 'U'

        for i in range(0, j):
            # at least one and at most three
            diff = abs(int(l[i+1]) - int(l[i]))
            if diff < 1 or diff > 3:
                # print ("Bad list")
                valid = False
                break
            
            new_dir = 'D'
            if int(l[i+1]) > int(l[i]):
                new_dir = 'U'

            if new_dir != initial_dir:
                # print ("Bad list 2")
                valid = False
                break

        if valid:
            total += 1

    return total

def part2():
    data = get_data("input_small.txt")
    total = 0
    for item in data:
        l = item.split()
        # print(l)
        i = 1
        j = len(l) - 1

        valid = True

        bad_level = 0

        initial_dir = 'D'
        if int(l[i+1]) > int(l[i]):
            initial_dir = 'U'

        for i in range(0, j):
            # at least one and at most three
            diff = abs(int(l[i+1]) - int(l[i]))
            if diff < 1 or diff > 3:
                # print ("Bad list")
                bad_level += 1
                if bad_level > 1:
                    valid = False
                    break
            
            new_dir = 'D'
            if int(l[i+1]) > int(l[i]):
                new_dir = 'U'

            if new_dir != initial_dir:
                # print ("Bad list 2")
                bad_level += 1
                if bad_level > 1:
                    valid = False
                    break

        if valid:
            total += 1

    return total

def main():
    # 252
    total = part1()
    print ("Part 1:", total)
    
    # 
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
