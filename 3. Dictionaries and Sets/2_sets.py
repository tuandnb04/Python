# Tập hợp (Sets) trong Python là cấu trúc dữ liệu tích hợp sẵn
# Các phần tử là DUY NHẤT (Unique) và KHÔNG CÓ THỨ TỰ (Unordered)

# 1. Khởi tạo Set
my_set = {1, 2, 3, 4, 5}
empty_set = set()  # Bắt buộc dùng set() để tạo set rỗng (dùng {} sẽ tạo dict rỗng)

# 2. Thêm và Xóa phần tử
my_set.add(6)
my_set.add(5)  # Không thay đổi vì 5 đã tồn tại
print("Sau khi add:", my_set)  # {1, 2, 3, 4, 5, 6}

# Xóa phần tử: .remove() (báo lỗi KeyError nếu không thấy) vs .discard() (an toàn, không báo lỗi)
my_set.remove(4)
my_set.discard(10)  # 10 không có trong set nhưng không bị lỗi

# 3. Kiểm tra phần tử tồn tại với toán tử 'in'
print(5 in my_set)  # True

# 4. Kiểm tra quan hệ giữa các tập hợp
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

print("issubset:", your_set.issubset(my_set))      # False (your_set có là tập con của my_set không)
print("issuperset:", my_set.issuperset(your_set))  # False (my_set có là tập cha của your_set không)
print("isdisjoint:", my_set.isdisjoint(your_set))  # False (2 tập có rời nhau hoàn toàn không)

# 5. Các phép toán tập hợp (Mathematical Set Operations)
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

# 6. Kiến thức mở rộng: Đếm tần suất với collections.Counter
from collections import Counter

numbers = [1, 3, 4, 2, 2, 5, 3, 3, 1]

# Counter đếm số lần xuất hiện của từng phần tử (trả về dict-like object)
counts = Counter(numbers)  # Counter({3: 3, 1: 2, 2: 2, 4: 1, 5: 1})

# Lấy các phần tử trùng lặp (> 1 lần)
duplicates = [num for num, count in counts.items() if count > 1]
print("Duplicates (Counter):", sorted(duplicates))  # [1, 2, 3]

# Top 2 phần tử xuất hiện nhiều nhất:
print("Top 2 most common:", counts.most_common(2))  # [(3, 3), (1, 2)]


