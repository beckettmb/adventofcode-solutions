#!/usr/bin/pypy3


def get_weight(programs, relations, node):
    weight = 0
    weight += int(programs[node])

    if node in relations:
        weights = {}
        for sub_node in relations[node].split(','):
            new_weight = get_weight(programs, relations, sub_node)
            if new_weight == True:
                return True
            else:
                weights[sub_node] = new_weight

        values = [x for x in weights.values()]
        if len(set(values)) is not 1:
            error = [x for x in weights.values() if list(weights.values()).count(x) == 1]
            correct = list(set(values) - set(error))[0]
            error = error[0]
            for k, v in weights.items():
                if v == error:
                    print(programs[k] - (error - correct))
                    break
            return True
        else:
            weight += sum(weights.values())

    return weight

programs = set()
dependant = set() 
with open('../input.txt', 'r') as f:
    for line in f:
        if '->' in line:
            programs.add(line.split('(')[0].rstrip())
            for program in line.split('>')[1].rstrip().replace(' ', '').split(','):
                dependant.add(program)

root = ''.join(programs - dependant)
print(root)

programs= {}
relations = {}
with open('../input.txt', 'r') as f:
    for line in f:
        program = line.split(')')[0].split('(')
        programs[program[0].rstrip()] = int(program[1])
        if '->' in line:
            relations[program[0].rstrip()] = line.split('>')[1].strip().replace(' ', '')

get_weight(programs, relations, root)
