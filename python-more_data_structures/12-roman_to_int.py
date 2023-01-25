#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = 0
    largo_str = len(roman_string)
    i = 0
    if not isinstance(roman_string, str):
        return 0
    for let in roman_string:
        if let == 'I' and i < len(roman_string) -1 and roman_string[i + 1] in "XVLCM":
            roman_num -= 1
        if let == 'I':
            roman_num += 1
        if let == 'X':
            roman_num += 10
        if let == 'V':
            roman_num += 5
        if let == 'L':
            roman_num += 50
        if let == 'C':
            roman_num += 100
        if let == 'D':
            roman_num += 500
        if let == 'M':
            roman_num += 1000
        i += 1
    return roman_num
