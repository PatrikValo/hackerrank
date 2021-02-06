def count_array(n: int, k: int, x: int) -> int:
    # https://www.hackerrank.com/challenges/construct-the-array/problem
    fst: int = 1
    snd: int = 0

    for j in range(1, n):
        fst_2: int = ((k - 1) * snd) % 1000000007
        snd: int = ((k - 2) * snd + fst) % 1000000007
        fst: int = fst_2

    return snd if x > 1 else fst


if __name__ == '__main__':
    assert(count_array(4, 3, 2) == 3)
    assert(count_array(3, 5, 2) == 3)
    assert(count_array(1, 5, 2) == 0)
    assert(count_array(2, 5, 2) == 1)
    assert(count_array(5, 3, 1) == 6)
    assert(count_array(761, 99, 1) == 236568308)
    assert(count_array(17048, 14319, 1) == 803254122)
    assert(count_array(942, 77, 13) == 804842436)
