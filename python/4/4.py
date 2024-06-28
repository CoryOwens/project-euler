#!/usr/bin/python3

def is_palindrome_number(x):
    x = str(x)
    return x == x[::-1]

def gen_palindrome_numbers():
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if is_palindrome_number(product):
                yield product

if __name__ == '__main__':
    max_palindrome = 0
    for next_palindrome in gen_palindrome_numbers():
        if next_palindrome > max_palindrome:
            max_palindrome = next_palindrome
    print(max_palindrome)
