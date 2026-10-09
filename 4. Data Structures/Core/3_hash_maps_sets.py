from collections import defaultdict, Counter

# Khái niệm ADT (Abstract Data Type) & Map vs Hash Map:
# - ADT: Bản thiết kế logic định nghĩa thao tác và tính chất dữ liệu, tách biệt khỏi cách cài đặt.
# - Map (ADT): Tập hợp cặp key-value với key duy nhất (unique), value có thể trùng lặp.
# - Hash Map (Hash Table): Cấu trúc cài đặt cụ thể của Map ADT dùng hàm băm (Hash Function) ánh xạ Key -> Index trong mảng ngầm định.
# - Xung đột băm (Hash Collision):
#   + Chaining: Mỗi ô mảng (bucket) trỏ đến một Linked List lưu các phần tử trùng index.
#   + Open Addressing: Dò tìm ô trống kế tiếp trong mảng (Python dict/set dùng Open Addressing).
# - Độ phức tạp:
#   + Time: O(1) average cho insert/lookup/delete; O(n) worst case khi nhiều xung đột.
#   + Space: O(1) average; O(n) worst case khi đầy mảng cần cấp phát lại (Resizing / Rehashing).

# 1. HASH MAP (Dictionary trong Python)
my_map = {'A': 1, 'B': 2, 'C': 3}

# Thao tác cơ bản: Insert, Access, Update, Delete -> O(1) average
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
# - Set (ADT): Tập hợp các phần tử đơn lẻ duy nhất (unique), không trùng lặp, không thứ tự, kích thước động (dynamic).
# - Cài đặt vật lý: Dùng bảng băm chỉ lưu key (không có value), yêu cầu phần tử phải bất biến (hashable).
# - Độ phức tạp: Add/Remove/Membership test đạt O(1) trung bình, O(n) worst-case (do xung đột băm).
my_set = {1, 2, 3, 4}
my_set.add(5)                             # Add O(1) avg
my_set.remove(2)                          # Remove O(1) avg
print("5 in set (O(1)):", 5 in my_set)    # True

# Ghi chú: Chi tiết các phép toán đại số tập hợp (| Union, & Intersection, - Difference)
# tham khảo tại: 1. Collections and Sequences/Core/5. Sets/1_sets.py

