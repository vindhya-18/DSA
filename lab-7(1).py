
tree = []

def insert():
    value = int(input("Enter element: "))
    tree.append(value)
    print("Element inserted")

def delete():
    value = int(input("Enter element to delete: "))
    if value in tree:
        index = tree.index(value)
        tree.pop(index)
        print("Element deleted")
    else:
        print("Element not found")

def search():
    value = int(input("Enter element to search: "))
    if value in tree:
        print("Element found at index", tree.index(value))
    else:
        print("Element not found")

def display():
    print("Binary Tree Array:", tree)

def inorder(i):
    if i < len(tree):
        inorder(2 * i + 1)
        print(tree[i], end=" ")
        inorder(2 * i + 2)

def preorder(i):
    if i < len(tree):
        print(tree[i], end=" ")
        preorder(2 * i + 1)
        preorder(2 * i + 2)

def postorder(i):
    if i < len(tree):
        postorder(2 * i + 1)
        postorder(2 * i + 2)
        print(tree[i], end=" ")

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Display  5.Inorder  6.Preorder")
    print("7.Postorder  8.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        insert()
    elif choice == 2:
        delete()
    elif choice == 3:
        search()
    elif choice == 4:
        display()
    elif choice == 5:
        inorder(0)
        print()
    elif choice == 6:
        preorder(0)
        print()
    elif choice == 7:
        postorder(0)
        print()
    elif choice == 8:
        break
    else:
        print("Invalid choice")
