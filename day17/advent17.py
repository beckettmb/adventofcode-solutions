#!/usr/bin/python


with open('input.txt') as f:
    steps = int(f.readline().rstrip())

circular_buffer = [0]
current_pos = 0
length = 1
for i in xrange(1, 2018):
    current_pos = (current_pos + steps) % length
    circular_buffer.insert(current_pos + 1, i)
    current_pos += 1
    length += 1 
print circular_buffer[circular_buffer.index(2017) + 1]

current_pos = 0
length = 1
for i in xrange(1, 50000001):
    current_pos = (current_pos + steps) % length
    if current_pos == 0:
        answer = i
    current_pos += 1
    length += 1
print answer
