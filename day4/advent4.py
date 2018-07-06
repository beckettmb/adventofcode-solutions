#/usr/bin/python

def checkpass1(passphrase):
    passlist = passphrase.split()
    if len(passlist) != len(set(passlist)):
        return False
    else:
        return True

i = 0
j = 0
with open('input.txt', 'r') as f:
    for line in f:
        passphrase = line.rstrip()
        if checkpass1(passphrase):
            j += 1
        i += 1

print str(j) + "/" + str(i) + " passphrases valid"
