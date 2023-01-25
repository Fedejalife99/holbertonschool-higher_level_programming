#!/usr/bin/python3
def common_elements(set_1, set_2):
    uniq = []
    for element in set_1:
        if element in set_2:
            uniq.append(element)
    return uniq
