from collections import deque

# 1. Stack (Ngăn xếp - LIFO: Last-In, First-Out)
# - Thao tác push (thêm vào đỉnh), pop (lấy ra từ đỉnh) -> Độ phức tạp O(1)
stack = []
stack.append(10)                       # Push 10
stack.append(20)                       # Push 20
stack.append(30)                       # Push 30

print("Stack top (peek):", stack[-1])  # 30
print("Stack pop (LIFO):", stack.pop())# 30 (lấy ra phần tử được thêm cuối cùng)
print("Remaining stack:", stack)       # [10, 20]

# 2. Queue (Hàng đợi - FIFO: First-In, First-Out)
# - Thao tác enqueue (thêm vào cuối), dequeue (lấy ra từ đầu) -> Độ phức tạp O(1) với deque
queue = deque()
queue.append("Alice")                  # Enqueue Alice
queue.append("Bob")                    # Enqueue Bob
queue.append("Charlie")                # Enqueue Charlie

print("Queue front (peek):", queue[0]) # Alice
print("Queue dequeue (FIFO):", queue.popleft()) # Alice (lấy ra phần tử đầu hàng)
print("Remaining queue:", list(queue)) # ['Bob', 'Charlie']
