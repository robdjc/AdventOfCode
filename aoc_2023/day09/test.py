#!/usr/bin/env python3

def get_data(filename):
    data = []
    with open(filename) as f:
        data = f.read().splitlines()
    return data

def part1():
    data = get_data("input.txt")

    total = 0
    for item in data:
        next_list = [int(x) for x in item.split()]

        sub_total = 0
        done = False
        while not done:
            # print(next_list)

            temp_list = []
            for i, j in enumerate(next_list):
                # print (i, j)
                if i > 0:
                    temp_list.append(next_list[i] - next_list[i - 1])

            if (all(x == 0 for x in temp_list)):
                done = True

            sub_total += next_list[-1]

            next_list = temp_list
        # print (sub_total)
        total += sub_total
    return total

def part2():
    data = get_data("input.txt")

    total = 0
    for item in data:
        next_list = [int(x) for x in item.split()]

        front_numbers = []
        sub_total = 0
        done = False
        while not done:
            # print(next_list)
            front_numbers.append(next_list[0])

            temp_list = []
            for i, j in enumerate(next_list):
                # print (i, j)
                if i > 0:
                    temp_list.append(next_list[i] - next_list[i - 1])

            if (all(x == 0 for x in temp_list)):
                done = True


            next_list = temp_list

        #print ("FN", front_numbers)
        prev_value = 0
        for ii in reversed(front_numbers):
            next_value = ii - prev_value
            # print(ii, prev_value, next_value)
            prev_value = next_value

        sub_total += prev_value
        # print (sub_total)
        total += sub_total

    return total

def main():
    total = part1()
    print ("Part 1:", total)
    total = part2()
    print ("Part 2:", total)

if __name__ == "__main__":
    main()