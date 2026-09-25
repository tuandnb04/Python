from collections import defaultdict, Counter

# 1. HASH MAP (Dictionary trong Python)
# - Cơ chế: Dùng hàm băm (Hash Function) tính vị trí ô nhớ -> Thao tác O(1) amortized
# - Hash Collision (Xung đột băm): Khi 2 key khác nhau có cùng hash value (Python giải quyết bằng Open Addressing)
my_map = {'A': 1, 'B': 2, 'C': 3}

# Thao tác cơ bản: Insert, Access, Update, Delete -> O(1)
my_map['D'] = 4                           # Insert O(1)
print("Lookup 'B' (O(1)):", my_map['B'])  # 2
del my_map['A']                           # Delete O(1)
print("'C' in map:", 'C' in my_map)       # True

# defaultdict: Tối ưu cấu trúc nhóm (Grouping) O(n) thời gian, O(1) amortized mỗi lookup/insert
# - Cơ chế: Khi key vắng mặt, tự động gọi factory function (list, int, set...) cấp phát bộ nhớ tại chỗ, tránh 2 lần lookup (kiểm tra `in` rồi mới gán)
group_by_len = defaultdict(list)
words = ["apple", "banana", "cherry", "fig", "pear"]
for word in words:
    group_by_len[len(word)].append(word)

print("defaultdict grouped by length:", dict(group_by_len))

# Counter: Tối ưu đếm tần suất bằng C-level Hash Table O(n)
# - Thuật toán tìm k phần tử phổ biến nhất `most_common(k)` dùng cấu trúc Min-Heap heapq ngầm định -> O(n log k) thay vì sort toàn bộ O(n log n)
letter_counts = Counter("abracadabra")
print("Counter frequencies:", letter_counts)
print("Top 2 most common (O(n log k) via heap):", letter_counts.most_common(2))


# 2. HASH SET (Set trong Python)
# - Tập hợp các phần tử đơn lẻ duy nhất (unique), không trùng lặp và không có thứ tự
# - Cài đặt bằng bảng băm chỉ lưu key (chỉ nhận các phần tử bất biến / hashable)
my_set = {1, 2, 3, 4}
my_set.add(5)                             # Add O(1)
my_set.remove(2)                          # Remove O(1)
print("5 in set (O(1)):", 5 in my_set)    # True

# Các phép toán đại số tập hợp tối ưu
s1, s2 = {1, 2, 3}, {3, 4, 5}
print("Union (|):", s1 | s2)              # {1, 2, 3, 4, 5}
print("Intersection (&):", s1 & s2)       # {3}
print("Difference (-):", s1 - s2)         # {1, 2}
