#!/usr/bin/python


def get_lengths(keystring):
    lengths = []
    for i in keystring:
        lengths.append(ord(i))
    end_lengths = [17, 31, 73, 47, 23]
    for i in end_lengths:
        lengths.append(i)
    return lengths


def do_round(ring, lengths, curr_pos, skips):
    seq_size = len(ring)
    for length in lengths:
        length = int(length)
        j = (curr_pos + length - 1) % seq_size
        for i in range(length):
            k = (curr_pos + i) % seq_size
            if not length % 2:
                if ((k - 1) % seq_size) == j:
                    break
                ring[k], ring[j] = ring[j], ring[k]
            elif length % 2:
                if k == j:
                    break
                ring[k], ring[j] = ring[j], ring[k]
            j = (j - 1) % seq_size
        curr_pos = (curr_pos + length + skips) % seq_size
        skips += 1

    return ring, curr_pos, skips


def get_sparse_hash(lengths):
    sparse_hash = []
    for i in xrange(256):
        sparse_hash.append(i)

    curr_pos = 0
    skips = 0
    for i in xrange(64):
        sparse_hash, curr_pos, skips = do_round(sparse_hash, lengths, curr_pos, skips)
    return sparse_hash

def get_dense_hash(sparse_hash):
    dense_hash = ''
    sparse_hash = [sparse_hash[i:i + 16] for i in xrange(0, len(sparse_hash), 16)]
    for i in sparse_hash:
        k = None
        for j in i:
            if not k:
                k = j
                continue
            k = k ^ j
        dense_hash += hex(k)[2:].zfill(2)
    return dense_hash


with open('input.txt') as f:
    keystring = f.readline().rstrip()
total_squares = 0
grid = []
total_regions = 0

for i in xrange(128):
    key = keystring + '-' + str(i)
    lengths = get_lengths(key)
    sparse_hash = get_sparse_hash(lengths)
    dense_hash = get_dense_hash(sparse_hash)
    binary_string = bin(int(dense_hash, 16))[2:]
    total_squares += binary_string.count('1')
    grid.append(list(binary_string.zfill(128)))

print total_squares

regions = 2
for index1, line in enumerate(grid):
    for index2, char in enumerate(line):
        if char == '1':
            grid[index1][index2] = regions
            to_check = []
            checked = []
            if index1 != 127 and index2 == 127:
                to_check.append((index1 + 1, index2))
            elif index1 == 127 and index2 != 127:
                to_check.append((index1, index2 + 1))
            elif index1 == 127 and index2 == 127:
                pass
            else:
                to_check.append((index1 + 1, index2))
                to_check.append((index1, index2 + 1))

            while len(set(to_check)) != len(set(checked)):
                to_add = []
                for coordinate in to_check:
                    if coordinate not in checked:
                        if grid[coordinate[0]][coordinate[1]] == '1':
                            grid[coordinate[0]][coordinate[1]] = regions
                            if coordinate[1] == 0:
                                if coordinate[0] == 127:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] + 1))
                                else:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] + 1))
                                    to_check.append((coordinate[0] + 1, coordinate[1]))
                            elif coordinate[1] == 127:
                                if coordinate[0] == 0:
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                    to_check.append((coordinate[0] + 1, coordinate[1]))
                                elif coordinate[0] == 127:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                else:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                    to_check.append((coordinate[0] + 1, coordinate[1]))
                            else:
                                if coordinate[0] == 0:
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                    to_check.append((coordinate[0], coordinate[1] + 1))
                                    to_check.append((coordinate[0] + 1, coordinate[1]))
                                elif coordinate[0] == 127:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                    to_check.append((coordinate[0], coordinate[1] + 1))
                                else:
                                    to_check.append((coordinate[0] - 1, coordinate[1]))
                                    to_check.append((coordinate[0], coordinate[1] - 1))
                                    to_check.append((coordinate[0], coordinate[1] + 1))
                                    to_check.append((coordinate[0] + 1, coordinate[1]))
                        checked.append(coordinate)
                for coordinate in to_add:
                    to_check.append(coordinate)
            regions += 1

print regions - 2
