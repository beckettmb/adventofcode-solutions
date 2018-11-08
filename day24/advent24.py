#!/usr/bin/python


def build(x, components, used_components, strength, max_strength, length, long_strength):
    for component in components:
        if component in used_components:
            continue

        side1, side2 = component.split('/')
        if side1 == x:
            y = side2
            strength += (int(x) + int(y))
            used_components.append(component)

            if strength > max_strength:
                max_strength = strength

            if len(used_components) >= length:
                if len(used_components) == length:
                    if strength > long_strength:
                        long_strength = strength
                else:
                    length = len(used_components)
                    long_strength = strength

            max_strength, length, long_strength = build(y, components, used_components, strength, max_strength, length, long_strength)
            strength -= (int(x) + int(y))
            used_components.remove(component)

        elif side2 == x:
            y = side1
            strength += (int(x) + int(y))
            used_components.append(component)

            if strength > max_strength:
                max_strength = strength

            if len(used_components) >= length:
                if len(used_components) == length:
                    if strength > long_strength:
                        long_strength = strength
                else:
                    length = len(used_components)
                    long_strength = strength

            max_strength, length, long_strength = build(y, components, used_components, strength, max_strength, length, long_strength)
            strength -= (int(x) + int(y))
            used_components.remove(component)
    return max_strength, length, long_strength


components = []
with open('input.txt') as f:
    for line in f:
        components.append(line.rstrip())

x = '0' 
strength = 0
max_strength = 0
length = 0
long_strength = 0
used_components = []
max_strength, length, long_strength = build(x, components, used_components, strength, max_strength, length, long_strength)
print max_strength
print long_strength
