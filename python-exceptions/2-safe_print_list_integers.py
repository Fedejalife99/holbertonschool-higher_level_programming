#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    if my_list is not my_list:
        print()
        return 0
    for elements in range(x):
        try:
            print("{:d}".format(my_list[elements]), end='')
            if elements + 1 == x:
                print()
                return elements + 1
        except (TypeError, ValueError):
            elements += 1
            continue