#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        new_string += c
    print (new_string,end = ' ')
    print('\n')
