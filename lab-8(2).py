class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root is None:
        return 0
    return root.height


def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)


def right_rotate(y):
    x = y.left
    t = x.right

    x.right = y
    y.left = t

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    t = y.left

    y.left = x
    x.right = t

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and key < root.left.key:
        return right_rotate(root)

    if b < -1 and key > root.right.key:
        return left_rotate(root)

    if b > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def min_value(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = min_value(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    root.height = 1 + max(height(root.left), height(root.right))
    b = balance(root)

    if b > 1 and balance(root.left) >= 0:
        return right_rotate(root)

    if b > 1 and balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if b < -1 and balance(root.right) <= 0:
        return left_rotate(root)

    if b < -1 and balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


root = None

while True:
    print("\n1.Insert  2.Delete  3.Search")
    print("4.Inorder  5.Preorder  6.Postorder  7.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter element: "))
        root = insert(root, key)

    elif choice == 2:
        key = int(input("Enter element to delete: "))
        if search(root, key):
            root = delete(root, key)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice == 3:
        key = int(input("Enter element to search: "))
        print("Element found" if search(root, key)
              else "Element not found")

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
