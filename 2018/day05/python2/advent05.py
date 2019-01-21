#!/usr/bin/python2


def collapse(polymer):
    while True:
        tmp_polymer = list(polymer)
        for i in xrange(len(tmp_polymer) - 1):
            if tmp_polymer[i].lower() == tmp_polymer[i + 1].lower():
                if tmp_polymer[i] != tmp_polymer[i + 1]:
                    tmp_polymer[i] = ' '
                    tmp_polymer[i + 1] = ' '

        new_polymer = ''.join(tmp_polymer).replace(' ', '')
        if polymer == new_polymer:
            break
        polymer = new_polymer
    return polymer


with open('../input.txt') as f:
    polymer = f.read().rstrip()

polymer = collapse(polymer)
poly_len = len(polymer)
print poly_len

units = set(polymer.lower())

for unit in units:
    tmp_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
    tmp_polymer = collapse(tmp_polymer)
    tmp_len = len(tmp_polymer)
    if tmp_len < poly_len:
        poly_len = tmp_len

print poly_len
