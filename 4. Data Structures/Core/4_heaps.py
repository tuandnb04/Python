import heapq

# HEAP & PRIORITY QUEUE (HEAP & HÀNG ĐỢI ƯU TIÊN)
#
# 1. KHÁI NIỆM & ĐẶC ĐIỂM CỦA HEAP:
# - Heap là cấu trúc cây nhị phân hoàn chỉnh (Complete Binary Tree) tuân theo Heap Property:
#   + Min-Heap: Giá trị node cha <= các node con (gốc luôn là phần tử NHỎ NHẤT).
#   + Max-Heap: Giá trị node cha >= các node con (gốc luôn là phần tử LỚN NHẤT).
# - Biểu diễn bằng Mảng (Array/List) dựa trên chỉ số (Index i):
#   + Node cha (Parent):       (i - 1) // 2
#   + Node con trái (Left):    2 * i + 1
#   + Node con phải (Right):   2 * i + 2
# - Độ phức tạp:
#   + heappush / heappop:             O(log n)
#   + peek (phần tử gốc heap[0]):     O(1)
#   + heapify (dựng heap từ list):    O(n)
#   + Tìm kiếm / Xóa phần tử bất kỳ:  O(n) (vì không có tính chất thứ tự toàn phần như BST)
#   + Độ phức tạp không gian:         O(n)

# 2. THAO TÁC CƠ BẢN VỚI MIN-HEAP (MODULE HEAPQ):
numbers = [9, 3, 7, 1, 5]
heapq.heapify(numbers)                     # Chuyển list thành min-heap in-place: O(n)
print("Min-heap after heapify:", numbers)

heapq.heappush(numbers, 2)                 # Thêm phần tử: O(log n)
print("Min element (peek - O(1)):", numbers[0]) # 1
print("Popped min (O(log n)):", heapq.heappop(numbers)) # 1

# heappushpop(): Thêm 1 phần tử rồi pop phần tử nhỏ nhất ra ngay.
# Tối ưu hơn gọi heappush() rồi heappop() riêng lẻ vì chỉ cần 1 lần tái cân bằng:
res = heapq.heappushpop(numbers, 4)
print("heappushpop(4) result:", res)


# 3. KỸ THUẬT MÔ PHỎNG MAX-HEAP TRONG PYTHON:
# Python heapq chỉ hỗ trợ Min-Heap mặc định. Để làm Max-Heap, ta đảo dấu (-val):
max_heap = []
for val in [10, 30, 20, 5]:
    heapq.heappush(max_heap, -val)         # Đảo dấu khi đưa vào

max_item = -heapq.heappop(max_heap)        # Đảo dấu ngược lại khi lấy ra
print("Popped max element:", max_item)      # 30


# 4. PRIORITY QUEUE (HÀNG ĐỢI ƯU TIÊN):
# - Sử dụng tuple: (priority, task)
# - Số priority càng nhỏ -> Độ ưu tiên càng cao (xử lý trước)
pq = []
heapq.heappush(pq, (3, "Low priority task"))
heapq.heappush(pq, (1, "Critical urgent task"))
heapq.heappush(pq, (2, "Medium priority task"))

print("\n--- Basic Priority Queue ---")
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority {priority}: {task}")

# Kỹ thuật Tie-breaking (Xử lý khi trùng độ ưu tiên):
# Khi 2 task cùng priority, Python sẽ so sánh phần tử kế tiếp trong tuple.
# Thêm counter (bộ đếm thứ tự) để giữ đúng chuẩn FIFO và tránh lỗi so sánh nếu task là object:
# Format: (priority, counter, task)
pq_stable = []
counter = 0

def add_task(priority: int, task: str) -> None:
    global counter
    heapq.heappush(pq_stable, (priority, counter, task))
    counter += 1

add_task(1, "Task A (inserted first)")
add_task(2, "Task B")
add_task(1, "Task C (inserted later, same priority as A)")

print("\n--- Priority Queue with Tie-breaking (FIFO for same priority) ---")
while pq_stable:
    p, c, t = heapq.heappop(pq_stable)
    print(f"Priority {p} (order #{c}): {t}")
