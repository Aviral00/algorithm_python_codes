def boxes(x):

    removed = 0

    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            removed = removed + (x[i+1] - x[i])
            x[i+1] = x[i]

    return removed


arr = [5, 6, 7, 1]
print(boxes(arr))