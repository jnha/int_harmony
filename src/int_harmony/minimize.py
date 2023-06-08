"""minimization functions

Since division is in general not possible it is convenient to
represent waveforms with the smallest coefficients possible.
The samples should be co-prime, or we can divide by the gcd of
the samples to get a smaller version.
However the gcd is affected by where the waveform is centered.

There are three natural ways to center an integer waveform:
- with the lowest sample at 0 (unsigned).
- with the lowest sample and highest sample an even distance from zero (equal distance).
- with 0 at the average sample value (equal weight).

The unsigned version:
 - the amplitude is as small as possible.
 - no negative values.
 - easy to convert to normalized unsigned output formats.

The even distance version:
 - is easy to convert to normalized signed output formats.
 - amplitude can be twice as large as the unsigned version.

The even weight version:
- stays close to zero when adding samples together.
- one of the values is 0 when it is integrated.
- the amplitude can be up to a factor of the length of the sample bigger.
"""

from math import gcd
from typing import Collection, Sequence


def shift_zero(samples: Collection[int]) -> Sequence[int]:
    """Shift a sequence of integers so the smallest is 0"""
    smallest = min(samples)
    return tuple(sample - smallest for sample in samples)


def center(samples: Collection[int]) -> Sequence[int]:
    """Center a sample around zero."""
    difference = max(samples) - min(samples)
    if difference & 1:
        return tuple(sample - difference // 2 for sample in samples)
    else:
        return tuple(sample * 2 - difference for sample in samples)


def simplify(samples: Collection[int]) -> Sequence[int]:
    """Divide out any common divisors in samples"""
    divisor = gcd(*samples)
    return tuple(sample // divisor for sample in samples)


def minimize(samples: Collection[int]) -> Sequence[int]:
    """Minimize a sample.

    After minimization the minimum sample is 0
    and the greatest common divisor of the samples is 1.
    """
    return simplify(shift_zero(samples))


def mincenter(samples: Collection[int]) -> Sequence[int]:
    """Center a sample around zero with no common divisors"""
    minimal = minimize(samples)
    largest = max(minimal)
    if largest & 1:
        return tuple(sample * 2 - largest for sample in samples)
    return tuple(sample - largest // 2 for sample in samples)


def average_zero(samples: Collection[int]) -> Sequence[int]:
    """Center the samples so that the average is 0"""
    # We want the average
    average = sum(samples)
    # To get the average we should divide by len(samples)
    # but we can't divide by more than the gcd.
    divisor = gcd(average, len(samples))
    average = average // divisor
    remainder = len(samples) // divisor
    # Instead we scale the samples up by the remainder
    # average = sum(samples)//len(samples)
    # = sum(samples)//divisor // (len(samples)//divisor)
    # = sum(samples) // divisor // remainder
    # sum(samples) // divisor = average * remainder
    # = sum(sample * remainder for sample in samples) // len(samples)
    return tuple(sample * remainder - average for sample in samples)
