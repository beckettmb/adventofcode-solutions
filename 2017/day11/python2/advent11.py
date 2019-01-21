#!/usr/bin/python2


with open('../input.txt', 'r') as f:
    directions = f.readline().rstrip().split(',')

n = 0
s = 0
nw = 0
se = 0
ne = 0
sw = 0
largest = 0

for d in directions:
    if d == 'n':
        n += 1
    elif d == 's':
        s += 1
    elif d == 'nw':
        nw += 1
    elif d == 'sw':
        sw += 1
    elif d == 'ne':
        ne += 1
    elif d == 'se':
        se += 1
        
    s1 = n - s
    s2 = nw - se
    s3 = ne - sw
    
    if s2 > 0 and s3 > 0:
        while s2 > 0 and s3 > 0:
            s1 += 1
            s2 -= 1
            s3 -= 1
    elif s2 < 0 and s3 < 0:
        while s2 < 0 and s3 < 0:
            s1 -= 1
            s2 += 1
            s3 += 1

    if s1 > 0 and s2 < 0:
        while s1 > 0 and s2 < 0:
            s1 -= 1
            s2 += 1
            s3 += 1
    elif s1 > 0 and s3 < 0:
        while s1 > 0 and s3 < 0:
            s1 -=1
            s2 += 1
            s3 += 1
    elif s1 < 0 and s2 > 0:
        while s1 < 0 and s2 > 0:
            s1 += 1
            s2 -= 1
            s3 -=1
    elif s1 < 0 and s3 > 0:
        while s1 < 0 and s3 > 0:
            s1 += 1
            s2 -= 1
            s3 -= 1

    if (s1 + s2 + s3) > largest:
        largest = s1 + s2 + s3

print s1 + s2 + s3
print largest
