#!/usr/bin/env python3

examples= {
    "14": 2,
    "1969": 966,
    "100756": 50346
}

def solve(mass):
	mass = int(mass)
	total = 0
	while mass>0:
		mass = (mass//3)-2
		total += mass if mass>0 else 0
	return total

for k,v in examples.items():
    #print(k, solve(k), v)
    assert solve(k)==v

total = 0
for module in open("input/1b.in"):
	total += solve(module)

print(total)