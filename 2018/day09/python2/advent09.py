#!/usr/bin/python2


from collections import defaultdict, deque


def play_game(number_of_players, points):
    ring = deque([0])
    current_player = 1
    current_position = 1
    scores = defaultdict(int)
    for x in xrange(1, points + 1):
        if x % 23:
            ring.rotate(-1)
            ring.append(x)
        else:
            ring.rotate(7)
            scores[current_player] += ring.pop() + x
            ring.rotate(-1)
        current_player = (current_player + 1) % number_of_players

    return max(scores.values())


with open('../input.txt') as f:
    line = f.readline().split()
    number_of_players = int(line[0])
    points = int(line[6])

print play_game(number_of_players, points)
print play_game(number_of_players, points * 100)
