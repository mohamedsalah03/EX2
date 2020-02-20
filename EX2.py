# -*- coding: utf-8 -*-
import random

START = 1
END   = 50
LIMIT = 11


def randomness():
    number = [random.randint(START, END) for _ in range(1, LIMIT)]
    number.sort()
    return number
if __name__ == '__main__':
    print(randomness())



# To test the output of the function we should verify the length of number(=10) and that number is
    # well sorted

#10 minutes