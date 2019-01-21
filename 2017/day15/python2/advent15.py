#!/usr/bin/python2


mul_a = 16807
mul_b = 48271
div = 2147483647

with open('../input.txt') as f:
    init_a = int(f.readline().rstrip())
    init_b = int(f.readline().rstrip())

val_a = init_a
val_b = init_b
total = 0
for _ in xrange(40000000):
    val_a = (mul_a * val_a) % div
    val_b = (mul_b * val_b) % div
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print total

val_a = init_a
val_b = init_b
total = 0
for _ in xrange(5000000):
    while True:
        val_a = (mul_a * val_a) % div
        if not val_a % 4:
            break
    while True:
        val_b = (mul_b * val_b) % div
        if not val_b % 8:
            break
    if (val_a & 0xffff) == (val_b & 0xffff):
        total += 1
print total
