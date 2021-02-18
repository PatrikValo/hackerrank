from typing import List


def distance(a: int, b: int):
    return (a - b) // 2


def flatland_space_stations(n: int, c: List[int]) -> int:
    first: int = 0
    last: int = n - 1
    c.sort()

    maximal = c[0] - first
    for i in range(1, len(c)):
        maximal = max(maximal, distance(c[i], c[i - 1]))

    return max(maximal, last - c[len(c) - 1])


if __name__ == '__main__':
    assert(flatland_space_stations(5, [0, 4]) == 2)
    assert(flatland_space_stations(6, [0, 1, 2, 3, 4, 5, 6]) == 0)
    assert(flatland_space_stations(20, [13, 1, 11, 10, 6]) == 6)
