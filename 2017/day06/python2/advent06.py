#!/usr/bin/python2


import operator

banks = []
with open('../input.txt', 'r') as f:
    for bank in f.readline().rstrip().split('\t'):
        banks.append(int(bank))

previous = []
i = 0
while True:
    if banks in previous:
        bankstate = banks[:]
        break
    previous.append(banks[:]) 

    maxindex, maxval = max(enumerate(banks), key=operator.itemgetter(1))
    banks[maxindex] = 0
    while maxval > 0:
        maxindex = (maxindex + 1) % len(banks)
        banks[maxindex] += 1
        maxval -= 1

    i += 1
print i

i = 0
while True:
    if banks == bankstate and i is not 0:
        break

    maxindex, maxval = max(enumerate(banks), key=operator.itemgetter(1))
    banks[maxindex] = 0
    while maxval > 0:
        maxindex = (maxindex + 1) % len(banks)
        banks[maxindex] += 1
        maxval -= 1

    i += 1
print i
