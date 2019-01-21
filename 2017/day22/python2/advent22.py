#!/usr/bin/python2


def turn(direction, status):
    directions = ['u', 'r', 'd', 'l']
    if status == 0:
        direction = directions[(directions.index(direction) - 1) % 4]
    elif status == 1:
        direction = directions[(directions.index(direction) + 1) % 4]
    return direction


def move(position, direction):
    x, y = position
    if direction == 'u':
        y -= 1
    elif direction == 'd':
        y += 1
    elif direction == 'r':
        x += 1
    elif direction == 'l':
        x -= 1
    position = (x, y)
    return position

def setup():
    infected_nodes = []
    with open('../input.txt') as f:
        for i, line in enumerate(f):
            for j, char in enumerate(line.rstrip()):
                if char == '#':
                    infected_nodes.append((j, i))
        size_y = i
        size_x = j

    current_position = (size_x / 2, size_y / 2)
    direction = 'u'
    infections = 0
    return infected_nodes, current_position, direction, infections

infected_nodes, current_position, direction, infections = setup()
for _ in xrange(10000):
    if current_position in infected_nodes:
        direction = turn(direction, 1)
        infected_nodes.remove(current_position)
    else:
        direction = turn(direction, 0)
        infected_nodes.append(current_position)
        infections += 1
    current_position = move(current_position, direction)
print infections

infected_nodes, current_position, direction, infections = setup()
weakened_nodes = []
flagged_nodes = []
infections = 0
for _ in xrange(10000000):
    if current_position in infected_nodes:
        direction = turn(direction, 1)
        infected_nodes.remove(current_position)
        flagged_nodes.append(current_position)
    elif current_position in flagged_nodes:
        direction = turn(direction, 1)
        direction = turn(direction, 1)
        flagged_nodes.remove(current_position)
    elif current_position in weakened_nodes:
        weakened_nodes.remove(current_position)
        infected_nodes.append(current_position)
        infections += 1
    else:
        direction = turn(direction, 0)
        weakened_nodes.append(current_position)
    current_position = move(current_position, direction)
print infections
