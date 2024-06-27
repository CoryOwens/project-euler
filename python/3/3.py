#!/usr/bin/python3

def factorize(x):
    prime_factors = []

    while x % 2 == 0:
        prime_factors.append(2)
        x = x // 2

    for i in range(3, int(x**0.5) + 1, 2):
        while x % i == 0:
            prime_factors.append(i)
            x = x // i

    if x > 2:
        prime_factors.append(x)

    return prime_factors

if __name__ == '__main__':
    factors = factorize(600_851_475_143)
    print(factors)
