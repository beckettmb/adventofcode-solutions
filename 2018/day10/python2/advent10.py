#!/usr/bin/python2


class Point(object):
    def __init__(self, posx, posy, velx, vely):
        self.posx = posx
        self.posy = posy
        self.velx = velx
        self.vely = vely

    def update(self):
        self.posx += self.velx
        self.posy += self.vely

    def revert(self):
        self.posx -= self.velx
        self.posy -= self.vely

    def get_pos(self):
        return self.posx, self.posy


def write_grid(points, maxx, maxy, offsetx, offsety):
    grid = []
    for y in xrange(maxy + offsety):
        line = []
        for x in xrange(maxx + offsetx):
            point_written = False
            for point in points:
                posx, posy = point.get_pos()
                if (posx + offsetx) == x:
                    if (posy + offsety) == y:
                        line.append('*')
                        point_written = True
                        break
            if not point_written:
                line.append('.')
        grid.append(line)

    first = None
    last = None
    for i in xrange(len(grid) - 1, -1, -1):
        if '*' not in grid[i]:
            del grid[i]
        else:
            tmpfirst = grid[i].index('*')
            tmplast = ''.join(grid[i]).rindex('*')
            if not first:
                first = tmpfirst
            elif tmpfirst < first:
                first = tmpfirst
            if not last:
                last = tmplast
            elif tmplast > last:
                last = tmplast

    for i in xrange(len(grid)):
        print ''.join(grid[i][first:last + 1])


points = []
with open('../input.txt') as f:
    for line in f:
        posx = int(line.split(',')[0].split('<')[1])
        posy = int(line.split(',')[1].split('>')[0])
        velx = int(line.split(',')[1].split('<')[1])
        vely = int(line.split(',')[2].split('>')[0])
        point = Point(posx, posy, velx, vely)
        points.append(point)

smallestx = 0
smallesty = 0
reverting = False
seconds = 0
while True:
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    offsetx = 0
    offsety = 0

    for point in points:
        posx, posy = point.get_pos()
        if posx > maxx:
            maxx = posx
        if posx < minx:
            minx = posx
        if posy > maxy:
            maxy = posy
        if posy < miny:
            miny = posy
    if minx < 0:
        offsetx = abs(minx)
    if miny < 0:
        offsety = abs(miny)

    if smallestx == 0:
        smallestx = maxx + offsetx
    elif maxx + offsetx < smallestx:
        smallestx = maxx + offsetx
    if smallesty == 0:
        smallesty = maxy + offsety
    elif maxy + offsety < smallesty:
        smallesty = maxy + offsety

    if maxx + offsetx > smallestx:
        if maxy + offsety > smallesty:
            for point in points:
                point.revert()
                reverting = True
            seconds -= 1

    if not reverting:
        for point in points:
            point.update()
        seconds += 1
    else:
            write_grid(points, maxx, maxy, offsetx, offsety)
            print seconds
            break
