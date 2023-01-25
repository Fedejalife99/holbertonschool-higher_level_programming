#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_nums = list(set(my_list))
    suma = 0
    for element in uniq_nums:
        suma += element
    return suma
