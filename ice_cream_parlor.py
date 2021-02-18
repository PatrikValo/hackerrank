from typing import List, Dict


def ice_cream_parlor(m: int, arr: List[int]) -> List[int]:
    dictionary: Dict[int, int] = {}

    for i, elem in enumerate(arr):
        prev = dictionary.get(elem)
        if prev is None:
            dictionary[m - elem] = i
        else:
            return [prev + 1, i + 1]
    return []


if __name__ == '__main__':
    assert(ice_cream_parlor(4, [1, 4, 5, 3, 2]) == [1, 4])
    assert(ice_cream_parlor(4, [2, 2, 4, 3]) == [1, 2])
