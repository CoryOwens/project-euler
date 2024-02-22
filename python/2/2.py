#!/usr/bin/python3


def fibonacci(n):
    yield 1
    yield 2
    first = 1
    second = 2
    for _ in range(n):
        x = first + second
        first = second
        second = x
        yield x


if __name__ == '__main__':
    fib = fibonacci(4_000_000)
    print(fib)
    sum = 0
    x = 0
    while x < 4_000_000:
        x = next(fib)
        if not x % 2:
            sum += x
    print(f'Total: {sum}')
    pass
