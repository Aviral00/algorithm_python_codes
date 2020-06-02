def activity(x, y):

    a = list(zip(x, y))
    m = sorted(a, key=lambda a : a[1])
    b = [0]
    i = 0

    for j in range(1, len(m)):

        if m[j][0] >= m[i][1]:
            b.append(j)
            i = j

    return b


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]

print(activity(s, f))
