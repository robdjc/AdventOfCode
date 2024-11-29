#!/usr/bin/env python3

import sys

from dataclasses import dataclass

@dataclass
class Part:
    x: int
    m: int
    a: int
    s: int

def get_data(filename):
    db1 = []
    db2 = []
    switch = False
    with open(filename) as f:
        for line in f:
            if len(line.rstrip()) == 0:
                switch = True
                continue
            if not switch:
                db1.append(line.rstrip())
            else:
                db2.append(line.rstrip())
    return db1, db2

def get_workflow(db1):
    wf = {}
    for line in db1:
        x = line[:-1].split('{')
        wf[x[0]] = x[1].split(',')
    return wf

def get_part_ratings(db2):
    pr = []
    for line in db2:
        parts = line[1:-1].split(',')
        np = Part(0, 0, 0, 0)
        for part in parts:
            t1 = part.split('=')[0]
            t2 = int(part.split('=')[1])
            if t1 == 'x':
                np.x = t2
            elif t1 == 'm':
                np.m = t2
            elif t1 == 'a':
                np.a = t2
            elif t1 == 's':
                np.s = t2
        pr.append(np)
    return pr

def get_number(part, part_type):
    pn = 0

    if part_type == 'x':
        pn = part.x
    if part_type == 'm':
        pn = part.m
    if part_type == 'a':
        pn = part.a
    if part_type == 's':
        pn = part.s

    return pn

def evaluate(part, f):
    dest = ""
    for rule in f:
        if ':' in rule:
            part_type = rule[0]
            operator = rule[1]
            number = int(rule[2:].split(':')[0])
            name = rule[2:].split(':')[1]

            if operator == '<':
                if get_number(part, part_type) < number:
                    dest = name
                    break
                else:
                    continue
            elif operator == '>':
                if get_number(part, part_type) > number:
                    dest = name
                    break
                else:
                    continue
            else:
                dest = name
        else:
            dest = rule

    return dest

def part1():
    total = 0

    db1, db2 = get_data("input.txt")

    wf = get_workflow(db1)

    pr = get_part_ratings(db2)

    for part in pr:
        f = wf['in']
        next = evaluate(part, f)
        while next not in 'AR':
            f = wf[next]
            next = evaluate(part, f)

        if next == 'A':
            total += (part.x + part.m + part.a + part.s)

    return total

def part2():
    total = 0
    return total

def main():
    total = part1()
    print ("Part 1:", total)
    # total = part2()
    # print ("Part 2:", total)

if __name__ == "__main__":
    main()