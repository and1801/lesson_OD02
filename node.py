class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if  root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 60)
root = insert(root, 45)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Теперь вы можете вызвать inorder_traversal для вывода всех значений
inorder_traversal(root)