#!/usr/bin/python2


with open('../input.txt', 'r') as f:
    lines = f.read().splitlines()

checksum = 0
for line in lines:
    items = line.split('\t')
    max = items[0]
    min = items[0]
    for item in items:
        if int(item) > int(max):
            max = item
        elif int(item) < int(min):
            min = item
    checksum += int(max) - int(min)
print checksum

checksum = 0
for line in lines:
    items = line.split('\t')
    for i in enumerate(items):
        for j in enumerate(items):
            if i[0] == j[0]:
                continue
            item1 = int(i[1])
            item2 = int(j[1])
            if item1 > item2:
                if not item1 % item2:
                    checksum += item1 % item2
                    break
            if item2 > item1:
                if not item2 % item1:
                    checksum += item2 / item1
                    break
print checksum
