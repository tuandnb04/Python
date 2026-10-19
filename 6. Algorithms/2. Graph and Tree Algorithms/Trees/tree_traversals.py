from collections import deque

# 6. Algorithms - Duyệt Cây nhị phân (Binary Tree Traversals)
# Các phương pháp duyệt cây cơ bản và nâng cao: BFS (Level-order) và DFS (Pre-order, In-order, Post-order)
#
# 1. Khái niệm về duyệt cây (Tree Traversal)
# - Duyệt cây là quá trình ghé thăm (visit) từng node trong cây đúng một lần.
# - Do cây là cấu trúc phi tuyến tính (rẽ nhánh), có hai nhóm chiến lược duyệt chính:
#   1. BFS (Breadth-First Search - Theo chiều rộng): Duyệt hết các node trên cùng một tầng trước khi xuống tầng kế tiếp.
#   2. DFS (Depth-First Search - Theo chiều sâu): Đi sâu theo từng nhánh đến tận cùng các node lá trước khi quay lui.


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 2. Duyệt theo chiều rộng: BFS (Level-Order Traversal)
# - Sử dụng Hàng đợi (Queue) để duyệt theo thứ tự từ trên xuống dưới, từ trái sang phải.
# - Độ phức tạp thời gian: O(n) vì mỗi node được đưa vào và lấy ra khỏi hàng đợi đúng một lần.
# - Độ phức tạp không gian: O(w) với w là chiều rộng lớn nhất của cây.
def bfs_level_order(root_node):
    if not root_node:
        return []
    queue = deque([root_node])
    result = []
    while queue:
        curr = queue.popleft()
        result.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return result


# 3. Duyệt theo chiều sâu: DFS Pre-order (Tiền thứ tự: Gốc -> Trái -> Phải)
# - Quy trình: Thăm node gốc hiện tại -> Đệ quy duyệt cây con trái -> Đệ quy duyệt cây con phải.
# - Đặc điểm: Node hiện tại luôn được xử lý TRƯỚC (Pre) khi đệ quy sang các cây con.
# - Ứng dụng: Sao chép cây, tuần tự hóa (serialize) cây, tạo ký pháp tiền tố (prefix).
def dfs_preorder(node):
    if not node:
        return []
    return [node.val] + dfs_preorder(node.left) + dfs_preorder(node.right)


# 4. Duyệt theo chiều sâu: DFS In-order (Trung thứ tự: Trái -> Gốc -> Phải)
# - Quy trình: Đệ quy duyệt cây con trái -> Thăm node gốc hiện tại -> Đệ quy duyệt cây con phải.
# - Đặc điểm: Node hiện tại được xử lý Ở GIỮA (In) sau khi xong nhánh trái và trước khi sang nhánh phải.
# - Ứng dụng: Trên BST, phép duyệt In-order luôn trả về dãy giá trị TĂNG DẦN (Ascending).
def dfs_inorder(node):
    if not node:
        return []
    return dfs_inorder(node.left) + [node.val] + dfs_inorder(node.right)


# 5. Duyệt theo chiều sâu: DFS Post-order (Hậu thứ tự: Trái -> Phải -> Gốc)
# - Quy trình: Đệ quy duyệt cây con trái -> Đệ quy duyệt cây con phải -> Thăm node gốc hiện tại.
# - Đặc điểm: Node hiện tại được xử lý SAU CÙNG (Post) khi cả hai nhánh con trái và phải đã duyệt xong.
# - Ứng dụng: Giải phóng / xóa cây an toàn từ dưới lên, tính dung lượng thư mục, ký pháp hậu tố (postfix / RPN).
def dfs_postorder(node):
    if not node:
        return []
    return dfs_postorder(node.left) + dfs_postorder(node.right) + [node.val]


# 6. Thử nghiệm với cây mẫu chuẩn
# Cấu trúc cây:
#         R
#       /   \
#      A     B
#     / \   / \
#    C   D E   F
#             /
#            G
root = TreeNode("R")
root.left = TreeNode("A")
root.right = TreeNode("B")
root.left.left = TreeNode("C")
root.left.right = TreeNode("D")
root.right.left = TreeNode("E")
root.right.right = TreeNode("F")
root.right.right.left = TreeNode("G")

print("Binary Tree Traversal Results:")
print("1. BFS Level-order: ", bfs_level_order(root))
print("2. DFS Pre-order:   ", dfs_preorder(root))
print("3. DFS In-order:    ", dfs_inorder(root))
print("4. DFS Post-order:  ", dfs_postorder(root))

# 7. Thử nghiệm với Cây tìm kiếm nhị phân (BST)
#       4
#      / \
#     2   5
#    / \
#   1   3
bst_root = TreeNode(4)
bst_root.left = TreeNode(2)
bst_root.right = TreeNode(5)
bst_root.left.left = TreeNode(1)
bst_root.left.right = TreeNode(3)

print("\nBST In-order Traversal (Sorted ascending):", dfs_inorder(bst_root))  # [1, 2, 3, 4, 5]
