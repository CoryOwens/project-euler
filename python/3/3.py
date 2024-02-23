#!/usr/bin/python3

def factorize(x):
    primes = []
    multiples = {}
    for n in range(2, x):
        if not multiples.get(n):
            # Has not been marked as a multiple of a lower prime.
            # Thus, prime.
            primes.append(n)
            print(f'Prime: {n}')
            mult = n
            while mult < x:
                multiples[mult] = True
                print(f'Mult: {mult}')
                mult = mult + n

if __name__ == '__main__':
    factors = factorize(600_851_475_143)
    print(factors)

