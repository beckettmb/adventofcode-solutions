#!/usr/bin/pypy3


with open('../input.txt', 'r') as f:
    maze_1 = [int(line.rstrip()) for line in f]
    maze_2 = maze_1.copy()

i = 0
steps = 0
while 0 <= i < len(maze_1):
    value = maze_1[i]
    maze_1[i] += 1
    i += value
    steps += 1
print(steps)

i = 0
steps = 0
while 0 <= i < len(maze_2):
    value = maze_2[i]
    if value >= 3:
        maze_2[i] -= 1
    else:
        maze_2[i] += 1
    i += value
    steps += 1
print(steps)
