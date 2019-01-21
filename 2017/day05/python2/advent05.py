#!/usr/bin/python2


maze1 = []
maze2 = []
with open('../input.txt', 'r') as f:
    for line in f:
        maze1.append(int(line.rstrip()))
        maze2.append(int(line.rstrip()))

i = 0
j = 0
c = True
while c:
    try:
        tmp = i
        i += maze1[tmp]
        maze1[tmp] += 1
        j += 1
    except IndexError:
        c = False
        print j

i = 0
j = 0
c = True
while c:
    try:
        tmp = i
        i += maze2[tmp]
        if maze2[tmp] >= 3:
            maze2[tmp] -= 1
        else:
            maze2[tmp] += 1
        j += 1
    except IndexError:
        c = False
        print j
