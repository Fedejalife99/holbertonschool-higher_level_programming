#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
    if num_args != 0:
        print(f"{num_args} arguments:")
        for i in range (1, num_args + 1):
            print("{}: {}".format(i, argv[i - 1]))
