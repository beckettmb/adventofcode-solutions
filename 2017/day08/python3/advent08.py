#!/usr/bin/pypy3


import operator

registers = {}
largest = 0

with open('../input.txt', 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' ')

        if line[0] not in registers:
            registers[line[0]] = 0
        if line[4] not in registers:
            registers[line[4]] = 0

        if line[5] == '>':
            if registers[line[4]] <= int(line[6]):
                continue
        elif line[5] == '<':
            if registers[line[4]] >= int(line[6]):
                continue
        elif line[5] == '==':
            if registers[line[4]] != int(line[6]):
                continue
        elif line[5] == '>=':
            if registers[line[4]] < int(line[6]):
                continue
        elif line[5] == '<=':
            if registers[line[4]] > int(line[6]):
                continue
        elif line[5] == '!=':
            if registers[line[4]] == int(line[6]):
                continue

        if line[1] == 'inc':
            registers[line[0]] += int(line[2])
            if registers[line[0]] > largest:
                largest = registers[line[0]]
        elif line[1] == 'dec':
            registers[line[0]] -= int(line[2])

print(max(registers.items(), key=operator.itemgetter(1))[1])
print(largest)
