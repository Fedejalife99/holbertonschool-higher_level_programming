#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    if type(my_list) != list or not my_list:
        return my_list
    for element in my_list:
        if element != search:
            new_list.append(element)
        else:
            new_list.append(replace)
    return new_list
