#!/usr/bin/python3

def sum_of_multiples(mult_list, lim):
    sum = 0
    for i in range(lim):
        for mult in mult_list:
            if not (i % mult):
                sum += i
                print(f'{i} divisible by {mult}')
                break
    return sum

if __name__ == '__main__':
    sum = sum_of_multiples([3, 5], 1000)
    print(sum)
