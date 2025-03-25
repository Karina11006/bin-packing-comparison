def nextfit(weight, c):
    res = 0
    rem = c
    for i in range(len(weight)):
        if rem >= weight[i]:
            rem = rem - weight[i]
        else:
            res += 1
            rem = c - weight[i]
    return res


def first_fit(weight, c):
    n = len(weight)
    res = 0
    bin_rem = [0] * n

    for i in range(n):
        j = 0
        while (j < res):
            if (bin_rem[j] >= weight[i]):
                bin_rem[j] = bin_rem[j] - weight[i]
                break
            j += 1

        if (j == res):
            bin_rem[res] = c - weight[i]
            res = res + 1
    return res


def best_fit(weight, c):
    n = len(weight)
    res = 0
    bin_rem = [0] * n

    for i in range(n):
        min = c + 1
        bi = 0
        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] - weight[i] < min):
                bi = j
                min = bin_rem[j] - weight[i]

        if (min == c + 1):
            bin_rem[res] = c - weight[i]
            res += 1
        else:
            bin_rem[bi] -= weight[i]
    return res
