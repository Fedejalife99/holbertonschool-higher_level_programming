#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    di = div(a, b)
    mu = mul(a, b)
    ad = add(a, b)
    su = sub(a, b)
    print("{} + {} = {}".format(a, b , add(a, b)))
    print("{} - {} = {}".format(a, b , sub(a, b)))
    print("{} * {} = {}".format(a, b , sub(a, b)))
    print("{} / {} = {}".format(a, b , div(a, b)))
