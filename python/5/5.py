#!/usr/bin/python3
from math import prod

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
    prime_factor_count = {}
    for i in range(2, 21):
        factors = factorize(i)
        factor_count = {x: factors.count(x) for x in factors}
        for k, v in factor_count.items():
            if k not in prime_factor_count or v > prime_factor_count[k]:
                prime_factor_count[k] = v
    product = prod([k**v for k, v in prime_factor_count.items()])
    print(product)
