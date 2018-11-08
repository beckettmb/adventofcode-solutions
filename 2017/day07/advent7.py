#!/usr/bin/python


import copy

progs1 = []
progs2 = set() 
with open('input.txt', 'r') as f:
    for line in f:
        if '->' in line:
            progs1.append(line.split('(')[0].rstrip())
            for prog in line.split('>')[1].rstrip().replace(' ', '').split(','):
                progs2.add(prog)
for prog in progs1:
    if prog not in progs2:
        print prog

progs1 = {}
progs2 = {}
with open('input.txt', 'r') as f:
    for line in f:
        prog = line.split(')')[0].split('(')
        progs1[prog[0].rstrip()] = int(prog[1])
        if '->' in line:
            progs2[prog[0].rstrip()] = line.split('>')[1].rstrip().replace(' ', '')
progs3 = copy.deepcopy(progs2)
progs4 = copy.deepcopy(progs1)
cc = True
while cc:
    for prog in progs2:
        c = True
        y = progs2[prog].split(',')
        for prog2 in y:
            try:
                x = progs2[prog2]
                c = False
            except KeyError:
                pass
        if c:
            z = set()
            for i in xrange(len(y)):
                z.add(progs1[y[i]])
            if len(z) is not 1:
                broken = progs2[prog].split(',')
                cc = False
                break
            else:
                for i in y:
                    progs1[prog] += progs1[i]
                    del progs1[i]
                del progs3[prog]
    progs2 = copy.deepcopy(progs3)
brokendict = {}
for broke in broken:
    brokendict[broke] = progs1[broke]
countMap = {}
for v in brokendict.values():
    countMap[v] = countMap.get(v,0) + 1
uni = [ k for k, v in brokendict.items() if countMap[v] == 1][0]
other = [k for k, v in brokendict.items() if countMap[v] is not 1][0]
diff = progs1[uni] - progs1[other]
print progs4[uni] - diff
