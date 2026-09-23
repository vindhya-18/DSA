class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


def display():
    global head

    temp = head

    if temp is None:
        print("List is empty")
        return

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("None")


def create():
    global head

    head = None
    n = int(input("Enter number of nodes: "))

    for i in range(n):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if head is None:
            head = new_node
        else:
            temp = head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    print("Linked list created")


def insert_beginning():
    global head

    data = int(input("Enter value: "))

    new_node = Node(data)
    new_node.next = head
    head = new_node


def insert_end():
    global head

    data = int(input("Enter value: "))
    new_node = Node(data)

    if head is None:
        head = new_node
        return

    temp = head

    while temp.next:
        temp = temp.next

    temp.next = new_node


def insert_index():
    global head

    data = int(input("Enter value: "))
    index = int(input("Enter index: "))

    new_node = Node(data)

    if index == 0:
        new_node.next = head
        head = new_node
        return

    temp = head

    for i in range(index - 1):
        if temp is None:
            print("Invalid index")
            return
        temp = temp.next

    if temp is None:
        print("Invalid index")
        return

    new_node.next = temp.next
    temp.next = new_node


def delete_value():
    global head

    value = int(input("Enter value to delete: "))

    if head is None:
        print("List is empty")
        return

    if head.data == value:
        head = head.next
        return

    temp = head

    while temp.next and temp.next.data != value:
        temp = temp.next

    if temp.next is None:
        print("Value not found")
    else:
        temp.next = temp.next.next


def delete_first():
    global head

    if head is None:
        print("List is empty")
    else:
        head = head.next


def delete_last():
    global head

    if head is None:
        print("List is empty")
        return

    if head.next is None:
        head = None
        return

    temp = head

    while temp.next.next:
        temp = temp.next

    temp.next = None


def count_nodes():
    global head

    count = 0
    temp = head

    while temp:
        count += 1
        temp = temp.next

    print("Number of nodes:", count)


while True:

    print("\n--- SINGLY LINKED LIST ---")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at index")
    print("5. Delete by value")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Count nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create()

    elif choice == 2:
        insert_beginning()

    elif choice == 3:
        insert_end()

    elif choice == 4:
        insert_index()

    elif choice == 5:
        delete_value()

    elif choice == 6:
        delete_first()

    elif choice == 7:
        delete_last()

    elif choice == 8:
        count_nodes()

    elif choice == 9:
        display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
