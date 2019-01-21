#!/usr/bin/python2


from itertools import cycle

def get_lengths(file_name, mode):
    if mode == 1:
        with open(file_name, 'r') as f:
            lengths = f.readline().rstrip().split(',')
        return lengths

    elif mode == 2:
        with open(file_name, 'r') as f:
            length_list = f.readline().rstrip()
        lengths = []
        for i in length_list:
            lengths.append(ord(i))
        end_lengths = [17, 31, 73, 47, 23]
        for i in end_lengths:
            lengths.append(i)
        return lengths

def do_round(ring, lengths, curr_pos, skips, mode):
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

    if mode == 1:
        return ring
    elif mode == 2:
        return ring, curr_pos, skips

def get_sparse_hash(lengths, mode):
    sparse_hash = []
    for i in xrange(256):
        sparse_hash.append(i)

    if mode == 1:
        sparse_hash = do_round(sparse_hash, lengths, 0, 0, 1)
        return sparse_hash
    elif mode == 2:
        curr_pos = 0
        skips = 0
        for i in xrange(64):
            sparse_hash, curr_pos, skips = do_round(sparse_hash, lengths, curr_pos, skips, 2)
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

lengths = get_lengths('../input.txt', 1)
sparse_hash = get_sparse_hash(lengths, 1)
print sparse_hash[0] * sparse_hash[1]

lengths = get_lengths('../input.txt', 2)
sparse_hash = get_sparse_hash(lengths, 2)
print get_dense_hash(sparse_hash)
