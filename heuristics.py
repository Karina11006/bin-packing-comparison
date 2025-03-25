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