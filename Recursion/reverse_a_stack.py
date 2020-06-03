def is_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.push(item)


def pop(stack):
    if is_empty(stack):
        print("Stack Underflow")
        return -1

    return stack.pop()


def create_stack(stack):
    return stack


def insert_at_bottom(stack, value):

    if is_empty(stack):
        push(stack, value)

    else:
        temp = pop(stack)
        insert_at_bottom(stack, value)
        push(stack, temp)


def reverse_stack(stack):

    if not is_empty(stack):
        temp = pop(stack)
        reverse_stack(stack)
        insert_at_bottom(stack, temp)


def prints(stack):
    for i in range(len(stack)-1, -1, -1):
        print(stack[i], end = ' ')
    print()


stack = type('stack', (list,), {'push':list.append})()
stack = create_stack(stack)
push(stack, 4)
push(stack, 3)
push(stack, 2)
push(stack, 1)
print("Original Stack ")
print(stack)

reverse_stack(stack)

print("Reversed Stack ")
print(stack)

