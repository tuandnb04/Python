# 1. Hash Map (Dictionary trong Python) - Quản lý các cặp key-value duy nhất
# - Cơ chế: Dùng hàm băm (Hash Function) tính vị trí ô nhớ -> Thao tác trung bình O(1)
# - Hash Collision (Xung đột băm): Khi 2 key khác nhau cho cùng 1 hash value (xử lý bằng Chaining / Open Addressing)
my_map = {'A': 1, 'B': 2, 'C': 3}

# Thao tác: Insert, Access, Update, Delete -> O(1) trung bình (O(n) xấu nhất khi nhiều va chạm)
my_map['D'] = 4                           # Insert O(1)
print("Lookup 'B' (O(1)):", my_map['B'])  # 2
del my_map['A']                           # Delete O(1)
print("'C' in map:", 'C' in my_map)       # True

# 2. Set trong Python - Lưu các phần tử đơn lẻ duy nhất (không trùng lặp), không thứ tự
# - Cài đặt bằng Hash Table chỉ lưu key (chỉ nhận các phần tử bất biến / hashable)
# - Thao tác .add(), .remove(), 'in': O(1) trung bình
my_set = {1, 2, 3, 4}
my_set.add(5)                             # Add O(1)
my_set.remove(2)                          # Remove O(1)
print("5 in set (O(1)):", 5 in my_set)    # True

# Các phép toán tập hợp cơ bản
s1, s2 = {1, 2, 3}, {3, 4, 5}
print("Union (|):", s1 | s2)              # {1, 2, 3, 4, 5}
print("Intersection (&):", s1 & s2)       # {3}
