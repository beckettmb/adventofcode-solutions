#!/usr/bin/python


group_dict = {}
program_groups = []
all_used_groups = []

with open('input.txt') as f:
    for line in f:
        line = line.rstrip().split('<')
        program = line[0].rstrip()
        line = line[1].split('>')[1]
        new_program_list = []
        for new_program in line.lstrip(' ').split(' '):
            new_program_list.append(new_program.rstrip(','))
        group_dict[program] = new_program_list

i = 0
while len(group_dict) != len(all_used_groups):
    used_groups = []
    for group in group_dict:
        if group not in all_used_groups:
            program_groups.append([group])
            break
    while len(program_groups[i]) != len(used_groups):
        groups = program_groups[i]
        for group in groups:
            if group in used_groups:
                continue
            for program in group_dict[group]:
                if program not in program_groups[i]:
                    program_groups[i].append(program)
            used_groups.append(group)
            all_used_groups.append(group)
    i += 1

for group in program_groups:
    if '0' in group:
        print len(group)
        break
print len(program_groups)
