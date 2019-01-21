#!/usr/bin/python2


current_state = None
steps = None
states = {}
cmds = [[], []]
with open('../input.txt') as f:
    for line in f:
        if line.rstrip() == '':
            if cmds != [[], []]:
                states[state] = tuple(cmds)
            state = None
            value = None
            cmds = [[], []]
            continue
        if not current_state:
            current_state = line.split()[-1].rstrip('.')
            continue
        if not steps:
            steps = int(line.split()[-2])
            continue

        if "In state" in line:
            state = line.split()[2].rstrip(':')
            continue
        if "If the current value" in line:
            value = int(line.split()[5].rstrip(':'))
            continue

        if state != None and value != None:
            action = line.split()[1]
            if action == 'Write':
                cmds[value].append(line.split()[4].rstrip('.'))
            elif action == 'Move':
                if line.split()[6].rstrip('.') == 'right':
                    cmds[value].append('+')
                else:
                    cmds[value].append('-')
            elif action == 'Continue':
                cmds[value].append(line.split()[4].rstrip('.'))
if cmds != [[], []]:
    states[state] = tuple(cmds)

active = set()
current_position = 0
for i in xrange(steps):
    if current_position in active:
        state = states[current_state][1]
        if state[0] == '1':
            active.add(current_position)
        else:
            active.remove(current_position)
        if state[1] == '+':
            current_position += 1
        else:
            current_position -= 1
        current_state = state[2]
    else:
        state = states[current_state][0]
        if state[0] == '1':
            active.add(current_position)
        else:
            active.remove(current_position)
        if state[1] == '+':
            current_position += 1
        else:
            current_position -= 1
        current_state = state[2]
print len(active)
