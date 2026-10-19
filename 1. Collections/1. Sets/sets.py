# Set: tập hợp không thứ tự, không đánh chỉ mục, không chứa phần tử trùng lặp

# 1. Khai báo:
# Set được tạo bằng cặp ngoặc nhọn {}, không có thứ tự và không chứa phần tử trùng lặp:
colors = {"red", "green", "blue"}
print("Colors set:", colors)

# Phần tử trùng lặp tự động bị loại bỏ:
s = {1, 2, 2, 3}
print("Duplicates removed:", s)  # {1, 2, 3}

# Set không có chỉ mục (truy cập s[0] sẽ lỗi TypeError).
# Khởi tạo set rỗng bắt buộc dùng set() (dùng {} sẽ tạo dict rỗng):
empty_set = set()
print("True and 1 duplicate:", {True, 1, False, 0})

# 2. Thêm phần tử (.add, .update):
colors = {"red", "blue"}
colors.add("yellow")             # Thêm 1 phần tử
colors.add("red")                # Nếu đã tồn tại: không báo lỗi, không bị trùng lặp
print("After add:", colors)

# update() thêm nhiều phần tử từ bất kỳ iterable nào (list, tuple, set):
colors.update(["pink", "gray"])
print("After update:", colors)

# 3. Xóa phần tử (.remove, .discard, .pop):
colors.remove("blue")            # Xóa phần tử chỉ định (ném lỗi KeyError nếu không tìm thấy)
colors.discard("unknown")        # Xóa an toàn: không làm gì nếu không tìm thấy (không báo lỗi)
popped = colors.pop()            # Xóa và trả về 1 phần tử ngẫu nhiên (do set không có thứ tự)
print("Popped item:", popped)
print("Remaining colors:", colors)

# 4. Duyệt qua Set và kiểm tra tồn tại (toán tử in):
# Duyệt bằng vòng lặp for: không đảm bảo thứ tự, nhưng mỗi phần tử chỉ xuất hiện đúng 1 lần:
for color in colors:
    print("Color item:", color)

# Kiểm tra tồn tại bằng 'in' đạt tốc độ O(1) cực nhanh (nhanh hơn rất nhiều so với List O(n)):
print("'yellow' in colors:", "yellow" in colors)

# 5. Các phép toán đại số tập hợp (Phương thức & Toán tử tương đương):
a = {1, 2, 3}
b = {2, 3, 4}

# Hợp (Union / |): lấy toàn bộ phần tử từ cả hai set:
print("Union (a | b):", a | b)  # {1, 2, 3, 4} (tương đương a.union(b))

# Giao (Intersection / &): chỉ lấy phần tử xuất hiện ở cả hai set:
print("Intersection (a & b):", a & b)  # {2, 3} (tương đương a.intersection(b))

# Hiệu (Difference / -): phần tử có trong set thứ nhất nhưng KHÔNG có trong set thứ hai:
print("Difference (a - b):", a - b)  # {1}
print("Difference (b - a):", b - a)  # {4} (thứ tự quyết định kết quả)

# Hiệu đối xứng (Symmetric Difference / ^): phần tử chỉ xuất hiện ở 1 trong 2 set:
print("Symmetric diff (a ^ b):", a ^ b)  # {1, 4} (tương đương a.symmetric_difference(b))

# Kiểm tra tập con (Subset / <=):
print("Subset (a <= b):", a <= b)  # False

# 6. frozenset: tập hợp bất biến, dùng được làm Key trong Dict hoặc phần tử của Set:
frozen = frozenset(["read", "write"])
roles = {frozen: "Editor"}
print("Frozenset key role:", roles[frozen])

# 7. Ứng dụng phổ biến: loại bỏ phần tử trùng lặp trong list:
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
