#!/usr/bin/env python3

import sys
import re

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def find_start(data):
    for i in range(len(data)):
        item = data[i]
        if '^' in item:
            # y = item.find('^')
            y = item.index('^')
            return i, y

def rotate90(direction):
    if direction == 'u':
        direction = 'r'
    elif direction == 'd':
        direction = 'l'
    elif direction == 'l':
        direction = 'u'
    elif direction == 'r':
        direction = 'd'
    return direction

def can_move(data, x, y, direction, b, r):
    nx = x
    ny = y
    valid = True
    if direction == 'u':
        nx -= 1
        if nx < 0:
            valid = False

    elif direction == 'd':
        nx += 1
        if nx >= r:
            valid = False
    elif direction == 'l':
        ny -= 1
        if ny < 0:
            valid = False
    elif direction == 'r':
        ny += 1
        if ny >= b:
            valid = False

    if valid:
        c = data[nx][ny]
        if c == '#':
            return 1 # need to rotate
        else:
            return 2 # ok to move next in the same direction
    else:
        return 3 # exited the grid
        

def move_next(data, x, y, direction):
    nx = x
    ny = y
    if direction == 'u':
        nx -= 1
    elif direction == 'd':
        nx += 1
    elif direction == 'l':
        ny -= 1
    elif direction == 'r':
        ny += 1

    # print(nx, ny)
    c = data[nx][ny]
    # print(c)

    return nx, ny

def part1():
    total = 0

    data = get_data("input.txt")

    # convert string to list for in place changes by index
    for i in range(len(data)):
        data[i] = list(data[i])

    b = len(data)
    # print(b)
    r = len(data[0])
    # print(r)

    x, y = find_start(data)
    # print(x, y)
    

    direction = 'u'

    visited = []
    key = str(x) + "|" + str(y)
    visited.append(key)

    done = False
    while not done:
        xx = can_move(data, x, y, direction, b, r)
        if xx == 2:
            nx, ny = move_next(data, x, y, direction)
        
            c = data[nx][ny]
            if c == '.':
                key = str(nx) + "|" + str(ny)
                if key not in visited:
                    visited.append(key)

            x = nx
            y = ny
        elif xx ==1:
            direction = rotate90(direction)
        else:
            done = True

    total = len(visited)
    return total

def get_baseline(data, x, y, b, r):
   
    direction = 'u'

    visited = []
    key = str(x) + "|" + str(y)
    visited.append(key)

    done = False
    while not done:
        xx = can_move(data, x, y, direction, b, r)
        if xx == 2:
            nx, ny = move_next(data, x, y, direction)
        
            c = data[nx][ny]
            if c == '.':
                key = str(nx) + "|" + str(ny)
                if key not in visited:
                    visited.append(key)

            x = nx
            y = ny
        elif xx ==1:
            direction = rotate90(direction)
        else:
            done = True

    return visited

def check_not_infinite(data, x, y, b, r):
    direction = 'u'

    key = str(x) + "|" + str(y)

    infinite = False
    loop_detect = {}

    done = False
    while not done:

        xx = can_move(data, x, y, direction, b, r)
        if xx == 2: # ok to move next in the same direction
            nx, ny = move_next(data, x, y, direction)
        
            # if the direction didn't change, then skip all this
            c = data[nx][ny]
            if c == '.':
                key = str(nx) + "|" + str(ny)
                if key in loop_detect.keys():
                    loop_detect[key] += 1
                    #print (max(loop_detect.values()))
                    if max(loop_detect.values()) > 1000:
                        print ("Infinite loop detected")
                        infinite = True
                        done = True
                else:
                    loop_detect[key] = 1

            x = nx
            y = ny
        elif xx ==1: # need to rotate
            direction = rotate90(direction)
            # print("Rotate")
        else:
            done = True # 3 exited the grid

    return infinite

def part2():
    total = 0

    data = get_data("input_small.txt")

    # convert string to list for in place changes by index
    for i in range(len(data)):
        data[i] = list(data[i])

    b = len(data)
    # print(b)
    r = len(data[0])
    # print(r)

    x, y = find_start(data)
    # print(x, y)

    baseline = get_baseline(data, x, y, b, r)
    print (baseline)
    print (len(baseline))

    for key in baseline:
        # print(baseline)
        print(key)
        cx = int(key.split('|')[0])
        cy = int(key.split('|')[1])
        # print(cx, cy)
        data[cx][cy] = '#' # place obstacle
        infinite = check_not_infinite(data, x, y, b, r)
        data[cx][cy] = '.' # renive obstacle

        if infinite:
            total += 1
    
    return total

def main():
    # 4903
    total = part1()
    print ("Part 1:", total)
    
    # 
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()
