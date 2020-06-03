def reverse_of_string(x):

    if len(x) == 0:
        return

    else:
        temp = x[0]
        reverse_of_string(x[1:])
        print(temp, end='')


x = "Geeks for geeks"
reverse_of_string(x)