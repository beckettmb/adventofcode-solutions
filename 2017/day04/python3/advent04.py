#!/usr/bin/python3


def checkpass(passphrase, part):
    if part == 1:
        passphrase = passphrase.split()
    elif part == 2:
        passphrase = [''.join(sorted(passwd)) for passwd in passphrase.split()]
    if len(passphrase) == len(set(passphrase)):
        return True
    else:
        return False

pass_total_1 = 0
pass_total_2 = 0
with open('../input.txt', 'r') as f:
    for line in f:
        passphrase = line.rstrip()
        if checkpass(passphrase, 1):
            pass_total_1 += 1
        if checkpass(passphrase, 2):
            pass_total_2 += 1

print(pass_total_1)
print(pass_total_2)
