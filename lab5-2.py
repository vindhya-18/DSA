stack = [10, 20, 30, None, None]
top = 2

if top == -1:
    print("Stack Underflow")
else:
    value = stack[top]
    stack[top] = None
    top = top - 1

    print("Popped element:", value)

print("Stack:", stack[:top + 1])
