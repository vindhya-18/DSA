class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None


def push():
    global top

    value = int(input("Enter value: "))

    new_node = Node(value)

    new_node.next = top
    top = new_node

    print("Element pushed")


def pop():
    global top

    if top is None:
        print("Stack Underflow")
    else:
        value = top.data
        top = top.next

        print("Popped element:", value)


def display():

    if top is None:
        print("Stack is empty")
        return

    temp = top

    print("Stack:")

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


while True:

    print("\n--- STACK USING LINKED LIST ---")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    print("4. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
