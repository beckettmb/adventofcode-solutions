#!/usr/bin/python


with open('input.txt', 'r') as f:
    seq = f.readline().rstrip()
length = len(seq)

i = 0
sum = 0
while i <= length - 1:
    j = (i + 1) % length
    if seq[i] is seq[j]:
        sum += int(seq[i])
    i += 1
print sum

i = 0
sum = 0
half = length / 2
while i <= length - 1:
    j = (i + half) % length
    if seq[i] is seq[j]:
        sum += int(seq[i])
    i += 1
print sum
