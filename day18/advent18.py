#!/usr/bin/python


import sys
from threading import Thread
from time import sleep


def set(regs, cmd):
    try:
        regs[cmd[1]] = int(cmd[2])
    except:
        regs[cmd[1]] = regs[cmd[2]]
    return regs


def add(regs, cmd):
    try:
        regs[cmd[1]] += int(cmd[2])
    except:
        regs[cmd[1]] += regs[cmd[2]]
    return regs


def mul(regs, cmd):
    try:
        regs[cmd[1]] *= int(cmd[2])
    except:
        regs[cmd[1]] *= regs[cmd[2]]
    return regs


def mod(regs, cmd):
    try:
        regs[cmd[1]] %= int(cmd[2])
    except:
        regs[cmd[1]] %= regs[cmd[2]]
    return regs


def jgz(regs, cmd, i):
    try:
        if int(cmd[1]) > 0:
            i += int(cmd[2])
    except:
        if regs[cmd[1]] > 0:
            try:
                i += int(cmd[2])
            except:
                i += regs[cmd[2]]
        else:
            i += 1
    return i


def run(cmds, tid, sendqueue, recvqueue, status, sent):
    regs = {}
    regs['p'] = tid
    i = 0
    while i < len(cmds):
        cmd = cmds[i]
        cmd = cmd.split()

        try:
            int(cmd[1])
        except:
            if cmd[1] not in regs:
                regs[cmd[1]] = 0

        if cmd[0] == 'set':
            regs = set(regs, cmd)

        if cmd[0] == 'add':
            regs = add(regs, cmd)

        if cmd[0] == 'mul':
            regs = mul(regs, cmd)

        if cmd[0] == 'mod':
            regs = mod(regs, cmd)

        if cmd[0] == 'snd':
            sendqueue.insert(0, regs[cmd[1]])
            if tid == 0:
                sent[0] += 1
            elif tid == 1:
                sent[1] += 1

        if cmd[0] == 'rcv':
            attempts = 0
            while True:
                if len(recvqueue) > 0:
                    regs[cmd[1]] = recvqueue.pop()
                    status[tid] = 'running'
                    break
                else:
                    status[tid] = 'waiting'
                    if (status[0] == 'waiting') and (status[1] == 'waiting'):
                        if attempts == 2:
                            if tid == 1:
                                print sent[tid]
                            sys.exit(0)
                        attempts += 1
                    sleep(0.5)

        if cmd[0] == 'jgz':
            i = jgz(regs, cmd, i)
        elif cmd[0] != 'jgz':
            i += 1
            
    print 'thread ' + str(tid) + ' finished.'


cmds = []
with open('input.txt') as f:
    for line in f:
        cmds.append(line.rstrip())

regs = {}
i = 0
while i < len(cmds):
    cmd = cmds[i]
    cmd = cmd.split()

    try:
        int(cmd[1])
    except:
        if cmd[1] not in regs:
            regs[cmd[1]] = 0

    if cmd[0] == 'set':
        regs = set(regs, cmd)

    if cmd[0] == 'add':
        regs = add(regs, cmd)

    if cmd[0] == 'mul':
        regs = mul(regs, cmd)

    if cmd[0] == 'mod':
        regs = mod(regs, cmd)

    if cmd[0] == 'snd':
        last_sound = regs[cmd[1]]

    if cmd[0] == 'rcv':
        if regs[cmd[1]] != 0:
            print last_sound
            break

    if cmd[0] == 'jgz':
        i = jgz(regs, cmd, i)
    elif cmd[0] != 'jgz':
        i += 1

queue = [[], []]
status = ['running', 'running']
sent = [0, 0]
thread0 = Thread(target = run, args = (cmds, 0, queue[0], queue[1], status, sent,))
thread1 = Thread(target = run, args = (cmds, 1, queue[1], queue[0], status, sent,))
thread0.start()
thread1.start()
