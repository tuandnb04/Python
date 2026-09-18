import heapq

# Min-Heap với module heapq trong Python
# - Cài đặt dạng mảng (Array/List): Dễ dàng tính toán chỉ số cha/con bằng công thức toán học
# - Độ phức tạp: heappush O(log n), heappop O(log n), peek O(1), heapify O(n)

numbers = [9, 3, 7, 1, 5]
heapq.heapify(numbers)                     # Chuyển list thành min-heap in-place: O(n)
print("Min-heap:", numbers)

heapq.heappush(numbers, 2)                 # Thêm phần tử: O(log n)
print("Min element (peek - O(1)):", numbers[0]) # 1
print("Popped min (O(log n)):", heapq.heappop(numbers)) # 1

# Hàng đợi ưu tiên (Priority Queue) - Dùng tuple (priority, task)
# - Số priority càng nhỏ -> Độ ưu tiên càng cao (xử lý trước)
# - Ứng dụng: Lập lịch tiến trình trong hệ điều hành (OS Task Scheduling), Dijkstra
pq = []
heapq.heappush(pq, (3, "Low priority task"))
heapq.heappush(pq, (1, "Critical urgent task"))
heapq.heappush(pq, (2, "Medium priority task"))

print("\n--- Priority Queue Processing Order ---")
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Priority {priority}: {task}")
