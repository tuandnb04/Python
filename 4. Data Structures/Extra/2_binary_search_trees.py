# Custom Binary Search Tree - BST (Cây tìm kiếm nhị phân tự cài đặt bằng Node)
# - Quy tắc BST:
#    - Mọi node ở cây con bên trái (left subtree) có giá trị < node gốc
#    - Mọi node ở cây con bên phải (right subtree) có giá trị > node gốc
# - Ứng dụng: Thao tác tìm kiếm, chèn, xóa trung bình O(log n)

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = BSTNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = BSTNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = BSTNode(val)
            else:
                self._insert(node.right, val)

    def search(self, val):
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

bst = BinarySearchTree()
for num in [50, 30, 70, 20, 40]:
    bst.insert(num)

print("BST search 30:", bst.search(30)) # True
print("BST search 99:", bst.search(99)) # False
