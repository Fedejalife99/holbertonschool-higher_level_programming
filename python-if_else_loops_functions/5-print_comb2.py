#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print(0,end ='')
        print(i,end =', ')
        continue
    if i == 99:
        print(i, end='\n')
        continue
    print(i, end= ', ')
