#!/usr/bin/python


def transform(rule):
    yield rule
    mirrored = rule[::-1]
    yield mirrored
    for r in rule, mirrored:
        for _ in xrange(3):
            r = tuple(zip(*r[::-1]))
            yield r
    return


def gen_rules():
    rule_book = {}
    with open('input.txt') as f:
        for line in f:
            line = line.rstrip().split(' ')
            rule_in = tuple([tuple(s) for s in line[0].split('/')])
            rule_out = tuple([tuple(s) for s in line[2].split('/')])

            for rule in transform(rule_in):
                rule_book[rule] = rule_out
    return rule_book


def count(pattern):
    count = 0
    for sub_pattern in pattern:
        count += sub_pattern.count('#')
    print count
    return


pattern = [list('.#.'), list('..#'), list('###')]
rule_book = gen_rules()

for iteration in xrange(18):
    n = len(pattern)
    
    if (n % 2) == 0:
        block_size = 2
    elif (n % 3) == 0:
        block_size = 3

    new_pattern = []
    block_lines = []
    for y in xrange(0, n, block_size):
        block_line = []
        for x in xrange(0, n, block_size):
            block = []
            for y2 in xrange(block_size):
                line = []
                for x2 in xrange(block_size):
                    line.append(pattern[y+y2][x+x2])
                block.append(tuple(line))
            block = rule_book[tuple(block)]
            block_line.append(block)
        block_lines.append(block_line)

    new_pattern = []
    for block_line in block_lines:
        new_line = []
        for x in block_line:
            for i, y in enumerate(x):
                try:
                    new_line[i].append(y)
                except:
                    new_line.append([])
                    new_line[i].append(y)
        for n in new_line:
            sub_pattern = ()
            for l in n:
                sub_pattern += l
            new_pattern.append(sub_pattern)

    pattern = tuple(new_pattern)

    if iteration == 4:
        count(pattern)

count(pattern)
