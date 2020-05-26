def bubble_sort(x):

    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

    return x


n = [64, 20, 10, 35, 40, 50]
print(bubble_sort(n))
