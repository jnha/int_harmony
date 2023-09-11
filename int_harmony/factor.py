"""Factor periodic signals"""


def factor(period: tuple[int]) -> list[tuple[int]]:
    if not period:
        return []
    return [period]