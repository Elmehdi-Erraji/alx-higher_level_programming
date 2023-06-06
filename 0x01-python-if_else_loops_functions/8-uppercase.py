#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            ch = chr(ord(c) - 32)
        else:
            ch = c
        print("{:s}".format(ch), end="")
    print('')
