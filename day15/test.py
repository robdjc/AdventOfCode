#!/usr/bin/env python3

import sys

multiplier = 17

def get_data(filename):

    clean_data = ""
    with open(filename) as f:
        data = f.read()
        clean_data=data.replace('\n', '')    

    return clean_data

def hash_it(s):
    sub_total = 0
    for c in s:
        sub_total += ord(c)
        sub_total = (sub_total * multiplier) % 256
    return sub_total

def part1():
    data = get_data("input.txt")

    total = 0
    sequences = data.split(',')

    for sequence in sequences:
        total += hash_it(sequence)

    return total

def part2():
    data = get_data("input.txt")

    total = 0
    sequences = data.split(',')

    lens_box = {}

    for sequence in sequences:
        sub_total = 0
        if '-' in sequence:
            temp = sequence.split('-')
            label = temp[0]
            key = hash_it(label)
            if key in lens_box:
                x = -1
                l = lens_box[key]
                for i, val in enumerate(l):
                    if label in val:
                        x = i
                        break
                if x >= 0:
                    del l[x]

        elif '=' in sequence:
            temp = sequence.split('=')
            label = temp[0]
            key = hash_it(label)
            value = "{} {}".format(label, temp[1])
            if key in lens_box:
                # add or replace
                x = -1
                l = lens_box[key]
                for i, val in enumerate(l):
                    if label in val:
                        x = i
                        break

                if x >= 0:
                    l[x] = value
                else:
                    lens_box[key].append(value)
            else:
                l = []
                l.append(value)
                lens_box[key] = l
            
        total += sub_total
    
    # for k, v in lens_box.items():
    #     if len(v) > 0:
    #         print(k, v)

    total_power = 0
    box_number = 0
    for key in range(256):
        box_number = key + 1
        if key in lens_box and len(lens_box[key]) > 0:
            temp_power = 1

            for i, value in enumerate(lens_box[key]):
                slot = i + 1
                temp = value.split()
                label = temp[0]
                length = int(temp[1])
                temp_power = box_number * slot * length
                total_power += temp_power

    return total_power

def main():
    total = part1()
    print ("Part 1:", total)
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()