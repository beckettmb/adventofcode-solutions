#!/usr/bin/python


with open('input.txt', 'r') as f:
    input = f.read()
lines = input.splitlines()

checksum = 0
for line in lines:
    items = line.split('\t')
    i = 0
    max = items[i]
    min = items[i]
    i += 1
    while i < len(items):
        if int(items[i]) > int(max):
            max = items[i]
        if int(items[i]) < int(min):
            min = items[i]
        i += 1
    checksum += int(max) - int(min)
print checksum

checksum = 0
for line in lines:
    items = line.split('\t')
    i = 0
    while i < len(items):
        j = 0
        while j < len(items):
            if i == j:
                j += 1
                continue
            if int(items[i]) > int(items[j]):
                if not int(items[i]) % int(items[j]):
                    checksum += (int(items[i]) % int(items[j]))
                    break
            if int(items[j]) > int(items[i]):
                if not int(items[j]) % int(items[i]):
                    checksum += (int(items[j]) / int(items[i]))
                    break
            j += 1
        i += 1
print checksum
