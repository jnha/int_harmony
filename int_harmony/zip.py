"""
What's the fastest way to zip two cyclic sequences?
"""


from itertools import cycle, islice
from math import gcd, lcm


def cycle2(a):
    while True:
        yield from a


def cycle3(a, n):
    for i in range(n):
        yield from a


def cycle_zip(a, b):
    return islice(zip(cycle(a), cycle(b)), lcm(len(a), len(b)))


def cycle2_zip(a, b):
    return islice(zip(cycle2(a), cycle2(b)))


def cycle3_zip(a, b):
    d = gcd(len(a), len(b))
    return zip(cycle3(a, len(a) // d), cycle3(b, len(b) // d))


def cycle4_zip(a, b):
    d = gcd(len(a), len(b))
    return zip(a * (len(a) // d), b * (len(b) // d))
