stack = []
sp = -1


def push(val):

    stack.append(val)


def pop():
    return(stack.pop())


push(5)
push(7)
push(9)
pop()
print(stack)
