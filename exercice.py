#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def square_root(number: int) -> float:
#fsbbgfx
    return number**0.5


def square(number: int) -> int:

    return math.pow(number,2)


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()


c = 0
for i in range(10, 100, 5):
    while i<100:
        c += i
        i += 1
        print(i)
        print("fintitigirnfhsuytgjhv")


c = 0
for i in range(10, 100, 5):
    c += i
    i += 1
    while i<100:
        print(i)