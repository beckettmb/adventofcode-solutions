#!/usr/bin/python2


import sys


nums = []
with open('../input.txt') as f:
    for num in f:
        nums.append(int(num))

sum = 0
for num in nums:
    sum += num
print sum

seen = [0]
sum = 0
while True:
    for num in nums:
        sum += num
        if sum in seen:
            print sum
            sys.exit(0)
        seen.append(sum)
