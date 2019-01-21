#!/usr/bin/python2


import sys
from collections import Counter


boxes = []
with open('../input.txt') as f:
    for id in f:
        boxes.append(id.rstrip())

l2 = 0
l3 = 0
for box in boxes:
    counter = Counter(box)
    if 2 in counter.values():
        l2 += 1
    if 3 in counter.values():
        l3 += 1

checksum = l2 * l3
print checksum

for index1, id1 in enumerate(boxes):
    for index2, id2 in enumerate(boxes):
        if index1 != index2:
            length = len(id1)
            diff = 0
            i = 0
            while i < length:
                if id1[i] != id2[i]:
                    diff += 1
                    if diff > 1:
                        break
                i += 1
            if diff == 1:
                common = ''
                j = 0
                while j < length:
                    if id1[j] == id2[j]:
                        common += id1[j]
                    j += 1
                print common
                sys.exit(0)
