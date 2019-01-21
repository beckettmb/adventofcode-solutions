#!/usr/bin/python2


def find_total(plants, combos, generations, added_l = 0):
    for _ in xrange(generations):
        if plants[0] == '#':
            plants = '..' + plants
            added_l += 2
        elif plants[1] == '#':
            plants = '.' + plants
            added_l += 1

        if plants[len(plants) - 1] == "#":
            plants += '..'
        elif plants[len(plants) - 2] == '#':
            plants += '.'

        new_plants = ''
        for i, c in enumerate(plants):
            if i == 0:
                group = '..' + c + plants[i + 1] + plants[i + 2]
            elif i == 1:
                group = '.' + plants[i - 1] + c + plants[i + 1] + plants[i + 2]
            elif i == len(plants) - 1:
                group = plants[i - 2] + plants[i - 1] + c + '..'
            elif i == len(plants) - 2:
                group = plants[i - 2] + plants[i - 1] + c + plants[i + 1] + '.'
            else:
                group = plants[i - 2] + plants[i - 1] + c + plants[i + 1] + plants[i + 2]

            if group in combos:
                new_plants += '#'
            else:
                new_plants += '.'
        plants = new_plants

    return (plants, added_l)


def get_total(arg):
    plants = arg[0]
    added_l = arg[1]
    total = 0
    for i, c in enumerate(plants):
        if c == '#':
            total += (i - added_l)
    return total


def find_pattern(plants, combos, total_times):
    plants, added_l = find_total(plants, combos, 1000)
    times = 1000
    end = get_total((plants,added_l)) % 100
    patterns = [[], []]
    index = 0
    while True:
        plants, added_l = find_total(plants, combos, 1, added_l)
        times += 1
        total = get_total((plants, added_l))
        patterns[index].append(total)
        if total % 100 == end:
            index += 1
            if index == 2:
                break

    diffs = set()
    for i in xrange(len(patterns[0])):
        diffs.add(patterns[1][i] - patterns[0][i])
    
    if len(diffs) == 1:
        print total + (list(diffs)[0] * ((total_times - times) / len(patterns[0])))


combos = {}
with open('../input.txt') as f:
    for line in f:
        if 'initial' in line:
            plants = line.rstrip().split()[2]
        if line == '\n':
            pass
        else:
            if line.rstrip().split()[2] == '#':
                combos[line.rstrip().split()[0]] = '#'

print get_total(find_total(plants, combos, 20))
find_pattern(plants, combos, 50000000000)
