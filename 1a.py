#!/usr/bin/env python3

examples= {
    "12": 2,
    "14": 2,
    "1969": 654,
    "100756": 33583
}

def solve(mass):
    return (int(mass)//3)-2

for k,v in examples.items():
    #print(k, solve(k), v)
    assert solve(k)==v

total = 0
for module in open("input/1a.in"):
	total += solve(module)

print(total)