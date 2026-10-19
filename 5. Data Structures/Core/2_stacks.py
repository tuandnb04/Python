# 1. Khái niệm Ngăn xếp (Stacks) & Nguyên lý LIFO
# Ngăn xếp (Stack) là cấu trúc dữ liệu tuyến tính tuân theo nguyên tắc Last-In, First-Out (LIFO - Vào sau, Ra trước).
# - Hình ảnh ẩn dụ: Tương tự một chồng bánh kếp (pile of pancakes) - bạn chỉ có thể đặt thêm bánh mới
#   hoặc lấy bánh ra từ trên đỉnh (top). Chiếc bánh được đặt vào cuối cùng sẽ là chiếc đầu tiên được lấy ra.
#
# 5 thao tác cơ bản trên Stack:
# - Push: Thêm một phần tử mới vào đỉnh ngăn xếp.
# - Pop: Lấy ra và xóa phần tử ở đỉnh ngăn xếp.
# - Peek: Trả về phần tử ở đỉnh mà không xóa khỏi ngăn xếp.
# - isEmpty: Kiểm tra xem ngăn xếp có đang rỗng hay không.
# - Size: Đếm tổng số lượng phần tử hiện có trong ngăn xếp.

# 2. Cài đặt Stack trực tiếp bằng Python List (Stack using Python Lists)
# Python list có các phương thức .append() và .pop() ở cuối mảng với độ phức tạp O(1) amortized,
# rất lý tưởng để mô phỏng hành vi của một ngăn xếp:

stack = []

# Push: Thêm phần tử lên đỉnh
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack after pushes: ", stack)  # ['A', 'B', 'C']

# Peek: Xem phần tử đỉnh (phần tử cuối danh sách)
top_element = stack[-1]
print("Peek top element:   ", top_element)  # 'C'

# Pop: Lấy phần tử đỉnh ra
popped_element = stack.pop()
print("Popped element:     ", popped_element)  # 'C'
print("Stack after pop:    ", stack)  # ['A', 'B']

# isEmpty: Kiểm tra rỗng
is_empty = not bool(stack)
print("isEmpty:            ", is_empty)  # False

# Size: Độ lớn ngăn xếp
print("Size:               ", len(stack))  # 2

# 3. Đóng gói thành lớp Stack chuyên dụng (Dedicated Stack Class)
# Tạo class riêng biệt giúp che giấu chi tiết cài đặt (Encapsulation) và bảo vệ dữ liệu:
class Stack:
    def __init__(self) -> None:
        self.stack: list[str] = []

    def push(self, element: str) -> None:
        """Thêm phần tử vào đỉnh ngăn xếp."""
        self.stack.append(element)

    def pop(self) -> str:
        """Lấy phần tử đỉnh ra; trả về thông báo nếu ngăn xếp rỗng."""
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self) -> str:
        """Xem phần tử đỉnh mà không xóa."""
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """Kiểm tra ngăn xếp có rỗng không."""
        return len(self.stack) == 0

    def size(self) -> int:
        """Trả về số lượng phần tử trong ngăn xếp."""
        return len(self.stack)

# Thử nghiệm với lớp Stack:
my_stack = Stack()
my_stack.push('A')
my_stack.push('B')
my_stack.push('C')

print("\n--- Dedicated Stack Class Demo ---")
print("Stack:             ", my_stack.stack)
print("Pop:               ", my_stack.pop())        # 'C'
print("Stack after Pop:   ", my_stack.stack)        # ['A', 'B']
print("Peek:              ", my_stack.peek())       # 'B'
print("isEmpty:           ", my_stack.isEmpty())    # False
print("Size:              ", my_stack.size())       # 2

# 4. Đánh giá: Ưu và Nhược điểm khi dùng List / Array làm Stack
# - Ưu điểm:
#   + Tiết kiệm bộ nhớ (Memory Efficient): Mỗi phần tử mảng chỉ lưu trữ dữ liệu,
#     không tốn thêm con trỏ trỏ đến địa chỉ tiếp theo như danh sách liên kết (Linked List).
#   + Dễ cài đặt và dễ hiểu: Tận dụng trực tiếp các hàm tích hợp sẵn của Python.
# - Nhược điểm:
#   + Cơ chế cấp phát mảng: Khi mảng đầy, Python phải cấp phát vùng nhớ mới và sao chép phần tử sang,
#     gây tốn chi phí O(n) cục bộ tại thời điểm resize (dù trung bình là O(1) amortized).

# 5. Các ứng dụng thực tế phổ biến của Stack (Common Stack Applications)
# 1. Cơ chế Hoàn tác / Làm lại (Undo / Redo) trong các trình soạn thảo văn bản.
# 2. Lịch sử điều hướng trình duyệt web (Browser History: nút Back / Forward).
# 3. Ngăn xếp lời gọi hàm trong ngôn ngữ lập trình (Call Stack trong đệ quy).
# 4. Kiểm tra dấu ngoặc hợp lệ (Parentheses Matching Algorithm):
def is_valid_parentheses(s: str) -> bool:
    """Kiểm tra chuỗi dấu ngoặc có đóng mở hợp lệ hay không - O(n) Time, O(n) Space."""
    bracket_map = {')': '(', '}': '{', ']': '['}
    match_stack: list[str] = []

    for char in s:
        if char in bracket_map.values():
            match_stack.append(char)
        elif char in bracket_map:
            if not match_stack or match_stack.pop() != bracket_map[char]:
                return False

    return len(match_stack) == 0

print("\n--- Real-World Application: Parentheses Matching ---")
print("Is '([]){}' valid: ", is_valid_parentheses("([]){}"))  # True
print("Is '([)]' valid:   ", is_valid_parentheses("([)]"))    # False
