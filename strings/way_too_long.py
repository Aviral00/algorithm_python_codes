def way(x):

    m = len(x)-2
    s = str(m)
    if m+2 > 10:
        x = x[0]+s+x[-1]

    return x


x = int(input())
for i in range(x):
    c = input()
    print(way(c))

