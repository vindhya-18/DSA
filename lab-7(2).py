
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    new_node = Node(data)

    if root is None:
        return new_node

    queue = [root]

    while queue:
        temp = queue.pop(0)

        if temp.left is None:
            temp.left = new_node
            return root
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = new_node
            return root
        else:
            queue.append(temp.right)


def search(root, key):
    if root is None:
        return False

    queue = [root]

    while queue:
        temp = queue.pop(0)

        if temp.data == key:
            return True

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return False


def delete(root, key):
    if root is None:
        return None

    if root.left is None and root.right is None:
        if root.data == key:
            return None
        return root

    queue = [root]
    key_node = None
    last_node = None
    parent = None

    while queue:
        last_node = queue.pop(0)

        if last_node.data == key:
            key_node = last_node

        if last_node.left:
            parent = last_node
            queue.append(last_node.left)

        if last_node.right:
            parent = last_node
            queue.append(last_node.right)

    if key_node:
        key_node.data = last_node.data

        if parent.right == last_node:
            parent.right = None
        else:
            parent.left = None

        print("Element deleted")
    else:
        print("Element not found")

    return root


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


root = None

while True:
    print("\n1.Insert  2.Search  3.Delete")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        root = insert(root, data)
        print("Element inserted")

    elif choice == 2:
        key = int(input("Enter element to search: "))
        if search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter element to delete: "))
        root = delete(root, key)

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
