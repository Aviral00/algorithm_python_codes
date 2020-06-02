def fractional_knapsack(x, y, z):

    w = []
    for i in range(len(x)):
        w.append(x[i]/y[i])

    a = list(zip(x, y, w))
    m = sorted(a, key=lambda a:a[2], reverse=True)
    n = z
    i = 0
    value = 0
    while n > 0 and i < len(m):
        if n >= m[i][1]:
            value += m[i][1]*m[i][2]
            n -= m[i][1]
        else:
            value += n*m[i][2]
            n -= n
        i += 1
    return value


wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
cap = 50
print(fractional_knapsack(val, wt, cap))
