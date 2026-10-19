# 1. Cài đặt Ngăn xếp bằng Danh sách liên kết (Stack using Linked List)
# Danh sách liên kết (Linked List) bao gồm các nút (Node), mỗi nút chứa dữ liệu (value)
# và một con trỏ (next) trỏ tới nút kế tiếp trong bộ nhớ.
#
# Đỉnh của Stack (top) sẽ ứng với phần tử đầu (head) của Linked List:
# - Push: Tạo nút mới, trỏ next của nút mới vào head hiện tại, cập nhật head = new_node -> O(1)
# - Pop: Lấy giá trị của head, trỏ head sang head.next, giảm size -> O(1)

# Lớp Node đại diện cho một nút trong danh sách liên kết:
class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.next: Node | None = None


# Lớp Stack cài đặt bằng Linked List:
class LinkedListStack:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size: int = 0

    def push(self, value: str) -> None:
        """Thêm một phần tử vào đỉnh ngăn xếp (chèn vào đầu danh sách liên kết)."""
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self) -> str:
        """Lấy phần tử ở đỉnh ra; trả về thông báo nếu ngăn xếp rỗng."""
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        assert popped_node is not None
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self) -> str:
        """Xem giá trị phần tử ở đỉnh ngăn xếp."""
        if self.isEmpty():
            return "Stack is empty"
        assert self.head is not None
        return self.head.value

    def isEmpty(self) -> bool:
        """Kiểm tra ngăn xếp có rỗng hay không."""
        return self.size == 0

    def stackSize(self) -> int:
        """Trả về kích thước hiện tại của ngăn xếp."""
        return self.size

    def traverseAndPrint(self) -> None:
        """Duyệt và in toàn bộ các phần tử từ đỉnh xuống đáy."""
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")


# 2. Chạy thử nghiệm các thao tác với LinkedListStack
my_stack = LinkedListStack()

# Push các phần tử 'A', 'B', 'C'
my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print("LinkedList Stack:        ", end="")
my_stack.traverseAndPrint()  # C -> B -> A -> None

print("Peek top element:        ", my_stack.peek())  # 'C'
print("Pop top element:         ", my_stack.pop())   # 'C'

print("LinkedList after Pop:    ", end="")
my_stack.traverseAndPrint()  # B -> A -> None

print("isEmpty:                 ", my_stack.isEmpty())    # False
print("Size:                    ", my_stack.stackSize())  # 2

# 3. Phân tích so sánh: Linked List vs Mảng / Danh sách trong việc cài đặt Stack
# - Ưu điểm của Linked List:
#   + Kích thước hoàn toàn động (Dynamic size): Các node được cấp phát phân tán ở bất kỳ ô nhớ trống nào,
#     không yêu cầu bộ nhớ phải liền kề nhau như mảng.
#   + Không bao giờ phải chịu chi phí tái cấp phát mảng (No array resizing / copying overhead).
# - Nhược điểm của Linked List:
#   + Tốn thêm bộ nhớ (Extra memory overhead): Mỗi phần tử bắt buộc phải lưu thêm con trỏ 'next'.
#   + Độ phức tạp mã nguồn (Code readability): Dài hơn và phức tạp hơn khi triển khai so với dùng list tích hợp.
#   + Kém thân thiện với CPU Cache (Cache locality): Do các node nằm rải rác trên Heap RAM.
