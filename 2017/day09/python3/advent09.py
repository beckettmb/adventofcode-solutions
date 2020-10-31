#!/usr/bin/pypy3


with open('../input.txt', 'r') as f:
    for line in f:
        newstr = ''
        skip = False
        for l in line:
            if skip:
                skip = False
                continue
            if l == '!':
                skip = True
                continue
            newstr += l

        newerstr = ''
        skip = False
        garbage = 0
        for l in newstr.rstrip():
            if l == '>':
                skip = False
                continue
            if skip:
                garbage += 1
                continue
            if l == '<':
                skip = True
                continue
            if l == ',':
                continue
            newerstr += l

        c = 0
        score = 0
        for l in newerstr:
            if l == '{':
                c += 1
            elif l == '}':
                score += c
                c -= 1

        print(score)
        print(garbage)
