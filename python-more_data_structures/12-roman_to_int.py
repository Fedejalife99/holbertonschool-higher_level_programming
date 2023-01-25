#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = 0
    largo_str = len(roman_string)
    index = 0
    if not isinstance(roman_string, str):
        return 0
    for letter in roman_string:
        if roman_string[index] == 'I' and roman_string[index + 1] != 'I':
            roman_num -= 1
        if letter == 'X':
            roman_num += 10
        if letter == 'V':
            roman_num += 5
        if letter == 'I':
            roman_num += 1
        if letter == 'L':
            roman_num += 50
        if letter == 'C':
            roman_num += 100
        if letter == 'D':
            roman_num += 500
        if letter == 'M':
            roman_num += 1000
    return roman_num
