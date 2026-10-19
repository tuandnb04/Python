# Cây tìm kiếm nhị phân (Binary Search Tree - BST)
# Đặc tính: Con bên trái luôn nhỏ hơn nút cha, con bên phải luôn lớn hơn nút cha

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 1. Chèn phần tử vào BST:
def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root


# 2. Tìm kiếm phần tử trong BST: O(h), cây cân bằng đạt O(log n)
def search(root, target):
    if root is None or root.val == target:
        return root
    if target < root.val:
        return search(root.left, target)
    return search(root.right, target)


# 3. Duyệt trung thứ tự (In-order traversal: Trái -> Gốc -> Phải)
# Kết quả luôn là danh sách tăng dần
def in_order(root):
    res = []
    if root:
        res.extend(in_order(root.left))
        res.append(root.val)
        res.extend(in_order(root.right))
    return res


# 4. Tìm nút có giá trị nhỏ nhất (đi hết về bên trái):
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# 5. Xóa phần tử khỏi BST:
# - Trường hợp 1: Nút lá (0 con) -> xóa trực tiếp
# - Trường hợp 2: Nút có 1 con -> nối nút con vào nút cha
# - Trường hợp 3: Nút có 2 con -> lấy nút nhỏ nhất cây con phải thay thế rồi xóa nút đó
def delete(root, val):
    if root is None:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Nút có 0 hoặc 1 con:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Nút có 2 con:
        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


# Xây dựng BST mẫu bằng hàm insert:
values = [13, 7, 15, 3, 8, 14, 19, 18]
root = None
for v in values:
    root = insert(root, v)

print("In-order traversal (Sorted):", in_order(root))

# Tìm kiếm:
found = search(root, 15)
missing = search(root, 99)
print("Search 15:", "Found" if found else "Not found")
print("Search 99:", "Found" if missing else "Not found")

# Nút nhỏ nhất:
print("Min value in BST:", min_value_node(root).val)

# Xóa nút có 2 con (15):
root = delete(root, 15)
print("After deleting 15:", in_order(root))
