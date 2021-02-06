from typing import List


def fibonacci_modified(t1: int, t2: int, n: int) -> int:
    """
    https://www.hackerrank.com/challenges/fibonacci-modified/problem
    """
    table: List[int] = [0] * n
    table[0] = t1
    table[1] = t2

    for i in range(2, n):
        table[i] = table[i - 2] + (table[i - 1] * table[i - 1])

    return table[n - 1]


if __name__ == '__main__':
    assert(fibonacci_modified(0, 1, 6) == 27)
    assert(fibonacci_modified(0, 1, 5) == 5)
    assert(fibonacci_modified(0, 1, 10) == 84266613096281243382112)
