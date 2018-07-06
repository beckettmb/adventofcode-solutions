#!/usr/bin/python


from math import sqrt

with open('input.txt', 'r') as f:
    input = float(f.readline())

i = 1
while i < sqrt(input):
    if (i + 2) >= sqrt(input):
        break
    i += 2
tr = (i**2)+(i+1)
tl = (i**2)+(i+1)*2
bl = (i**2)+(i+1)*3
br = (i**2)+(i+1)*4
c = (i + 2)/2
if (input >= tr) and (input <= tl):
    x = input - tr
    y = tl - input
    if x <= y:
        print c-x+c
    if y < x:
        print c-y+c
if (input >= tl) and (input <= bl):
    x = input - tl
    y = bl - input
    if x <= y:
        print c-x+c
    if y < x:
        print c-y+c
if (input >= bl) and (input <= br):
    x = input - bl
    y = br - input
    if x <= y:
        print c-x+c
    if y < x:
        print c-y+c
if (input >= i**2) and (input <= tr):
    x = tr - input
    print abs(c-x)+c



def getsum(grid, posx, posy):
    #print grid[posx-1][posy-1]
    sum = 0
    x = 0
    while x <= 2:
        y = 0
        while y <= 2:
            try:
                if posy-y < 0 or posx-x < 0:
                    pass
                else:
                    sum += grid[posy-y][posx-x]
            except IndexError:
                #print 'error'
                pass
            y += 1
        x += 1
    grid[posy-1][posx-1] = sum
    return grid

grid = [[0,0,0],
        [0,1,0],
        [0,0,0]]
sizex = 3
sizey = 3
posx = 3
posy = 2
dir = 'l'
getsum(grid, posx, posy)
while grid[posy-1][posx-1] < input:
    if dir == 'l':
        if posx == sizex and posy == sizey:
            sizex += 2
            sizey += 2
            posx += 1
            posy += 1
            newgrid = [[] for i in range(sizex)]
            i = 0
            while i < sizex:
                newgrid[0].append(0)
                i += 1
            i = 1
            while i < sizey-1:
                newgrid[i].append(0)
                j = 0
                while j < sizex-2:
                    newgrid[i].append(grid[i-1][j])
                    j += 1
                newgrid[i].append(0)
                i += 1
            i = 0
            while i < sizex:
                newgrid[sizey-1].append(0)
                i+= 1
            grid = newgrid
        elif posx == sizex:
            dir = 'u'
    if dir == 'r':
        if posx == 1:
            dir = 'd'
    if dir == 'u':
        if posy == 1:
            dir = 'r'
    if dir == 'd':
        if posy == sizey:
            dir = 'l'
    if dir == 'l':
        posx += 1
    if dir == 'r':
        posx -= 1
    if dir == 'u':
        posy -= 1
    if dir == 'd':
        posy += 1
    getsum(grid, posx, posy)

print grid[posy-1][posx-1]
