#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = (number * -1) % 10
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
if last_digit < 6:
    print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
if last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is zero")
