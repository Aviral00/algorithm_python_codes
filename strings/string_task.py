def task(x):

    a = []
    b = 0
    m = x.lower()
    b = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
    n = m.translate({ord(i): None for i in b})
    for i in range(len(n)):
        a.append('.' + n[i])
    b = ''.join(a)
    return b


x = input()
print(task(x))

