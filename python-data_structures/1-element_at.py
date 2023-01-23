#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0, len(my_list)):
        if idx == i:
            print("Element at index {:d} is {:d}".format(i , my_list[i]))
        if idx > len(my_list):
            return None
