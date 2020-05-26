def selection_sort(x):

    minimum = 0
    for i in range(len(x)-1):
        minimum = i
        for j in range(i+1, len(x)):
            if x[j] < x[minimum]:
                minimum = j
        temp = x[i]
        x[i] = x[minimum]
        x[minimum] = temp
    return x


n = [61, 21, 14, 20, 50, 40, 35]
print(selection_sort(n))