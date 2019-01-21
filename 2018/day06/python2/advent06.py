#!/usr/bin/python2


import operator
import itertools


coords = []
with open('../input.txt') as f:
    for line in f:
        coords.append(line.rstrip())

minx = None
maxx = None
miny = None
maxy = None
for coord in coords:
    x, y = map(int, coord.split(','))
    if minx == None:
        minx = x
    if maxx == None:
        maxx = x
    if miny == None:
        miny = y
    if maxy == None:
        maxy = y
    if x < minx:
        minx = x
    if x > maxx:
        maxx = x
    if y < miny:
        miny = y
    if y > maxy:
        maxy = y

grid = []
for i in xrange(maxy - miny + 1):
    grid2 = []
    for j in xrange(maxx - minx + 1):
        grid2.append(' ')
    grid.append(grid2)

new_coords = {}
for index, coord in enumerate(coords):
    tmp_x, tmp_y = map(int, coord.split(','))
    new_coords[index] = (tmp_x - minx, tmp_y - miny)

max_dist = 10000
safe = 0
for iy, cy in enumerate(grid):
    for ix, cx in enumerate(cy):
        value = ' '
        dists = {}
        for index, coord in new_coords.iteritems():
            dists[index] = abs(ix - coord[0]) + abs(iy - coord[1])
        min_dist = min(dists.items(), key=operator.itemgetter(1))[1]
        found = False
        if sum(dists.values()) < max_dist:
            safe += 1
        for key, item in dists.iteritems():
            if item == min_dist:
                if found == True:
                    value = '.'
                    break
                else:
                    found = True
                    value = str(key)
        grid[iy][ix] = value

inf = []
for i in grid[0]:
    inf.append(i)
for i in grid[-1]:
    inf.append(i)
for i in grid:
    inf.append(i[0])
    inf.append(i[-1])
inf = set(inf) - set('.')

sizes = []
values = list(itertools.chain.from_iterable(grid))
for key in new_coords:
    key = str(key)
    if key not in inf:
        sizes.append(values.count(key))

print max(sizes)
print safe
