import math


def theater(m, n, a):
    x = math.ceil(m / a) * math.ceil(n / a)
    return x


x, y, z = list(map(int, input().split(" ")))
print(theater(x, y, z))
