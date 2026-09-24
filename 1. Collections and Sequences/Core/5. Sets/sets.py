# Tập hợp (Sets) trong Python là cấu trúc dữ liệu tích hợp sẵn
# Các phần tử là DUY NHẤT (Unique) và KHÔNG CÓ THỨ TỰ (Unordered)

# Khởi tạo Set
my_set = {1, 2, 3, 4, 5}
empty_set: set[int] = set()  # Bắt buộc dùng set() để tạo set rỗng (dùng {} sẽ tạo dict rỗng)

# Thêm và Xóa phần tử
my_set.add(6)
my_set.add(5)  # Không thay đổi vì 5 đã tồn tại
print("Sau khi add:", my_set)  # {1, 2, 3, 4, 5, 6}

# Xóa phần tử: .remove() (báo lỗi KeyError nếu không thấy) vs .discard() (an toàn, không báo lỗi)
my_set.remove(4)
my_set.discard(10)  # 10 không có trong set nhưng không bị lỗi

# Kiểm tra phần tử tồn tại với toán tử 'in'
print(5 in my_set)  # True

# Kiểm tra quan hệ giữa các tập hợp
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print("issubset:", your_set.issubset(my_set))      # False (your_set có là tập con của my_set không)
print("issuperset:", my_set.issuperset(your_set))  # False (my_set có là tập cha của your_set không)
print("isdisjoint:", my_set.isdisjoint(your_set))  # False (2 tập có rời nhau hoàn toàn không)

# Các phép toán tập hợp (Mathematical Set Operations)
# Union (|) - Hợp: Lấy tất cả phần tử từ cả 2 tập hợp
print("Union (|):", my_set | your_set)  # {1, 2, 3, 4, 5, 6}

# Intersection (&) - Giao: Chỉ lấy các phần tử chung
print("Intersection (&):", my_set & your_set)  # {2, 3, 4}

# Difference (-) - Hiệu: Lấy phần tử thuộc my_set nhưng KHÔNG thuộc your_set
print("Difference (-):", my_set - your_set)  # {1, 5}

# Symmetric Difference (^) - Hiệu đối xứng: Thuộc tập này hoặc tập kia nhưng KHÔNG thuộc cả hai
print("Symmetric Diff (^):", my_set ^ your_set)  # {1, 5, 6}

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





