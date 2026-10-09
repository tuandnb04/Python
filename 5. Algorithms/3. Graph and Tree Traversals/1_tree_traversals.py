# * [BỔ SUNG NÂNG CAO] Tree Traversals (In-order, Pre-order, Post-order)

class TreeNode:
    def __init__(self, val: int):
        self.val: int = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

# In-order (Left -> Root -> Right): Xuất các phần tử theo thứ tự tăng dần trên BST
def inorder(node: TreeNode | None) -> list[int]:
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Pre-order (Root -> Left -> Right): Dùng để sao chép / serialize cấu trúc cây
def preorder(node: TreeNode | None) -> list[int]:
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)

# Post-order (Left -> Right -> Root): Dùng để giải phóng / xóa cây hoặc tính toán biểu thức
def postorder(node: TreeNode | None) -> list[int]:
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]

# Tạo cây mẫu:
#       4
#      / \
#     2   5
#    / \
#   1   3
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print("In-order (Sorted):", inorder(root))        # [1, 2, 3, 4, 5]
print("Pre-order (Root first):", preorder(root))  # [4, 2, 1, 3, 5]
print("Post-order (Root last):", postorder(root)) # [1, 3, 2, 5, 4]
