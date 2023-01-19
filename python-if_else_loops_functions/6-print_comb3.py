#!/usr/bin/python3
for i in range(10):
  for j in range(i + 1, 10):
    if i == 8 and j == 9:
      print(i,end= '')
      print(j)
      continue
    print(i, end='')
    print(j, end = ', ')
