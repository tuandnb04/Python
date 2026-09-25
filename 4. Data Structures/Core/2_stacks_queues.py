from collections import deque

# Stack (Ngăn xếp - LIFO: Last-In, First-Out - Như chồng đĩa)
# - Hai đầu: top (đỉnh) và bottom (đáy). Mọi thao tác thêm (push) / lấy (pop) đều diễn ra ở top -> O(1)
stack = []
stack.append(10)                       # Push 10
stack.append(20)                       # Push 20
stack.append(30)                       # Push 30

print("Stack top (peek):", stack[-1])  # 30
print("Stack pop (LIFO):", stack.pop())# 30 (lấy ra phần tử được thêm cuối cùng)
print("Remaining stack:", stack)       # [10, 20]

# Queue (Hàng đợi - FIFO: First-In, First-Out - Như hàng người xếp hàng)
# - Hai đầu: back (thêm cuối - enqueue) và front (lấy đầu - dequeue) -> O(1) với collections.deque
#   (Lưu ý: Không dùng list thường làm Queue vì list.pop(0) tốn O(n) dịch chuyển mảng)
queue = deque()
queue.append("Alice")                  # Enqueue Alice
queue.append("Bob")                    # Enqueue Bob
queue.append("Charlie")                # Enqueue Charlie

print("Queue front (peek):", queue[0]) # Alice
print("Queue dequeue (FIFO):", queue.popleft()) # Alice (lấy ra phần tử đầu hàng)
print("Remaining queue:", list(queue)) # ['Bob', 'Charlie']

# Ghi chú: Để xem cách tự xây dựng Class Generic Stack & Queue theo hướng đối tượng (OOP),
# vui lòng tham khảo file: 4. Data Structures/Extra/4_custom_stack_queue.py

