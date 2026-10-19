# 5. Data Structures: Bảng băm tự thiết kế (Custom Hash Table from Scratch)
#
# LÝ THUYẾT NỀN TẢNG: BẢNG BĂM & KIỂU DỮ LIỆU ÁNH XẠ (MAP ADT)
# 1. Khái niệm ADT (Abstract Data Type) & Map vs Hash Table:
#    - Map (ADT): Bản thiết kế trừu tượng mô tả tập hợp các cặp khóa-giá trị (Key-Value)
#      với Key là duy nhất.
#    - Hash Table: Cấu trúc dữ liệu cài đặt vật lý cụ thể cho Map ADT bằng cách sử dụng
#      Hàm băm (Hash Function) để chuyển đổi Key thành vị trí ô nhớ (Index) trong mảng ngầm định.
#
# 2. Độ phức tạp (Complexity):
#    - Tra cứu (Lookup), Thêm (Insert), Xóa (Delete):
#      + Trung bình (Average): O(1) - Nhảy thẳng tới ô nhớ bằng mã băm.
#      + Tệ nhất (Worst case): O(n) - Khi tất cả các key bị băm vào cùng một bucket (xung đột băm).
#    - Không gian (Space): O(n) cho mảng bucket và các phần tử lưu trữ.
#
# 3. Chiến lược giải quyết xung đột băm (Collision Resolution):
#    - Separate Chaining (Nối chuỗi): Mỗi bucket là một danh sách con (hoặc DSLK) lưu tất cả
#      các phần tử trùng chỉ số (đây là kỹ thuật được minh họa trong file này).
#    - Open Addressing (Địa chỉ mở): Khi xảy ra xung đột, dò tìm vị trí trống tiếp theo
#      trong mảng (Python dict & set sử dụng biến thể tối ưu của Open Addressing ở tầng C).
#
# Lưu ý: Các kiểu dữ liệu ánh xạ tích hợp sẵn trong Python như dict, set, defaultdict,
# Counter đã được học chi tiết trong thư mục [1. Collections]. File này tập trung vào
# cơ chế bên dưới (Under the hood) để hiểu cách máy tính hiện thực hóa O(1).


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
        index = self._hash(key)
        return any(k == key for k, _ in self.buckets[index])

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
