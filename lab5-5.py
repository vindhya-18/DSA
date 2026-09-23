class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = Node(30)
top.next = Node(20)
top.next.next = Node(10)

if top is None:
    print("Stack Underflow")
else:
    value = top.data
    top = top.next

    print("Popped element:", value)

temp = top

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
