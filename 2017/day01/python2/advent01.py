#!/usr/bin/python2


def getsum(seq, length, dist):
    sum = 0
    for i in xrange(length):
        j = (i + dist) % length
        if seq[i] is seq[j]:
            sum += int(seq[i])
    return sum

with open('../input.txt', 'r') as f:
    seq = f.readline().rstrip()
    length = len(seq)

print getsum(seq, length, 1)
print getsum(seq, length, length / 2)
