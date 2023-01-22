#!/usr/bin/python3
import sys


def main():
    result = 0
    num_args = len(sys.argv)
    for i in range(1, num_args):
        result = result + int(sys.argv[i])
    print(result)


if __name__ == "__main__":
    main()
