#!/usr/bin/python2


import sys
from string import ascii_uppercase


def move(network_map, letters, steps, x, y, d):
    if d == 'd':
        next_step = network_map[y + 1][x]
        if next_step == '|':
            y = y + 1
            steps += 1
        elif next_step == '+':
            y = y + 1
            steps += 1
        elif next_step == '-':
            y = y + 1
            steps += 1
        elif next_step in ascii_uppercase:
            letters.append(next_step)
            y = y + 1
            steps += 1
        elif next_step == ' ':
            if network_map[y][x - 1] != ' ':
                d = 'l'
            elif network_map[y][x + 1] != ' ':
                d = 'r'
            else:
                print ''.join(letters)
                print steps
                sys.exit(0)
        else:
            sys.exit(0)

    elif d == 'u':
        next_step = network_map[y - 1][x]
        if next_step == '|':
            y = y - 1
            steps += 1
        elif next_step == '+':
            y = y - 1
            steps += 1
        elif next_step == '-':
            y = y - 1
            steps += 1
        elif next_step in ascii_uppercase:
            letters.append(next_step)
            y = y - 1
            steps += 1
        elif next_step == ' ':
            if network_map[y][x - 1] != ' ':
                d = 'l'
            elif network_map[y][x + 1] != ' ':
                d = 'r'
            else:
                print ''.join(letters)
                print steps
                sys.exit(0)
        else:
            sys.exit(0)

    elif d == 'r':
        next_step = network_map[y][x + 1]
        if next_step == '|':
            x = x + 1
            steps += 1
        elif next_step == '+':
            x = x + 1
            steps += 1
        elif next_step == '-':
            x = x + 1
            steps += 1
        elif next_step in ascii_uppercase:
            letters.append(next_step)
            x = x + 1
            steps += 1
        elif next_step == ' ':
            if network_map[y - 1][x] != ' ':
                d = 'u'
            elif network_map[y + 1][x] != ' ':
                d = 'd'
            else:
                print ''.join(letters)
                print steps
                sys.exit(0)
        else:
            sys.exit(0)
            
    elif d == 'l':
        next_step = network_map[y][x - 1]
        if next_step == '|':
            x = x - 1
            steps += 1
        elif next_step == '+':
            x = x - 1
            steps += 1
        elif next_step == '-':
            x = x - 1
            steps += 1
        elif next_step in ascii_uppercase:
            letters.append(next_step)
            x = x - 1
            steps += 1
        elif next_step == ' ':
            if network_map[y - 1][x] != ' ':
                d = 'u'
            elif network_map[y + 1][x] != ' ':
                d = 'd'
            else:
                print ''.join(letters)
                print steps
                sys.exit(0)
        else:
            sys.exit(0)

    else:
        sys.exit(0)
    return steps, x, y, d


network_map = []
with open('../input.txt') as f:
    for line in f:
        network_map.append(line.rstrip('\n'))

letters = []
steps = 1
x = network_map[0].find('|')
y = 0
d = 'd'

while True:
    steps, x, y, d = move(network_map, letters, steps, x, y, d)
