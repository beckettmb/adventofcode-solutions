#!/usr/bin/python2


import operator
from collections import defaultdict


input_file = []
with open('../input.txt') as f:
    for line in f:
        input_file.append(line)
input_file.sort()

guard_dict = {}
current_guard = ''
for line in input_file:
    if 'Guard #' in line:
        current_guard = line.rstrip().split()[3].lstrip('#')
        if current_guard not in guard_dict:
            guard_dict[current_guard] = defaultdict(int)
    if 'falls asleep' in line:
        sleep = int(line.split()[1].rstrip(']').split(':')[1])
    if 'wakes up' in line:
        wake = int(line.split()[1].rstrip(']').split(':')[1])
        for i in xrange(sleep, wake):
            guard_dict[current_guard][i] += 1

highest = 0
highest_sleep_count = 0
for key, val in guard_dict.iteritems():
    total = sum(val.values())
    try:
        sleep = max(val.items(), key=operator.itemgetter(1))
    except:
        pass
    if sleep[1] > highest_sleep_count:
        highest_sleep_count = sleep[1]
        highest_sleep = sleep[0]
        highest_sleep_key = key
    if total > highest:
        highest = total
        highest_key = key

print max(guard_dict[highest_key].items(), key=operator.itemgetter(1))[0] * int(highest_key)
print highest_sleep * int(highest_sleep_key)
