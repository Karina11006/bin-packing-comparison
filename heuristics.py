from typing import List

def next_fit(weight: List[int], c: int) -> int:
    res = 0
    rem = c
    for i in range(len(weight)):
        if rem >= weight[i]:
            rem -= weight[i]
        else:
            res += 1
            rem = c - weight[i]
    return res


def first_fit(weight: List[int], c: int) -> int:
    n = len(weight)
    res = 0
    bin_rem = [0] * n

    for i in range(n):
        j = 0
        while j < res:
            if bin_rem[j] >= weight[i]:
                bin_rem[j] -= weight[i]
                break
            j += 1

        if j == res:
            bin_rem[res] = c - weight[i]
            res += 1
    return res


def best_fit(weight: List[int], c: int) -> int:
    n = len(weight)
    res = 0
    bin_rem = [0] * n

    for i in range(n):
        min_rem = c + 1
        bi = 0
        for j in range(res):
            if bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min_rem:
                bi = j
                min_rem = bin_rem[j] - weight[i]

        if min_rem == c + 1:
            bin_rem[res] = c - weight[i]
            res += 1
        else:
            bin_rem[bi] -= weight[i]
    return res
