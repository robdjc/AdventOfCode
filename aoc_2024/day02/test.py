#!/usr/bin/env python3

import sys

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def part1():
    data = get_data("input.txt")
    total = 0
    for item in data:
        l = item.split()
        # print(l)
        i = 0
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

def is_valid(l):
    valid = True

    i = 0
    j = len(l) - 1

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

    return valid

def part2():
    data = get_data("input.txt")
    total = 0
    for item in data:
        l = item.split()

        valid = is_valid(l)
        # print (valid, bad_index)

        if valid:
            total += 1
        else:
            print('')
            print (item)
            i = 0
            j = len(l)
            copy_is_valid = False
            for i in range(0, j):
                l1 = l.copy()
                del l1[i]
                print(l1)
                copy_is_valid = is_valid(l1)
                if copy_is_valid:
                    print("copy is valid")
                    total += 1
                    break


    return total

def main():
    # 252
    total = part1()
    print ("Part 1:", total)
    
    # 323
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
