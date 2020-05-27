def bubble_sort(x):

    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            bubble_sort(x)

    return x


x = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(x))


