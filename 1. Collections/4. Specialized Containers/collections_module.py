from collections import Counter, defaultdict, deque, namedtuple

# 1. Counter: Bộ đếm tần suất tự động
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print("Word counts:", counts)
print("Count of 'apple':", counts["apple"])
print("Count of 'missing':", counts["missing"])  # Tự trả về 0, không lỗi KeyError
print("Top 2 common:", counts.most_common(2))

# 2. defaultdict: Từ điển tự khởi tạo giá trị khi gặp key mới
# Gom nhóm dữ liệu theo khoa:
students = [("IT", "Alice"), ("Math", "Bob"), ("IT", "Charlie")]
groups = defaultdict(list)
for dept, student in students:
    groups[dept].append(student)

print("Grouped by dept:", dict(groups))

# 3. namedtuple: Tuple có tên trường, truy cập thuộc tính như object nhưng nhẹ và bất biến
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"Point coordinates: x={p.x}, y={p.y}")
print("Access by index:", p[0])

# 4. deque: Hàng đợi hai đầu (chèn/xóa ở 2 đầu đạt O(1))
queue = deque(["middle"])
queue.append("right")       # Thêm vào đuôi
queue.appendleft("left")    # Thêm vào đầu
print("Deque elements:", list(queue))

queue.pop()                 # Lấy ra từ đuôi
queue.popleft()             # Lấy ra từ đầu
print("Deque after pops:", list(queue))

# Giới hạn kích thước (maxlen) tự trượt khi đầy:
recent = deque(maxlen=3)
for i in range(1, 6):
    recent.append(f"task_{i}")
print("Recent 3 tasks:", list(recent))
