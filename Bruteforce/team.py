def team(a, b, c):

    if a + b + c >= 2:
        return 1

    return 0


x = int(input())
d = 0
for i in range(x):
    a, b, c = list(map(int, input().split(" ")))
    d = d + team(a, b, c)
print(d)
