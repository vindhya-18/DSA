class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


top = None

value = int(input("Enter value to push: "))

new_node = Node(value)

new_node.next = top
top = new_node

print("Element pushed successfully")

temp = top

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")
