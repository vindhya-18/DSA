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

if head is None:
    print("List is empty")

elif head.next is None:
    head = None

else:
    temp = head

    while temp.next.next:
        temp = temp.next

    temp.next = None

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
