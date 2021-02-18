def len_for_pair(a: int, b: int, s: str) -> int:
    fst_count = 0
    snd_count = 0
    curr_size = 0
    for char in s:
        if char == a:
            fst_count += 1
            snd_count = 0
            curr_size += 1
        if char == b:
            snd_count += 1
            fst_count = 0
            curr_size += 1
        if fst_count > 1 or snd_count > 1:
            return 0
    return curr_size


def alternate(s: str) -> int:
    unique = list(set(s))
    maximal = 0
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            maximal = max(maximal, len_for_pair(unique[i], unique[j], s))
    return maximal


if __name__ == '__main__':
    print(alternate("beabeefeab"))
