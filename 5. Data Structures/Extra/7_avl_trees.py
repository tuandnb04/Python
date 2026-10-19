# 5. Data Structures - Extra: Cây AVL (AVL Trees - Self-Balancing BST)
# Cấu trúc Cây tìm kiếm nhị phân tự cân bằng qua các phép xoay (Rotations)
#
# 1. Lịch sử & Khái niệm Cây AVL (History & Concept)
# - Được phát minh năm 1962 bởi hai nhà toán học Liên Xô Georgy Adelson-Velsky và Evgenii Landis.
# - Là Cây tìm kiếm nhị phân tự cân bằng (Self-Balancing Binary Search Tree).
# - Điểm khác biệt duy nhất so với BST thông thường là Cây AVL thực hiện thêm các phép xoay (Rotations)
#   để duy trì chiều cao cây luôn ở mức tối thiểu h = O(log n).
# - Nhờ duy trì cân bằng, các thao tác Tìm kiếm (Search), Thêm (Insert), và Xóa (Delete)
#   đều được đảm bảo đạt độ phức tạp O(log n) trong mọi trường hợp (kể cả worst-case).

# 2. Hệ số cân bằng (The Balance Factor - BF)
# - Chiều cao của một node là số cạnh trên đường đi dài nhất từ node đó xuống một node lá.
# - Hệ số cân bằng của node X:
#   BF(X) = height(leftSubtree(X)) - height(rightSubtree(X))
# - Ý nghĩa giá trị của Balance Factor:
#   + BF = 0: Node cân bằng hoàn hảo.
#   + BF > 0: Node bị lệch trái (left-heavy).
#   + BF < 0: Node bị lệch phải (right-heavy).
# - Điều kiện cân bằng AVL: BF của mọi node trong cây chỉ được phép nằm trong tập {-1, 0, 1}.
# - Khi BF > 1 hoặc BF < -1, cây bị mất cân bằng và cần thực hiện phép xoay để tái cân bằng.


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


# 3. Các hàm bổ trợ đo chiều cao và tính hệ số cân bằng
def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


# 4. Các phép xoay cơ bản (Left and Right Rotations)
# Mục đích: Đổi node cha của các cây con để giảm chiều cao nhánh bị lệch,
# đồng thời bảo toàn tính chất thứ tự BST (left < root < right) và dãy duyệt In-order.

# 4.1. Phép xoay phải (Right Rotation): Áp dụng khi cây bị lệch trái
def right_rotate(y):
    print("Rotate right on node", y.data)
    x = y.left
    t2 = x.right

    # Thực hiện xoay
    x.right = y
    y.left = t2

    # Cập nhật chiều cao (y trước, x sau)
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x


# 4.2. Phép xoay trái (Left Rotation): Áp dụng khi cây bị lệch phải
def left_rotate(x):
    print("Rotate left on node", x.data)
    y = x.right
    t2 = y.left

    # Thực hiện xoay
    y.left = x
    x.right = t2

    # Cập nhật chiều cao (x trước, y sau)
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y


# 5. Thêm phần tử vào Cây AVL (Insert with Retracing & Rebalancing)
# Quá trình truy vết ngược (Retracing):
# - Sau khi đệ quy chèn node mới ở tầng lá, đệ quy quay lui (backtrack) dần về node gốc.
# - Tại mỗi node tổ tiên, chiều cao được cập nhật và hệ số cân bằng được tính lại.
# - Nếu phát hiện mất cân bằng, xử lý theo 1 trong 4 trường hợp (LL, RR, LR, RL).
def insert(node, data):
    # Bước 1: Thao tác chèn BST tiêu chuẩn
    if not node:
        return AVLNode(data)

    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    else:
        return node  # Không cho phép giá trị trùng lặp

    # Bước 2: Cập nhật chiều cao của node hiện tại
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    # Bước 3: Tính hệ số cân bằng để kiểm tra xem node có bị mất cân bằng không
    balance = get_balance(node)

    # Bước 4: Tái cân bằng nếu mất cân bằng (4 trường hợp)
    # Case 1: Left-Left (LL) - Node cha lệch trái, con trái lệch trái
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    # Case 2: Left-Right (LR) - Node cha lệch trái, con trái lệch phải
    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    # Case 3: Right-Right (RR) - Node cha lệch phải, con phải lệch phải
    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    # Case 4: Right-Left (RL) - Node cha lệch phải, con phải lệch trái
    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


# 6. Tìm giá trị nhỏ nhất trong cây con (minValueNode)
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# 7. Xóa phần tử trong Cây AVL (Delete with Rebalancing)
# Sau khi xóa node theo chuẩn BST, tiến hành quay lui cập nhật chiều cao và tái cân bằng.
def delete(node, data):
    if not node:
        return node

    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Node cần xóa có 0 hoặc 1 con
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # Node cần xóa có 2 con: Lấy in-order successor
        temp = min_value_node(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)

    if node is None:
        return node

    # Cập nhật chiều cao
    node.height = 1 + max(get_height(node.left), get_height(node.right))

    # Kiểm tra cân bằng
    balance = get_balance(node)

    # Tái cân bằng (4 trường hợp)
    if balance > 1 and get_balance(node.left) >= 0:
        return right_rotate(node)

    if balance > 1 and get_balance(node.left) < 0:
        node.left = left_rotate(node.left)
        return right_rotate(node)

    if balance < -1 and get_balance(node.right) <= 0:
        return left_rotate(node)

    if balance < -1 and get_balance(node.right) > 0:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


# 8. Duyệt In-order để kiểm tra tính có thứ tự
def in_order_traversal(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    in_order_traversal(node.left, result)
    result.append(node.data)
    in_order_traversal(node.right, result)
    return result


# 9. Thử nghiệm xây dựng Cây AVL theo dữ liệu mẫu chuẩn
print("Building AVL Tree (Step-by-step simulation):")
root = None
letters = ["C", "B", "E", "A", "D", "H", "G", "F"]

for letter in letters:
    print(f"Insert '{letter}':")
    root = insert(root, letter)

print("\nIn-order Traversal of AVL Tree (Ascending):")
print(in_order_traversal(root))  # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
print("Tree Height at Root:", get_height(root))
print("Balance Factor at Root:", get_balance(root))

# Thử nghiệm xóa node 'E':
print("\nDeleting node 'E' from AVL Tree:")
root = delete(root, "E")
print("In-order Traversal after deleting 'E':")
print(in_order_traversal(root))


# 10. Giải thích toán học về độ phức tạp O(log n)
# - Với một cây nhị phân hoàn hảo chiều cao h:
#   Tổng số node: n = 2^0 + 2^1 + 2^2 + ... + 2^h = 2^(h+1) - 1
# - Ta có:
#   n + 1 = 2^(h+1)
#   log2(n + 1) = h + 1
#   h = log2(n + 1) - 1
#   => Chiều cao h xấp xỉ O(log n)
# - Vì các thao tác Search, Insert, Delete chỉ duyệt dọc theo chiều cao h của cây,
#   thời gian chạy trên Cây AVL luôn được đảm bảo là O(h) = O(log n),
#   nhanh hơn rất nhiều so với BST không cân bằng O(n).
print("\nAVL Tree Time Complexity Summary:")
print("- Search, Insert, Delete: O(log n) guaranteed")
print("- Space Complexity: O(n)")
