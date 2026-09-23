stack = [None] * 5
top = -1

while True:

    print("\n--- STACK USING ARRAY ---")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        if top == 4:
            print("Stack Overflow")
        else:
            value = int(input("Enter value: "))
            top = top + 1
            stack[top] = value
            print("Element pushed")

    elif choice == 2:

        if top == -1:
            print("Stack Underflow")
        else:
            value = stack[top]
            stack[top] = None
            top = top - 1
            print("Popped element:", value)

    elif choice == 3:

        if top == -1:
            print("Stack is empty")
        else:
            print("Stack:", stack[:top + 1])

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
