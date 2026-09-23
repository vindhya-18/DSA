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

data = int(input("Enter value: "))
index = int(input("Enter index: "))

new_node = Node(data)

if index == 0:
    new_node.next = head
    head = new_node
else:
    temp = head

    for i in range(index - 1):
        if temp is None:
            break
        temp = temp.next

    if temp is None:
        print("Invalid index")
    else:
        new_node.next = temp.next
        temp.next = new_node

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
