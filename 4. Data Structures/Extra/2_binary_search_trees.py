# TREE & BINARY SEARCH TREE (CÂY & CÂY TÌM KIẾM NHỊ PHÂN)
#
# 1. CÁC KHÁI NIỆM & THUẬT NGỮ CƠ BẢN VỀ CÂY (TREE TERMINOLOGY):
# - Định nghĩa: Cây là một đồ thị đặc biệt: liên thông (connected) và KHÔNG có chu trình (acyclic / no loops).
# - Root (Gốc): Node trên cùng, không có cha. Điểm bắt đầu để truy cập và duyệt cây.
# - Parent / Child / Sibling: Node cha / Node con / Node anh em (cùng cha).
# - Leaf (Lá): Node ở cuối cành, không có con (bậc = 0).
# - Subtree (Cây con): Một nhánh của cây tự bản thân nó cũng tạo thành một cây độc lập.
# - Depth (Độ sâu của node): Khoảng cách (số cạnh) từ Root đến node đó.
# - Height (Chiều cao của node): Đường đi dài nhất từ node đó xuống node lá.
#   -> Chiều cao của cây = Chiều cao của node Root.
# - Degree (Bậc của node): Số node con của node đó.
#
# 2. CÂY NHỊ PHÂN & CÂY TÌM KIẾM NHỊ PHÂN (BST):
# - Binary Tree: Mỗi node có TỐI ĐA 2 con (trái và phải).
# - Binary Search Tree (BST):
#    - Mọi node ở cây con bên trái (left subtree) có giá trị < node gốc
#    - Mọi node ở cây con bên phải (right subtree) có giá trị > node gốc
#    - Cả 2 cây con trái và phải cũng phải là cây BST
# - Balanced Tree (Cây cân bằng - AVL, Red-Black Tree):
#    - Đảm bảo độ cao 2 cây con cân đối, giúp tìm kiếm/chèn/xóa đạt O(log n),
#      tránh trường hợp cây bị lệch (thoái hóa) thành danh sách liên kết O(n).


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
