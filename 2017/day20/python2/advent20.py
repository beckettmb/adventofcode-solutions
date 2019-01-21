#!/usr/bin/python2


import collections


class Particle(object):
    def __init__(self, pid, p, v, a):
        self.pid = pid
        self.p = p
        self.v = v
        self.a = a
        self.orig_p = [x for x in self.p]
        self.orig_v = [x for x in self.v]
        self.orig_a = [x for x in self.a]


    def reset(self):
        self.p = self.orig_p
        self.v = self.orig_v
        self.a = self.orig_a

    def step(self):
        for i in xrange(3):
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def get_id(self):
        return self.pid

    def distance(self):
        return sum([abs(x) for x in self.p])

    def position(self):
        return tuple(self.p)


particles = []
with open('../input.txt') as f:
    for pid, line in enumerate(f):
        line = line.rstrip().split(', ')
        for index, values in enumerate(line):
            values = [int(x) for x in values[3:-1].lstrip().split(',')]
            if index == 0:
                p = values
            elif index == 1:
                v = values
            elif index == 2:
                a = values
        particles.append(Particle(pid, p, v, a))

closest_distance = None
closest_particle = None
for particle in particles:
    for _ in xrange(1000):
        particle.step()

    if closest_distance == None:
        closest_distance = particle.distance()
        closest_particle = particle.get_id()
    elif particle.distance() < closest_distance:
        closest_distance = particle.distance()
        closest_particle = particle.get_id()

print closest_particle

for particle in particles:
    particle.reset()

for _ in xrange(1000):
    positions = {}
    for particle in particles:
        positions[particle.get_id()] = particle.position()
    
    occurances = collections.Counter(positions.values())
    collisions = [key for key, value in positions.items() if occurances[value] > 1]
    for collision in collisions:
        delete = None
        for index, particle in enumerate(particles):
            if particle.get_id() == collision:
                delete = index
                break
        del particles[delete]

    for particle in particles:
        particle.step()
print len(particles)
