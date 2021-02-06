from typing import List


def count_array(n: int, k: int, x: int) -> int:
    # https://www.hackerrank.com/challenges/construct-the-array/problem
    rows = k
    cols = n

    table: List[List[int]] = [[0 for _ in range(cols)] for _ in range(rows)]
    table[0][0] = 1

    for j in range(1, cols):
        for i in range(rows):
            for num in range(rows):
                if num != i:
                    table[i][j] += table[num][j - 1]
    return table[x - 1][n - 1] % 1000000007


if __name__ == '__main__':
    assert(count_array(4, 3, 2) == 3)
    assert(count_array(3, 5, 2) == 3)
    assert(count_array(1, 5, 2) == 0)
    assert(count_array(2, 5, 2) == 1)
    assert(count_array(5, 3, 1) == 6)
    assert(count_array(761, 99, 1) == 236568308)
    # assert(count_array(17048, 14319, 1) == 803254122)
