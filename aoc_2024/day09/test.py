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
 
    file_system = []

    count = 0
    fid = 0
    for c in data[0]:
        if (count % 2) == 0:
            formatted_number = str(fid).zfill(4)
            # print (f"File ID {formatted_number}, size {c}")
            for _ in range(int(c)):
                file_system.append(formatted_number)
            fid += 1
        else:
            filler = "."
            # print (f"Space {c}, {filler}")
            for _ in range(int(c)):
                file_system.append(filler)
        count += 1

    # print (file_system)
    # print (len(file_system))

    p_beg = 0
    p_end = len(file_system) - 1

    # for _ in range(len(file_system)):
    # print (file_system)
    while p_beg < p_end:
        if file_system[p_beg] == ".":
            # print(f"move {p_end} to {p_beg}")
            # move
            file_system[p_beg] = file_system[p_end]
            # clear out with dots
            file_system[p_end] = "."

            # find the next block to move
            while p_end >= 0 and file_system[p_end] == ".":
                p_end -= 1

        p_beg += 1
        # print (file_system)

    # print (file_system)


    # loop thru and count
    pos = 0
    for item in file_system:
        if item == ".":
            break
        else:
           total += (int(item) * pos)
        pos += 1

    return total

class FileEntry:
    def __init__(self, id, index, size):
        self.id = id
        self.index = index
        self.size = size

    def __str__(self):
        return f'FID {self.id}, idx {self.index}, sz {self.size}'

class FreeSpace:
    def __init__(self, index, size):
        self.index = index
        self.size = size

    def __str__(self):
        return f'FS idx {self.index}, sz {self.size}'

def get_free_space(free_space, size_needed):
    idx = -1

    for i in range(len(free_space)):
        if free_space[i].size >= size_needed:
            idx = i
            break

    return idx

def part2():

    # Attempt to move each file exactly once in order of decreasing file ID number starting with the 
    # file with the highest file ID number. If there is no span of free space to the left of a file 
    # that is large enough to fit the file, the file does not move.

    total = 0

    data = get_data("input.txt")
 
    file_system = []
    all_files = []
    free_space = []

    count = 0
    fid = 0
    for c in data[0]:
        if (count % 2) == 0:
            # formatted_number = str(fid).zfill(4)
            formatted_number = str(fid)
            fe = FileEntry(formatted_number, 0, int(c))
            for _ in range(int(c)):
                file_system.append(formatted_number)
                if fe.index == 0:
                    index_of_new_item = len(file_system) - 1
                    fe.index = index_of_new_item
            # print (fe)
            all_files.append(fe)
            fid += 1
        else:
            if int(c) > 0:
                filler = "."
                fs = FreeSpace(0, int(c))
                for _ in range(int(c)):
                    file_system.append(filler)
                    if fs.index == 0:
                       index_of_new_item = len(file_system) - 1
                       fs.index = index_of_new_item
                # print (fs)
                free_space.append(fs)

        count += 1

    # print (file_system)
    # print (len(file_system))
    # for x in all_files:
    #     print(x)
    # for x in free_space:
    #     print(x)

    f_idx = 0
    s_idx = 0

    for fl in reversed(all_files):
        if fl.id == '683':
           pass

        idx = get_free_space(free_space, fl.size)
        if idx >= 0:
            fs = free_space[idx]
            if fs.index < fl.index:
                # print("Move file: ", fl, " to ", fs)
                f_idx = fl.index
                s_idx = fs.index
                for _ in range(fl.size):
                    file_system[s_idx] = file_system[f_idx]
                    file_system[f_idx] = "."
                    f_idx += 1
                    s_idx += 1

                if fl.size < fs.size:
                    fs.index += fl.size
                    fs.size -= fl.size
                elif fl.size == fs.size:
                    fs.size = 0

    # print (file_system)

    # loop thru and count
    pos = 0
    for item in file_system:
        if item == ".":
            pass
        else:
           total += (int(item) * pos)
        pos += 1

    return total

def main():

    # 6430446922192
    total = part1()
    print ("Part 1:", total)
    
    # 6460170593016
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
