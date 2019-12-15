#!/usr/bin/env python3
import sys, traceback

examples = {
    "1,0,0,0,99": [2, 0, 0, 0, 99],
    "2,3,0,3,99": [2, 3, 0, 6, 99],
    "2,4,4,5,99,0": [2, 4, 4, 5, 99, 9801],
    "1,1,1,4,99,5,6,0,99": [30, 1, 1, 4, 2, 5, 6, 0, 99],
    "1,9,10,3,2,3,11,0,99,30,40,50": [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
}


def undefined(i):
    raise Exception("invalid opcode %s" % i)


dispatch = [lambda x, y: undefined(i) for i in range(100)]
dispatch[1] = lambda x, y: x + y
dispatch[2] = lambda x, y: x * y


def solve(intcode):
    pos = 0
    try:
        while intcode[pos] != 99:
            f = dispatch[intcode[pos]]
            res = f(intcode[intcode[pos + 1]], intcode[intcode[pos + 2]])
            intcode[intcode[pos + 3]] = res
            pos += 4
    except:
        print("Exception in user code:")
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
    return intcode


for k, v in examples.items():
    input = list(map(int, k.split(",")))
    solution = solve(input)
    # print(k, solution, v)
    assert solution == v

with open("input/2a.in") as file:
    input = list(map(int, file.read().split(",")))
    input[1] = 12
    input[2] = 2
    solution = solve(input)
    print(solution[0])
