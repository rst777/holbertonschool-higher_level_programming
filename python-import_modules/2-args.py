#!/usr/bin/python3
import sys

if __name__ == "__main__":
    nombre_args = len(sys.argv) - 1

    if nombre_args == 0:
        print("0 arguments.")
    elif nombre_args == 1:
        print("1 argument:")
    else:
        print(f"{nombre_args} arguments:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
