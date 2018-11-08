#!/usr/bin/python


def send_packet(layers, delay=0, strict=False):
    severity = 0
    
    for layer, depth in layers.iteritems():
        if not (layer + delay) % (2 * (depth - 1)):
            if strict:
                return 1
            severity += (layer * depth)
    return severity


layers = {}
with open('input.txt') as f:
    for line in f:
        layers[int(line.split(':')[0])] = int(line.split(':')[1].lstrip().rstrip())

print send_packet(layers)

delay = 0
while True:
    if send_packet(layers, delay, strict=True) == 0:
        break
    delay += 1
print delay
