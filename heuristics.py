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
