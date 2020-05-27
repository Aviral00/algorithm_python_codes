def insertion_sort(x):

    for i in range(1, len(x)):
        key = x[i]
        for j in range(i-1, -1, -1):
            if key < x[j]:
                x[j+1] = x[j]
                x[j] = key

            else:
                break

    return x


arr = [65, 12, 15, 30, 20, 50, 45]
print(insertion_sort(arr))




