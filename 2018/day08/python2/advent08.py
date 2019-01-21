#!/usr/bin/python2


with open('../input.txt') as f:
    tree = f.readline().rstrip().split()

nodes = {}
meta_sum = 0
meta_sum_2 = 0
meta_entries = []
subnode_entries = []
next_num = 'sne'
end_node = False
current_meta_sum = 0
current_depth = 0
child_nodes = {0: []}
for number in tree:
    if next_num == 'sne':
        subnode_entries.append(int(number))
        next_num = 'me'
    elif next_num == 'me':
        meta_entries.append(int(number))
        if subnode_entries[-1] == 0:
            next_num = 'md'
            end_node = True
            current_meta_sum = 0
        else:
            current_depth += 1
            child_nodes[current_depth] = []
            next_num = 'sne'
    elif next_num == 'md':
        meta_sum += int(number)
        meta_entries[-1] -= 1
        if end_node:
            current_meta_sum += int(number)
        else:
            try:
                current_meta_sum += child_nodes[current_depth + 1][int(number) - 1]
            except:
                current_meta_sum += 0
        if meta_entries[-1] == 0:
            child_nodes[current_depth].append(current_meta_sum)
            if end_node:
                end_node = False
            del subnode_entries[-1]
            del meta_entries[-1]
            if len(subnode_entries) == 0:
                meta_sum_2 = current_meta_sum
            else:
                subnode_entries[-1] -= 1
                if subnode_entries[-1] != 0:
                    next_num = 'sne'
                else:
                    current_depth -= 1
                    current_meta_sum = 0

print meta_sum
print meta_sum_2
