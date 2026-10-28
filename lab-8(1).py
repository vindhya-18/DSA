class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root


def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def find_min(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


root = None

while True:
    print("\n1.Insert  2.Search  3.Delete")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        root = insert(root, data)

    elif choice == 2:
        key = int(input("Enter element to search: "))
        if search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter element to delete: "))
        if search(root, key):
            root = delete(root, key)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice == 4:
        print("Inorder:", end=" ")
        inorder(root)
        print()

    elif choice == 5:
        print("Preorder:", end=" ")
        preorder(root)
        print()

    elif choice == 6:
        print("Postorder:", end=" ")
        postorder(root)
        print()

    elif choice == 7:
        break

    else:
        print("Invalid choice")
