#!/usr/bin/env python3

# n. nazari nov 20 2018
import time

def freqcount(bts):
    freqs = {} 

    for bit in bts:
        if bit not in freqs:
            freqs[bit] = 1

        else:
            freqs[bit] += 1

    return freqs


class Image():
    def __init__(self, path):
        self.path = path
        with open(path, 'rb') as rawimg:
            img = rawimg.read()
            self.bts = bytearray(img)

    def __str__(self):
        return 'Path: %s' % self.path

if __name__ == '__main__':
    myimg = Image('bwimg1.jpg')
    print(myimg)
    print(myimg.bts[0])
    print(freqcount(myimg.bts))
