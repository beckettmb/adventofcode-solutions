#!/usr/bin/python


def spin(array, cmd):
    n = int(cmd[1:])
    for _ in xrange(n):
        new_array = []
        for i in xrange(-1, len(array) - 1):
            new_array.append(array[i])
        array = new_array
    return array


def swap(array, cmd):
    cmd = cmd[1:]
    pos = cmd.split('/')
    for index, i in enumerate(pos):
        try:
            pos[index] = int(i)
        except:
            pos[index] = array.index(i)
    array[pos[0]], array[pos[1]] = array[pos[1]], array[pos[0]]
    return array


programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

with open('input.txt') as f:
    commands = f.readline().rstrip().split(',')

seen = {}
seen[0] = 'abcdefghijklmnop'
for i in xrange(1, 1000000001):
    for cmd in commands:
        if cmd[0] == 's':
            programs = spin(programs, cmd)
        elif cmd[0] == 'p' or cmd[0] == 'x':
            programs = swap(programs, cmd)
    end_programs = ''.join(programs)
    if i == 1:
        print end_programs
    if end_programs in seen.values():
        cycle = []
        start = False
        for key, value in sorted(seen.items()):
            if value == end_programs:
                start = True
            if start:
                cycle.append(value)
        remainder = 1000000000 - i
        print cycle[remainder % len(cycle)]
        break
    seen[i] = end_programs
