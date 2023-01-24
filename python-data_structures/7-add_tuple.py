#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    frst_elem = 0
    sec_elem = 0
    if len(tuple_b) >= 2 and len(tuple_a) == 1:
        frst_elem += tuple_b[0]
        sec_elem += 0
    if len(tuple_a) >= 2 and len(tuple_b) == 1:
        frst_elem += tuple_a[0] + tuple_b[0]
        sec_elem += tuple_a[1]
    elif len(tuple_a) >= 2 and len(tuple_b) >= 2:
        frst_elem += tuple_a[0] + tuple_b[0]
        sec_elem += tuple_a[1] + tuple_b[1]
    elif len(tuple_a) < 2 and len(tuple_b) >= 2:
        frst_elem += tuple_b[0]
        sec_elem += tuple_b[1]
    elif len(tuple_a) >= 2 and len(tuple_b) < 2:
        frst_elem += tuple_a[0]
        sec_elem += tuple_a[1]
    else:
        frst_elem += 0
        sec_elem += 0
    return (frst_elem, sec_elem)
