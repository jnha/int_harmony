"""
Functions for infinite iterables with a repeating pattern (cyclic iterables).
"""
from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from itertools import cycle, islice
from math import lcm, prod
from typing import TypeVar

S = TypeVar("S")  # input sequence value type
T = TypeVar("T")  # output sequence value type

# I considered making Cyclic iterables their own class
# implimenting the sequence protocol, but infinite
# sequences play really badly with a lot of operations.
# x in cyclic, list(cyclic), and basically anything else
# risks ending up being an infinite loop.
#
# I think using forcing the caller to explicitly use itertools.cycle
# is a lot clearer in avoiding footguns.


def get_cycle(iterable: Iterable[T], period: int) -> Sequence[T]:
    """Gets a cycle with a specified period from an iterable"""
    return tuple(islice(iterable, period))


def reduce_cycles(
    reduction: Callable[[Sequence[S]], T], cycles: tuple[Sequence[S], ...]
) -> Sequence[T]:
    """Calculate the pointwise reduction of the cycles"""
    return tuple(
        islice(
            (
                reduction(values)
                for values in zip(*(cycle(cyclic) for cyclic in cycles))
            ),
            lcm(*(len(cyclic) for cyclic in cycles)),
        )
    )


def add_cycles(*cycles: Sequence[int]) -> Sequence[int]:
    """Calculate the pointwise sum of the cycles"""
    return reduce_cycles(sum, cycles)


def mul_cycles(*cycles: Sequence[int]) -> Sequence[int]:
    """Calculate the pointwise product of the cycles"""
    return reduce_cycles(prod, cycles)
