# Tập hợp (Sets) trong Python là cấu trúc dữ liệu tích hợp sẵn
# Các phần tử là DUY NHẤT (Unique) và KHÔNG CÓ THỨ TỰ (Unordered)

# Khởi tạo Set
my_set = {1, 2, 3, 4, 5}
empty_set: set[int] = set()  # Bắt buộc dùng set() để tạo set rỗng (dùng {} sẽ tạo dict rỗng)

# Thêm và Xóa phần tử
my_set.add(6)
my_set.add(5)  # Không thay đổi vì 5 đã tồn tại
print("Sau khi add:", my_set)  # {1, 2, 3, 4, 5, 6}

# Xóa phần tử:
# - .remove(): Xóa giá trị, báo lỗi KeyError nếu không tìm thấy
# - .discard(): Xóa an toàn, không báo lỗi nếu giá trị không tồn tại
# - .pop(): Lấy và xóa một phần tử ngẫu nhiên/tùy ý (báo KeyError nếu set rỗng)
my_set.remove(4)
my_set.discard(10)  # 10 không có trong set nhưng không bị lỗi
popped_elem = my_set.pop()
print("Popped element (.pop()):", popped_elem)

# Kiểm tra phần tử tồn tại với toán tử 'in' (thời gian trung bình O(1))
print(5 in my_set)

# Kiểm tra quan hệ giữa các tập hợp
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print("issubset:", your_set.issubset(my_set))      # False (your_set có là tập con của my_set không)
print("issuperset:", my_set.issuperset(your_set))  # False (my_set có là tập cha của your_set không)
print("isdisjoint:", my_set.isdisjoint(your_set))  # False (2 tập có rời nhau hoàn toàn không)

# Các phép toán tập hợp (Mathematical Set Operations)
# Hỗ trợ cả toán tử (operators) và phương thức (methods) tương ứng:
# 1. Union (| hoặc .union()): Hợp - Lấy tất cả phần tử từ cả 2 tập hợp
print("Union (|):", my_set | your_set)                       # {1, 2, 3, 4, 5, 6}
print("Union (.union()):", my_set.union(your_set))

# 2. Intersection (& hoặc .intersection()): Giao - Chỉ lấy các phần tử chung
print("Intersection (&):", my_set & your_set)               # {2, 3, 4}
print("Intersection (.intersection()):", my_set.intersection(your_set))

# 3. Difference (- hoặc .difference()): Hiệu - Lấy phần tử thuộc my_set nhưng KHÔNG thuộc your_set
print("Difference (-):", my_set - your_set)                 # {1, 5}
print("Difference (.difference()):", my_set.difference(your_set))

# 4. Symmetric Difference (^ hoặc .symmetric_difference()): Hiệu đối xứng - Thuộc một trong hai tập nhưng không thuộc cả hai
print("Symmetric Diff (^):", my_set ^ your_set)             # {1, 5, 6}
print("Symmetric Diff (.symmetric_difference()):", my_set.symmetric_difference(your_set))

# Toán tử gán kết hợp (Compound assignment): |=, &=, -=, ^=
my_set -= your_set  # Cập nhật trực tiếp my_set = my_set - your_set
print("my_set sau khi -= :", my_set)  # {1, 5}

# .clear() - Xóa toàn bộ phần tử
my_set.clear()
print("After clear():", my_set)  # set()

# Thuật toán: Tìm phần tử trùng lặp với Set trong O(n) Time & O(n) Space
# Tận dụng tra cứu O(1) của Set thay vì quét danh sách O(n^2):

numbers = [1, 3, 4, 2, 2, 5, 3, 3, 1]

seen = set()
duplicates = set()
for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates found via Set:", sorted(duplicates))  # [1, 2, 3]

# Kỹ thuật Đếm số phần tử thỏa điều kiện (Pythonic Counting với sum):
# - Tận dụng True == 1, False == 0 và Generator Expression để đếm cực nhanh không tốn RAM.
# - Ví dụ: Đếm số lượng ký tự xuất hiện > 1 lần trong văn bản (không phân biệt hoa thường):
text_sample = "Indivisibility"
s_lower = text_sample.lower()
dup_count = sum(s_lower.count(char) > 1 for char in set(s_lower))
print(f"Duplicates count in '{text_sample}':", dup_count)  # 1 ('i' occurs 6 times)

# Set Comprehension: {expression for item in iterable} (Tự động loại bỏ trùng lặp)
duplicate_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_squares = {x ** 2 for x in duplicate_numbers}
print("Set Comprehension:", sorted(unique_squares))  # [1, 4, 9, 16, 25]

