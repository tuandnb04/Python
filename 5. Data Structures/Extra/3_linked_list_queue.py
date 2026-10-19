# 1. Cài đặt Hàng đợi bằng Danh sách liên kết (Queue using Linked List)
# Trong danh sách liên kết, các nút (Node) không cần phải nằm liền kề nhau trong bộ nhớ.
# Một hàng đợi tối ưu bằng Linked List duy trì 2 con trỏ:
# - 'front' (đầu): Nơi các phần tử rời khỏi hàng đợi (Dequeue) -> O(1) thời gian, không cần dịch chuyển mảng!
# - 'rear' (cuối): Nơi các phần tử mới gia nhập hàng đợi (Enqueue) -> O(1) thời gian!

# Lớp Node đại diện cho một phần tử:
class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next: Node | None = None


# Lớp Queue cài đặt bằng Danh sách liên kết:
class LinkedListQueue:
    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None
        self.length: int = 0

    def enqueue(self, element: str) -> None:
        """Thêm một phần tử vào cuối hàng đợi (rear)."""
        new_node = Node(element)
        if self.rear is None:
            # Hàng đợi ban đầu rỗng, nút mới vừa là front vừa là rear
            self.front = self.rear = new_node
            self.length += 1
            return
        # Nối nút mới vào sau rear hiện tại và cập nhật rear
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self) -> str:
        """Lấy phần tử ở đầu hàng đợi (front) ra khỏi hàng."""
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        assert temp is not None
        self.front = temp.next
        self.length -= 1
        # Nếu sau khi lấy ra hàng đợi rỗng hoàn toàn, đặt rear về None
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self) -> str:
        """Xem phần tử ở đầu hàng đợi mà không xóa."""
        if self.isEmpty():
            return "Queue is empty"
        assert self.front is not None
        return self.front.data

    def isEmpty(self) -> bool:
        """Kiểm tra hàng đợi có rỗng không."""
        return self.length == 0

    def size(self) -> int:
        """Trả về số lượng phần tử hiện tại."""
        return self.length

    def printQueue(self) -> None:
        """Duyệt và in toàn bộ hàng đợi từ front đến rear."""
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 2. Chạy thử nghiệm các thao tác với LinkedListQueue
my_queue = LinkedListQueue()

# Enqueue các phần tử 'A', 'B', 'C':
my_queue.enqueue('A')
my_queue.enqueue('B')
my_queue.enqueue('C')

print("Queue:                  ", end="")
my_queue.printQueue()  # A -> B -> C -> None

print("Peek front element:     ", my_queue.peek())     # 'A'
print("Dequeue element (FIFO): ", my_queue.dequeue())  # 'A'

print("Queue after Dequeue:    ", end="")
my_queue.printQueue()  # B -> C -> None

print("isEmpty:                ", my_queue.isEmpty())  # False
print("Size:                   ", my_queue.size())     # 2

# 3. Phân tích so sánh: Linked List vs Mảng / Danh sách trong việc cài đặt Queue
# - Ưu điểm của Linked List:
#   + Kích thước hoàn toàn động (Dynamic size): Tự do co giãn theo nhu cầu, không phụ thuộc vào mảng cố định.
#   + Không cần dồn mảng (No shifting): Thao tác dequeue lấy phần tử đầu ra chỉ tốn O(1) thời gian,
#     hoàn toàn vượt trội so với list.pop(0) tốn O(n) do phải dịch chuyển n - 1 phần tử còn lại.
# - Nhược điểm của Linked List:
#   + Tốn thêm bộ nhớ (Extra memory overhead): Mỗi phần tử cần thêm 1 con trỏ 'next' (tốn thêm 8 bytes trên 64-bit OS).
#   + Độ phức tạp mã nguồn (Code readability): Cần tự quản lý các liên kết con trỏ front, rear và trường hợp rỗng.
