class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

value = int(input("Enter value to delete: "))

if head is None:
    print("List is empty")
elif head.data == value:
    head = head.next
else:
    temp = head

    while temp.next and temp.next.data != value:
        temp = temp.next

    if temp.next is None:
        print("Value not found")
    else:
        temp.next = temp.next.next

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
