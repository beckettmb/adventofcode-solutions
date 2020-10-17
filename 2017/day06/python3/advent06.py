#!/usr/bin/pypy3


import operator

def update_banks(banks):
    maxindex, maxval = max(enumerate(banks), key=operator.itemgetter(1))
    banks[maxindex] = 0
    while maxval > 0:
        maxindex = (maxindex + 1) % len(banks)
        banks[maxindex] += 1
        maxval -= 1

    return banks

with open('../input.txt', 'r') as f:
    banks = [int(bank) for bank in f.readline().rstrip().split('\t')]

previous = set()
while True:
    if ','.join([str(num) for num in banks]) in previous:
        bankstate = banks[:]
        break
    previous.add(','.join([str(num) for num in banks])) 
    banks = update_banks(banks)

print(len(previous))

i = 0
while True:
    if banks == bankstate and i is not 0:
        break
    banks = update_banks(banks)
    i += 1

print(i)
