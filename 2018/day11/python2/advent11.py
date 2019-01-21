#!/usr/bin/python2


with open('../input.txt') as f:
    serial = int(f.readline())

grid = []
for y in xrange(1, 301):
    line = []
    for x in xrange(1, 301):
        rack_id = x + 10
        power = (((((rack_id * y) + serial) * rack_id) / 100) % 10) - 5
        line.append(power)
    grid.append(line)

highest_x = 0
highest_y = 0
highest_power = 0
for y in xrange(298):
    for x in xrange(298):
        power = 0
        for yi in xrange(3):
            for xi in xrange(3):
                power += grid[y + yi][x + xi]
        if power > highest_power:
            highest_power = power
            highest_x = x
            highest_y = y

print str(highest_x + 1) + ',' + str(highest_y + 1)

highest_x = 0
highest_y = 0
highest_size = 0
highest_power = 0
for y in xrange(298):
    for x in xrange(298):
        if x >= y:
            square = 300 - x
        else:
            square = 300 - y
        for size in xrange(1, square):
            power = 0
            for yi in xrange(size):
                for xi in xrange(size):
                    power += grid[y + yi][x + xi]
            if power > highest_power:
                highest_power = power
                highest_x = x
                highest_y = y
                highest_size = size

print str(highest_x + 1) + ',' + str(highest_y + 1) + ',' + str(highest_size)
