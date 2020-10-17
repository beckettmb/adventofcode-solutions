#!/usr/bin/python3


import itertools


with open('../input.txt', 'r') as f:
    lines = f.read().splitlines()

checksum = 0
for line in lines:
    items = sorted(list(map(int, line.split('\t'))))
    checksum += items[-1] - items[0]
print(checksum)

checksum = 0
for line in lines:
    items = list(map(int, line.split('\t')))
    for i, j in itertools.combinations(sorted(items), 2):
        if not j % i:
            checksum += j / i
print(checksum)
