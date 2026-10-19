# 1. Khái niệm Danh sách liên kết (Linked Lists) & So sánh với Mảng (Arrays)
# Danh sách liên kết là cấu trúc dữ liệu tuyến tính bao gồm các nút (Node) liên kết với nhau.
# Mỗi nút chứa 2 phần: Dữ liệu (data) và Con trỏ / Liên kết (next pointer) trỏ tới địa chỉ ô nhớ của nút tiếp theo.
#
# So sánh chi tiết giữa Arrays và Linked Lists:
# - Cấu trúc có sẵn: Arrays có sẵn trong Python (list) | Linked Lists phải tự cài đặt bằng Node.
# - Kích thước bộ nhớ: Arrays cấp phát theo mảng liên tục | Linked Lists cấp phát động từng node trên Heap.
# - Tiêu thụ bộ nhớ: Arrays chỉ lưu phần tử | Linked Lists tốn thêm bộ nhớ lưu con trỏ (next pointer).
# - Truy cập ngẫu nhiên: Arrays đạt O(1) qua chỉ số | Linked Lists tốn O(n) do phải duyệt từ đầu.
# - Chèn / Xóa: Arrays tốn O(n) do phải dồn mảng | Linked Lists đạt O(1) khi đã trỏ tới vị trí node.

# 2. Các loại Danh sách liên kết (Types of Linked Lists)
# 1. Singly Linked List (Đơn): Mỗi node chỉ có 1 con trỏ 'next' trỏ tới node kế tiếp.
# 2. Doubly Linked List (Đôi): Mỗi node có 2 con trỏ: 'prev' (node trước) và 'next' (node sau).
# 3. Circular Linked List (Vòng): Nút cuối cùng (tail) trỏ ngược lại nút đầu tiên (head),
#    thích hợp cho các ứng dụng cần xoay vòng liên tục (như đổi lượt chơi, phát nhạc lặp lại).

# Lớp Node cơ bản cho Singly Linked List:
class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node | None = None


# 3. Duyệt danh sách liên kết (Traversal of a Linked List)
# Bắt đầu từ nút head và lần theo con trỏ next cho đến khi gặp None:
def traverse_and_print(head: Node | None) -> None:
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")


# Khởi tạo 5 node rời rạc và liên kết chúng thành chuỗi: 7 -> 11 -> 3 -> 2 -> 9 -> null
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Linked list traversal:")
traverse_and_print(node1)

# 4. Thuật toán tìm giá trị nhỏ nhất (Find The Lowest Value)
# Tương tự như duyệt mảng: gán min_val = head.data, duyệt qua từng node và cập nhật:
def find_lowest_value(head: Node) -> int:
    min_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value

print("\nLowest value in linked list:", find_lowest_value(node1))  # 2

# 5. Xóa một nút cụ thể (Delete a Specific Node)
# Để xóa một node mà không làm đứt chuỗi:
# Nối con trỏ next của node đứng trước trực tiếp tới node đứng sau node cần xóa:
def delete_specific_node(head: Node | None, node_to_delete: Node) -> Node | None:
    if head == node_to_delete:
        return head.next

    current_node = head
    while current_node and current_node.next and current_node.next != node_to_delete:
        current_node = current_node.next

    if current_node and current_node.next:
        # Bỏ qua node_to_delete và nối thẳng tới node kế tiếp:
        current_node.next = current_node.next.next

    return head

print("\n--- Deleting Node with value 2 ---")
print("Before deletion: ", end="")
traverse_and_print(node1)

node1 = delete_specific_node(node1, node4)

print("After deletion:  ", end="")
traverse_and_print(node1)  # 7 -> 11 -> 3 -> 9 -> null

# 6. Chèn nút vào vị trí cụ thể (Insert a Node at Position)
# Vị trí position tính từ 1 (1-indexed):
def insert_node_at_position(head: Node | None, new_node: Node, position: int) -> Node | None:
    if position == 1:
        new_node.next = head
        return new_node

    current_node = head
    for _ in range(position - 2):
        if current_node is None or current_node.next is None:
            break
        current_node = current_node.next

    if current_node is not None:
        new_node.next = current_node.next
        current_node.next = new_node

    return head

# Chèn node mới có giá trị 97 vào vị trí thứ 2 (giữa 7 và 11):
new_node_97 = Node(97)
node1 = insert_node_at_position(node1, new_node_97, 2)

print("\n--- Inserting Node 97 at Position 2 ---")
print("After insertion: ", end="")
traverse_and_print(node1)  # 7 -> 97 -> 11 -> 3 -> 9 -> null

# 7. Danh sách liên kết đôi (Doubly Linked List) & Vòng (Circular)
class DoublyNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.prev: DoublyNode | None = None
        self.next: DoublyNode | None = None

# Tạo chuỗi đôi: 10 <-> 20 <-> 30
d1 = DoublyNode(10)
d2 = DoublyNode(20)
d3 = DoublyNode(30)
d1.next = d2
d2.prev = d1
d2.next = d3
d3.prev = d2

print("\nDoubly linked list (Forward):  ", f"{d1.data} <-> {d2.data} <-> {d3.data}")
print("Doubly linked list (Backward): ", f"{d3.data} <-> {d2.data} <-> {d1.data}")

# Minh họa Circular Linked List (vòng tròn):
d3.next = d1  # Nút cuối trỏ ngược về nút đầu
print("Circular check (d3.next == d1):", d3.next == d1)  # True

# 8. Phân tích độ phức tạp thời gian (Time Complexity of Linked Lists)
# - Tìm kiếm tuyến tính (Linear Search): O(n) - duyệt từ head đến tail.
# - Tìm kiếm nhị phân (Binary Search): KHÔNG KHẢ THI trên Linked List vì không thể truy cập
#   trực tiếp phần tử ở giữa trong O(1) như mảng (không hỗ trợ random indexing arr[mid]).
# - Thuật toán sắp xếp (Sorting): Các thuật toán yêu cầu truy cập ngẫu nhiên (như QuickSort với index partition)
#   rất khó triển khai hiệu quả trên Linked List. Thay vào đó, Merge Sort là thuật toán sắp xếp lý tưởng nhất cho Linked List (O(n log n)).
