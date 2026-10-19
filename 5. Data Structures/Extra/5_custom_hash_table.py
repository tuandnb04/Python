# 5. Data Structures - Extra: Bảng băm tự thiết kế (Custom Hash Table from Scratch)
# Xây dựng Bảng băm (Hash Table) từ đầu theo 5 bước chuẩn mực DSA
#
# Lý do sử dụng Hash Table:
# - Trong Linked List: Tìm "Bob" phải duyệt qua từng node O(n).
# - Trong Array / List: Tìm "Bob" khi chưa biết index phải quét toàn bộ mảng O(n).
# - Trong Hash Table: Hàm băm tính ra vị trí lưu trữ và nhảy thẳng đến bucket trong O(1) trung bình.

# 1. Bước 1: Tạo danh sách Bucket ban đầu
# Tạo danh sách 10 phần tử trống. Mỗi vị trí được gọi là một "bucket" (thùng chứa).
initial_table = [None] * 10
print("Step 1 - Initial empty buckets:", initial_table)


# 2. Bước 2: Xây dựng hàm băm (Hash Function)
# Chuyển giá trị chuỗi thành chỉ số từ 0 đến 9 bằng cách tính tổng mã Unicode chia lấy dư cho 10.
def simple_hash(value, size=10):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
    return sum_of_chars % size


# Minh họa tính toán cho "Bob":
# B (66) + o (111) + b (98) = 275 -> 275 % 10 = 5.
bob_code = simple_hash("Bob")
print(f"Step 2 - 'Bob' has hash code: {bob_code}")


# 3. Bước 3: Thêm phần tử (Insertion chưa xử lý xung đột)
def simple_add(table, name):
    index = simple_hash(name, len(table))
    table[index] = name


simple_add(initial_table, "Bob")
print("Step 3 - After adding 'Bob':", initial_table)

simple_add(initial_table, "Pete")
simple_add(initial_table, "Jones")
simple_add(initial_table, "Lisa")
simple_add(initial_table, "Siri")
print("Step 3 - After adding Pete, Jones, Lisa, Siri:", initial_table)


# 4. Bước 4: Tìm kiếm phần tử (Lookup O(1))
# Nhờ hàm băm, truy cập thẳng vào ô index mà không cần duyệt qua từng phần tử.
def simple_contains(table, name):
    index = simple_hash(name, len(table))
    return table[index] == name


print("Step 4 - Contains 'Pete':", simple_contains(initial_table, "Pete"))  # True (index 8)
print("Step 4 - Contains 'Alice':", simple_contains(initial_table, "Alice"))  # False


# 5. Bước 5: Xử lý xung đột bằng phương pháp nối chuỗi (Chaining)
# Vấn đề: "Stuart" có mã băm là 3 (83+116+117+97+114+116 = 653 % 10 = 3).
# Nhưng index 3 đã bị "Lisa" chiếm chỗ. Nếu ghi đè sẽ làm mất "Lisa".
# Giải pháp Chaining: Mỗi bucket là một danh sách con chứa được nhiều phần tử.
chained_table = [[] for _ in range(10)]


def chained_add(table, name):
    index = simple_hash(name, len(table))
    table[index].append(name)


def chained_contains(table, name):
    index = simple_hash(name, len(table))
    return name in table[index]


for name in ["Bob", "Pete", "Jones", "Lisa", "Siri", "Stuart"]:
    chained_add(chained_table, name)

print("\nStep 5 - Chained table buckets:")
for idx, bucket in enumerate(chained_table):
    print(f"  Bucket {idx}: {bucket}")

print("Step 5 - Contains 'Stuart' (chained in bucket 3):", chained_contains(chained_table, "Stuart"))
print("Step 5 - Contains 'Lisa' (still preserved in bucket 3):", chained_contains(chained_table, "Lisa"))


# 6. Bước 6: Đóng gói OOP hoàn chỉnh (ChainedHashTable Key-Value)
# Cài đặt đầy đủ bảng băm lưu trữ cặp (Key, Value) với các phương thức put, get, remove.
class ChainedHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        key_str = str(key)
        return sum(ord(c) for c in key_str) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key, default=None):
        index = self._hash(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def __contains__(self, key):
        return self.get(key) is not None

    def __len__(self):
        return self.size

    def display(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items_str = ", ".join(f"{k}: {v}" for k, v in bucket)
                result.append(f"Bucket {i} -> [{items_str}]")
            else:
                result.append(f"Bucket {i} -> []")
        return "\n".join(result)


# Thử nghiệm OOP ChainedHashTable:
print("\nStep 6 - OOP ChainedHashTable demo:")
ht = ChainedHashTable(capacity=7)
ht.put("Alice", "0901-111-222")
ht.put("Bob", "0902-333-444")
ht.put("Charlie", "0903-555-666")
ht.put("David", "0904-777-888")

print(ht.display())
print("Lookup 'Bob':", ht.get("Bob"))
print("Lookup 'Eve' (default):", ht.get("Eve", "Not Found"))
print("'Alice' in ht:", "Alice" in ht)

# Xóa phần tử:
ht.remove("Bob")
print("Lookup 'Bob' after remove:", ht.get("Bob"))
print("Current size:", len(ht))
