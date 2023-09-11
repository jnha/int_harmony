"""

"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable
from itertools import islice


def windowed_sum(window_size: int, samples: Iterable[int]):
    """Take a moving average of the samples"""
    samples = iter(samples)
    window = deque(islice(samples, None, window_size), maxlen=window_size)
    value = sum(window)
    yield value
    for sample in samples:
        value = value - window.popleft() + sample
        window.append(sample)
        yield value
