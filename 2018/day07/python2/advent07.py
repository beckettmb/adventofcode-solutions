#!/usr/bin/python2


import collections
from string import ascii_uppercase
from copy import deepcopy, copy


steps = collections.defaultdict(list)
with open('../input.txt') as f:
    for line in f:
        step1 = line.split()[1]
        step2 = line.split()[7]
        if step1 not in steps:
            steps[step1] = []
        steps[step2].append(step1)
steps_cpy = deepcopy(steps)

steps_taken = ''
while len(steps) > 0:
    for key in sorted(steps.iterkeys()):
        value = steps[key]
        if value == []:
            steps_taken += key
            break
    for k, v in steps.iteritems():
        if key in v:
            v.remove(key)
    del steps[key]
print steps_taken

steps = steps_cpy
workers = 5
working = {}
in_progress = {}
steps_completed = ''
for worker in xrange(workers):
    working[worker] = None
total_steps = len(steps)
time = 0
while len(steps_completed) != total_steps:
    for worker in xrange(workers):
        if working[worker] != None:
            continue
        for key in sorted(steps.iterkeys()):
            value = steps[key]
            if value == []:
                working[worker] = key
                in_progress[key] = ascii_uppercase.find(key) + 61
                del steps[key]
                break
    tmp_progress = copy(in_progress)
    for k, v in in_progress.iteritems():
        tmp_progress[k] -= 1
        v -= 1
        if v == 0:
            steps_completed += k
            for k1, v1 in steps.iteritems():
                if k in v1:
                    v1.remove(k)
            del tmp_progress[k]
            for k1, v1 in working.iteritems():
                if k == v1:
                    working[k1] = None
                    break
    in_progress = copy(tmp_progress)
    time += 1

print time
