stack = [None] * 5
top = -1

value = int(input("Enter value to push: "))

if top == 4:
    print("Stack Overflow")
else:
    top = top + 1
    stack[top] = value
    print("Element pushed successfully")

print("Stack:", stack[:top + 1])
