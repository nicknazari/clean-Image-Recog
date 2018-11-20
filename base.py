#!/usr/bin/env python3

# n. nazari nov 20 2018


class Image():
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return 'Path: %s' % self.path

if __name__ == '__main__':
    x = Image('test')
