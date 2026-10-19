from collections import deque

# 5. Data Structures - Extra: Cây & Cây tìm kiếm nhị phân (Trees & BST)
# Toàn diện kiến thức về Cây, Cây nhị phân, Cây tìm kiếm nhị phân (BST) và cân bằng AVL
#
# 1. Khái niệm về Cây và Tính phân cấp (Hierarchical Data Structure)
# - Các cấu trúc tuyến tính (Linear): Arrays, Linked Lists, Stacks, Queues
#   Mỗi phần tử chỉ có duy nhất một phần tử kế tiếp theo một chuỗi thẳng tuần tự.
# - Cây (Tree): Cấu trúc dữ liệu phi tuyến tính (Non-linear) có tính phân cấp (Hierarchical).
#   Mỗi phần tử có thể có nhiều phần tử con, cho phép rẽ nhánh theo nhiều hướng.
# - Ứng dụng thực tế của Cây:
#   + Hệ thống tệp tin (File System: thư mục gốc -> thư mục con -> tệp).
#   + Cơ sở dữ liệu: Cây B-Tree / B+ Tree giúp truy vấn dữ liệu tốc độ cao.
#   + Bảng định tuyến mạng (Routing Tables) trong giao thức mạng.
#   + Hàng đợi ưu tiên (Priority Queues): Cài đặt bằng Binary Heap (module heapq).
#   + Tìm kiếm & sắp xếp: Binary Search Tree (BST), AVL Tree.

# 2. Thuật ngữ cơ bản về Cây (Tree Terminology)
# - Root (Gốc): Node cao nhất của cây, không có node cha (parent).
# - Edge (Cạnh): Đường nối giữa node cha và node con.
# - Parent / Child / Sibling: Node cha / Node con / Node anh em (cùng cha).
# - Leaf (Lá): Node không có con (bậc = 0), nằm ở tận cùng các nhánh.
# - Subtree (Cây con): Một nhánh bắt đầu từ một node con, bản thân nó cũng là một cây độc lập.
# - Depth (Độ sâu của node): Số lượng cạnh từ Root đến node đó.
# - Height (Chiều cao của node): Độ dài đường đi dài nhất từ node đó xuống node lá.
#   Chiều cao của cây chính là chiều cao của Root.
# - Degree (Bậc của node): Số lượng node con của node đó.

# 3. So sánh Trees vs Arrays và Linked Lists
# - Mảng (Array):
#   + Ưu điểm: Truy cập trực tiếp cực nhanh O(1) theo chỉ số (ví dụ: phần tử 700 / 1000).
#   + Nhược điểm: Chèn và Xóa rất chậm O(n) vì phải dịch chuyển ô nhớ (memory shifting).
# - Danh sách liên kết (Linked List):
#   + Ưu điểm: Chèn và Xóa nhanh O(1) tại vị trí con trỏ, không cần dịch chuyển ô nhớ.
#   + Nhược điểm: Truy cập phần tử bất kỳ rất chậm O(n) vì phải duyệt tuần tự từ đầu (traversal).
# - Cây (Trees - Binary Search Tree / AVL Tree):
#   + Giải quyết được cả 2 nhược điểm: VỪA truy cập/tìm kiếm nhanh O(log n),
#     VỪA chèn và xóa nhanh O(log n) mà không cần phải dịch chuyển toàn bộ bộ nhớ!


# 4. Cây tổng quát (General Tree) - Minh họa Hệ thống tệp tin
class GeneralTreeNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        indent = "  " * level
        icon = "[File]" if self.is_file else "[Dir]"
        lines = [f"{indent}{icon} {self.name}"]
        for child in self.children:
            lines.append(child.display(level + 1))
        return "\n".join(lines)


# Xây dựng hệ thống tệp tin mẫu:
fs_root = GeneralTreeNode("/")
bin_dir = GeneralTreeNode("bin")
bin_dir.add_child(GeneralTreeNode("python.exe", is_file=True))

home_dir = GeneralTreeNode("home")
alice_dir = GeneralTreeNode("alice")
alice_dir.add_child(GeneralTreeNode("notes.txt", is_file=True))
bob_dir = GeneralTreeNode("bob")

home_dir.add_child(alice_dir)
home_dir.add_child(bob_dir)

fs_root.add_child(bin_dir)
fs_root.add_child(home_dir)

print("Hierarchical File System (General Tree):")
print(fs_root.display())


# 5. Cây nhị phân (Binary Tree) & Cài đặt cây mẫu tiêu chuẩn
# Khái niệm Cây nhị phân:
# - Là cây mà mỗi node có TỐI ĐA 2 node con: con trái (left child) và con phải (right child).
# Lợi ích lớn của việc giới hạn tối đa 2 con:
# - Thuật toán duyệt, tìm kiếm, chèn, xóa dễ hiểu, dễ cài đặt và chạy nhanh hơn.
# - Dễ dàng duy trì thứ tự sắp xếp trong Cây tìm kiếm nhị phân (BST).
# - Cân bằng cây thuận lợi hơn (ví dụ Cây AVL).
# - Có thể biểu diễn gọn gàng bằng Mảng liên tục (như cấu trúc Binary Heap), tiết kiệm bộ nhớ.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Xây dựng Cây nhị phân mẫu:
#         R
#       /   \
#      A     B
#     / \   / \
#    C   D E   F
#             /
#            G
root_sample = BinaryTreeNode("R")
nodeA = BinaryTreeNode("A")
nodeB = BinaryTreeNode("B")
nodeC = BinaryTreeNode("C")
nodeD = BinaryTreeNode("D")
nodeE = BinaryTreeNode("E")
nodeF = BinaryTreeNode("F")
nodeG = BinaryTreeNode("G")

root_sample.left = nodeA
root_sample.right = nodeB
nodeA.left = nodeC
nodeA.right = nodeD
nodeB.left = nodeE
nodeB.right = nodeF
nodeF.left = nodeG

print("\nBinary Tree Implementation:")
print("root.right.left.data:", root_sample.right.left.data)  # 'E'


# 6. Bốn loại Cây nhị phân đặc thù (Types of Binary Trees)
# - Balanced Binary Tree (Cây cân bằng):
#   Độ chênh lệch chiều cao giữa cây con trái và phải của mọi node không vượt quá 1.
# - Complete Binary Tree (Cây hoàn chỉnh):
#   Mọi tầng đều đầy đủ node, ngoại trừ tầng cuối cùng có thể khuyết nhưng phải được điền
#   liên tục từ trái sang phải. Cây hoàn chỉnh cũng luôn là cây cân bằng (nền tảng của Binary Heap).
# - Full Binary Tree (Cây đầy đủ):
#   Mỗi node đều có đúng 0 hoặc 2 con (không bao giờ tồn tại node chỉ có 1 con).
# - Perfect Binary Tree (Cây hoàn hảo):
#   Tất cả các node lá đều nằm ở cùng một tầng cuối cùng. Mọi node bên trong đều có đủ 2 con.
#   Cây hoàn hảo mang đủ cả 3 tính chất: Full, Balanced và Complete.


# 7. Cây tìm kiếm nhị phân (Binary Search Tree - BST)
# Các tính chất bắt buộc của BST:
# 1. Cây con bên trái của node X chỉ chứa các giá trị NHỎ HƠN X.
# 2. Cây con bên phải của node X chỉ chứa các giá trị LỚN HƠN X.
# 3. Cả hai cây con trái và phải đều phải là Cây tìm kiếm nhị phân (BST).
# Giả định tất cả các giá trị trong BST là duy nhất (unique values).
#
# Thuật ngữ bổ sung:
# - Size: Tổng số node trong cây (n).
# - Descendants (Hậu duệ): Toàn bộ node con, cháu, chắt... nằm bên dưới một node.
# - In-order successor (Node kế tiếp trung thứ tự): Node xuất hiện ngay sau node hiện tại
#   khi duyệt In-order (chính là node có giá trị nhỏ nhất trong cây con bên phải).


# 7.1. Duyệt In-order trên BST
# Duyệt In-order (Trái -> Gốc -> Phải) luôn tạo ra danh sách giá trị tăng dần (Ascending order).
# Đây là cách chuẩn xác nhất để kiểm tra một Cây nhị phân có phải là BST hay không.
def in_order_traversal(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    in_order_traversal(node.left, result)
    result.append(node.data)
    in_order_traversal(node.right, result)
    return result


# Xây dựng BST mẫu tiêu chuẩn:
#           13
#         /    \
#        7      15
#       / \    /  \
#      3   8  14   19
#                 /
#                18
bst_root = BinaryTreeNode(13)
node7 = BinaryTreeNode(7)
node15 = BinaryTreeNode(15)
node3 = BinaryTreeNode(3)
node8 = BinaryTreeNode(8)
node14 = BinaryTreeNode(14)
node19 = BinaryTreeNode(19)
node18 = BinaryTreeNode(18)

bst_root.left = node7
bst_root.right = node15
node7.left = node3
node7.right = node8
node15.left = node14
node15.right = node19
node19.left = node18

print("\nBST In-order Traversal (Should be sorted ascending):")
print(in_order_traversal(bst_root))  # [3, 7, 8, 13, 14, 15, 18, 19]


# 7.2. Tìm kiếm trên BST (Search for a value in a BST)
# Cơ chế hoạt động:
# - Bắt đầu từ node gốc.
# - Nếu target == node.data: tìm thấy node.
# - Nếu target < node.data: tiếp tục tìm ở cây con bên trái.
# - Nếu target > node.data: tiếp tục tìm ở cây con bên phải.
# - Nếu nhánh cần tìm là None: trả về None (không tìm thấy).
# Độ phức tạp thời gian: O(h) với h là chiều cao của cây.
def search(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target)
    else:
        return search(node.right, target)


res_13 = search(bst_root, 13)
if res_13:
    print(f"Found the node with value: {res_13.data}")
else:
    print("Value not found in the BST.")

res_99 = search(bst_root, 99)
if res_99:
    print(f"Found the node with value: {res_99.data}")
else:
    print("Value not found in the BST.")


# 7.3. Thêm phần tử vào BST (Insert a node in a BST)
# Cơ chế hoạt động:
# - Bắt đầu từ gốc và so sánh: nhỏ hơn đi sang trái, lớn hơn đi sang phải.
# - Khi gặp vị trí trống (None), tạo node mới và gắn vào đó.
# - Node mới thêm vào luôn trở thành một node lá (leaf node).
# - Nếu giá trị đã tồn tại, bỏ qua (đảm bảo tính unique).
def insert(node, data):
    if node is None:
        return BinaryTreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node


# Thêm giá trị 10 vào BST:
insert(bst_root, 10)
print("\nBST after inserting 10 (In-order):")
print(in_order_traversal(bst_root))  # [3, 7, 8, 10, 13, 14, 15, 18, 19]


# 7.4. Tìm giá trị nhỏ nhất trong cây con (Find the lowest value in a BST subtree)
# Bắt đầu từ node gốc của cây con, đi hết cỡ về bên trái cho đến khi không còn con trái.
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


lowest = min_value_node(bst_root)
print("Lowest value in the BST:", lowest.data)  # 3


# 7.5. Xóa phần tử trong BST (Delete a node in a BST)
# Ba trường hợp khi xóa một node:
# - Trường hợp 1: Node lá (không có con) -> Xóa liên kết, trả về None cho node cha.
# - Trường hợp 2: Node chỉ có 1 con (chỉ có con trái hoặc chỉ có con phải)
#   -> Nối node con đó trực tiếp vào node cha, bỏ qua node cần xóa.
# - Trường hợp 3: Node có đủ cả 2 con
#   -> Tìm node kế tiếp trung thứ tự (in-order successor = node nhỏ nhất ở cây con phải).
#   -> Gán giá trị của successor vào node hiện tại.
#   -> Đệ quy xóa node successor khỏi cây con bên phải.
def delete(node, data):
    if not node:
        return None
    if data < node.data:
        node.left = delete(node.left, data)
    elif data > node.data:
        node.right = delete(node.right, data)
    else:
        # Trường hợp 1 & 2: Node có 0 hoặc 1 con
        if not node.left:
            temp = node.right
            node = None
            return temp
        elif not node.right:
            temp = node.left
            node = None
            return temp

        # Trường hợp 3: Node có đủ 2 con
        temp = min_value_node(node.right)
        node.data = temp.data
        node.right = delete(node.right, temp.data)
    return node


# Xóa node 15 khỏi BST:
delete(bst_root, 15)
print("\nBST after deleting 15 (In-order):")
print(in_order_traversal(bst_root))  # [3, 7, 8, 10, 13, 14, 18, 19]


# 8. So sánh BST với Mảng đã sắp xếp và Danh sách liên kết
# - Sorted Array: Tìm kiếm O(log n), nhưng Thêm/Xóa tốn O(n) do phải dịch chuyển bộ nhớ.
# - Linked List: Tìm kiếm O(n), nhưng Thêm/Xóa không cần dịch chuyển bộ nhớ.
# - BST: VỪA tìm kiếm nhanh O(log n), VỪA Thêm/Xóa không cần dịch chuyển bộ nhớ!


# 9. Tính cân bằng và Độ phức tạp thời gian (BST Balance and Time Complexity)
# - Trên BST, các thao tác Search, Insert, Delete đều phụ thuộc vào chiều cao h: O(h).
# - Cây cân bằng (Balanced BST): h ≈ log2(n) -> Thao tác đạt O(log n).
# - Cây bị lệch hoàn toàn (Unbalanced BST): h ≈ n -> Thao tác bị thoái hóa về O(n).
# - Giải pháp: Cây AVL (AVL Tree) tự cân bằng để đảm bảo chiều cao luôn ở mức tối thiểu O(log n).
print("\nBST Summary:")
print("- Search, Insert, Delete: O(h) time complexity")
print("- Balanced BST: h = O(log n)")
print("- Unbalanced BST: h = O(n)")
