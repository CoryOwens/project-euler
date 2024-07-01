#!/usr/bin/python3
from math import prod

def sum_diff(x):
    # Find the difference between the sum of the squares from 1 to x (inclusive)
    running_sum = 0
    running_sum_of_squares = 0
    for i in range(x+1):
        running_sum += i
        running_sum_of_squares += i**2
    return running_sum**2 - running_sum_of_squares

if __name__ == '__main__':
    answer = sum_diff(100)
    print(answer)
