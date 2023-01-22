#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    if num_args != 0 and num_args != 1:
        print(f"{num_args} arguments:")
    if num_args == 1:
        print(f"{num_args} argument:")
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i - 1]))
