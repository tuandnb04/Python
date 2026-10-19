from collections import deque

# 1. Khái niệm Hàng đợi (Queue) & Nguyên lý FIFO
# Hàng đợi (Queue) là cấu trúc dữ liệu tuyến tính tuân theo nguyên tắc First-In, First-Out (FIFO - Vào trước, Ra trước).
# - Hình ảnh ẩn dụ: Hãy tưởng tượng hàng người xếp hàng thanh toán tại siêu thị (supermarket line).
#   Người đầu tiên xếp hàng cũng chính là người đầu tiên được thanh toán tiền và rời khỏi siêu thị.
#   Phần tử được thêm vào đầu tiên sẽ luôn là phần tử đầu tiên được lấy ra.
#
# 5 thao tác cơ bản trên Queue:
# - Enqueue: Thêm một phần tử mới vào cuối hàng đợi.
# - Dequeue: Lấy ra và xóa phần tử ở đầu hàng đợi (front).
# - Peek: Xem phần tử ở đầu hàng đợi mà không xóa.
# - isEmpty: Kiểm tra xem hàng đợi có đang rỗng không.
# - Size: Tìm tổng số lượng phần tử hiện có trong hàng đợi.

# 2. Cài đặt Hàng đợi bằng Python List (Queue using Python Lists)
# Tương tự như Stack, ta có thể dùng List tích hợp để thực hiện các thao tác Queue cơ bản:
queue = []

# Enqueue: Thêm vào cuối
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue:               ", queue)  # ['A', 'B', 'C']

# Peek: Xem phần tử đầu tiên (index 0)
front_element = queue[0]
print("Peek:                ", front_element)  # 'A'

# Dequeue: Lấy phần tử đầu tiên ra bằng pop(0)
popped_element = queue.pop(0)
print("Dequeue:             ", popped_element)  # 'A'
print("Queue after Dequeue: ", queue)  # ['B', 'C']

# isEmpty: Kiểm tra rỗng
is_empty = not bool(queue)
print("isEmpty:             ", is_empty)  # False

# Size: Độ lớn hàng đợi
print("Size:                ", len(queue))  # 2

# 3. Đóng gói thành lớp Queue dùng List (Queue Class Implementation)
# Đóng gói danh sách thành một lớp riêng biệt với các phương thức chuẩn:
class ListQueue:
    def __init__(self) -> None:
        self.queue: list[str] = []

    def enqueue(self, element: str) -> None:
        """Thêm phần tử vào cuối hàng đợi."""
        self.queue.append(element)

    def dequeue(self) -> str:
        """Lấy phần tử ở đầu hàng đợi ra (O(n))."""
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self) -> str:
        """Xem phần tử ở đầu hàng đợi."""
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self) -> bool:
        """Kiểm tra hàng đợi có rỗng không."""
        return len(self.queue) == 0

    def size(self) -> int:
        """Trả về số phần tử trong hàng đợi."""
        return len(self.queue)

# Chạy thử nghiệm lớp ListQueue:
my_queue = ListQueue()
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print("\n--- Dedicated ListQueue Class Demo ---")
print("Queue:               ", my_queue.queue)
print("Peek:                ", my_queue.peek())        # 'A'
print("Dequeue:             ", my_queue.dequeue())     # 'A'
print("Queue after Dequeue: ", my_queue.queue)        # ['B', 'C']
print("isEmpty:             ", my_queue.isEmpty())     # False
print("Size:                ", my_queue.size())        # 2

# 4. Cạm bẫy hiệu năng & Giải pháp tối ưu: collections.deque
# - Lưu ý quan trọng: Mặc dù dùng List rất đơn giản, thao tác dequeue (queue.pop(0))
#   bắt buộc phải dịch chuyển toàn bộ n - 1 phần tử còn lại trong RAM sang trái, tốn O(n) thời gian.
# - Trong môi trường thực tế với hàng triệu phần tử, ta dùng `collections.deque` (Double-ended Queue):
#   Được triển khai dưới dạng danh sách liên kết đôi ở tầng C, cho phép popleft() với thời gian O(1):

fast_queue = deque()
fast_queue.append("A")
fast_queue.append("B")
fast_queue.append("C")
print("\n--- Optimized Deque O(1) Demo ---")
print("Fast Queue:          ", list(fast_queue))
print("Fast Dequeue O(1):   ", fast_queue.popleft())  # 'A'
print("Fast Queue remaining:", list(fast_queue))      # ['B', 'C']

# 5. Các ứng dụng thực tế phổ biến của Queue (Common Queue Applications)
# 1. Hàng đợi tác vụ cho máy in văn phòng (Printer Spooler / Job Scheduling).
# 2. Xử lý đơn hàng đặt vé điện tử (Order Processing for E-tickets - FIFO công bằng).
# 3. Thuật toán tìm kiếm theo chiều rộng trên đồ thị và cây (BFS - Breadth-First Search).
# 4. Lập lịch tiến trình tác vụ trong hệ điều hành (Task Scheduling in OS).
# 5. Hệ thống hàng đợi tin nhắn trong kiến trúc phân tán (Message Queues: RabbitMQ, Apache Kafka).
