#!/usr/bin/python2


from math import sqrt


cmds = []
with open('../input.txt') as f:
    for line in f:
        cmds.append(line.rstrip())

regs = {}
for reg in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    regs[reg] = 0

i = 0
mul_count = 0
while i < len(cmds):
    cmd = cmds[i].split()
    cmd, x, y = cmd
    try:
        y = int(y)
    except:
        y = regs[y]

    if cmd == 'set':
        regs[x] = y
    elif cmd == 'sub':
        regs[x] -= y
    elif cmd == 'mul':
        regs[x] *= y
        mul_count += 1

    if cmd == 'jnz':
        try:
            if regs[x] != 0:
                i += y
            else:
                i += 1
        except:
            if int(x) != 0:
                i += y
            else:
                i += 1
    else:
        i += 1
print mul_count

regs = {}
for reg in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    regs[reg] = 0

i = 0
h_count = 0
for i in xrange(8):
    cmd = cmds[i].split()
    cmd, x, y = cmd
    try:
        y = int(y)
    except:
        y = regs[y]

    if cmd == 'set':
        regs[x] = y
    elif cmd == 'sub':
        regs[x] -= y
    elif cmd == 'mul':
        regs[x] *= y
        mul_count += 1

for i in xrange(regs['b'], regs['c'] + 17, 17):
    for j in xrange(2, i):
        if (i % j) == 0:
            h_count += 1
            break

print h_count
