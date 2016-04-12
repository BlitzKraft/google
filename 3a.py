#! /usr/bin/python

'''
message[-1] = 0
digest[i] = ((129 * message[i]) XOR message[i - 1]) % 256
'''

def sasha(message):
    i = 0
    l = 16
    digest = [0] * 16
    for l in message:
        if i == 0:
            digest[i] = ((129 * message[i]) ^ 0) % 256
        else:
            digest[i] = ((129 * message[i]) ^ message[i - 1]) % 256
        i = i + 1
    return digest

print(sasha(range(0,16)))

print(sasha(test))
