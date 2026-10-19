# List Comprehension: cú pháp [biểu_thức for phần_tử in iterable if điều_kiện]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Lọc phần tử có chứa chữ 'a':
filtered = [x for x in fruits if "a" in x]
print("Filtered with 'a':", filtered)

# Biến đổi giá trị:
print("Upper fruits:", [x.upper() for x in fruits])

# Kết hợp if-else:
replaced = [x if x != "banana" else "orange" for x in fruits]
print("Replaced banana:", replaced)

# Toán tử Walrus (:=) để tránh tính toán 2 lần:
words = ["python", "ast", "ai", "code"]
long_words = [(w, length) for w in words if (length := len(w)) > 3]
print("Long words with Walrus:", long_words)

# Làm phẳng danh sách 2D (Nested List Comprehension):
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [val for row in matrix for val in row]
print("Flattened matrix:", flattened)

# Generator Expression: dùng ngoặc tròn (), tính toán lười (lazy) tiết kiệm bộ nhớ:
numbers = [1, 2, 3, 4, 5]
gen_squares = (x ** 2 for x in numbers)
print("Generator sum:", sum(gen_squares))

# Hàm ẩn danh Lambda: lambda tham_số: biểu_thức
square = lambda x: x ** 2
print("Lambda square(4):", square(4))

# Thường dùng làm key sắp xếp:
pairs = [(1, "one"), (3, "three"), (2, "two")]
print("Sorted by key:", sorted(pairs, key=lambda item: item[1]))

# all() và any():
# all(): True nếu TẤT CẢ phần tử đều True
# any(): True nếu CÓ ÍT NHẤT MỘT phần tử True
print("all([1, 2, 3]):", all([1, 2, 3]))
print("all([0, 1, 2]):", all([0, 1, 2]))
print("any([0, 1, 2]):", any([0, 1, 2]))
