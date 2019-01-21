#!/usr/bin/python2


from collections import defaultdict


claim_ids = []
claims = []
with open('../input.txt') as f:
    for line in f:
        claims.append(line.rstrip())

grid = defaultdict(list)
for claim in claims:
    claim_id = int(claim.split()[0].lstrip('#'))
    claim_ids.append(claim_id)
    x, y = map(int, claim.split()[3].split('x'))
    origin = map(int, claim.split()[2].rstrip(':').split(','))
    for i in xrange(1, x + 1):
        for j in xrange(1, y + 1):
            point = (origin[0] + i, origin[1] + j)
            grid[point].append(claim_id)


conflicts = 0
for point, claim_id in grid.iteritems():
    if len(claim_id) > 1:
        conflicts += 1
        for id in claim_id:
            try:
                claim_ids.remove(id)
            except:
                pass
print conflicts
for claim in claim_ids:
    print claim
