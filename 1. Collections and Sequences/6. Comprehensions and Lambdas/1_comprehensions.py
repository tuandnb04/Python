# 1. List Comprehension cơ bản & So sánh với vòng lặp truyền thống:
# Cú pháp tổng quát: newlist = [expression for item in iterable if condition]
# - Thay vì phải tạo danh sách rỗng và dùng vòng lặp for kết hợp .append():
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# Cách truyền thống (Traditional for-loop):
filtered_traditional = []
for x in fruits:
    if "a" in x:
        filtered_traditional.append(x)
print("Traditional filter:    ", filtered_traditional)

# Cách dùng List Comprehension (Ngắn gọn trên 1 dòng, tối ưu opcode C):
filtered_comp = [x for x in fruits if "a" in x]
print("List Comprehension:    ", filtered_comp)

# 2. Bóc tách 3 thành phần trong List Comprehension:
# a) Condition (Bộ lọc tùy chọn ở cuối):
no_apple = [x for x in fruits if x != "apple"]
print("Filter (x != 'apple'): ", no_apple)

# b) Iterable (Bất kỳ đối tượng duyệt được nào, ví dụ range):
less_than_five = [x for x in range(10) if x < 5]
print("Range iterable (< 5):  ", less_than_five)  # [0, 1, 2, 3, 4]

# c) Expression (Biểu thức kết quả ở đầu - có thể biến đổi giá trị):
upper_fruits = [x.upper() for x in fruits]
print("Manipulate (.upper()): ", upper_fruits)

constant_list = ['hello' for x in fruits]
print("Constant expression:   ", constant_list)

# Expression kết hợp biểu thức điều kiện if-else (Ternary Operator ở đầu):
# Cú pháp: [val_if_true if condition else val_if_false for item in iterable]
# "Nếu là 'banana' thì đổi thành 'orange', ngược lại giữ nguyên"
replaced_banana = [x if x != "banana" else "orange" for x in fruits]
print("Ternary in expression: ", replaced_banana)

even_numbers = [num for num in range(21) if num % 2 == 0]
print("Even numbers:          ", even_numbers)

# List Comprehension phân loại chẵn / lẻ:
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print("Even or Odd result:    ", result)
# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# Toán tử Walrus (:=) trong List Comprehension:
# Vừa gán giá trị vừa kiểm tra điều kiện để tránh phải gọi hàm/tính toán 2 lần (ví dụ: len(w)):
words_sample = ["python", "ast", "codegraph", "ai"]
word_lengths = [(w, length) for w in words_sample if (length := len(w)) > 3]
print("Walrus in List Comp:", word_lengths)  # [('python', 6), ('codegraph', 9)]

# Nested List Comprehension & Generator Expression:
# 1. Nested List Comprehension: Làm phẳng danh sách lồng nhau (Flattening)
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [val for row in matrix for val in row]
print("Flattened matrix:", flattened)  # [1, 2, 3, 4, 5, 6]

# 2. Generator Expression: (expression for item in iterable)
# Sinh dữ liệu lười (Lazy Evaluation), không tạo cả danh sách trong RAM như List Comp:
sample_numbers = [1, 2, 3, 4, 5]
gen_squares = (x ** 2 for x in sample_numbers)
print("Generator Object:", gen_squares)  # <generator object ...>
print("Generator Sum:", sum(gen_squares))  # 55
print("Join with Generator:", "-".join(str(x) for x in range(5)))  # '0-1-2-3-4'

# Hàm filter(func, iterable) - Lọc các phần tử thỏa mãn điều kiện trả về True
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']


def is_long_word(word):
    return len(word) > 4


long_words = list(filter(is_long_word, words))
print("filter() with function:", long_words)  # ['mountain', 'river', 'cloud']

# Hàm map(func, *iterables) - Áp dụng hàm lên từng phần tử của iterable
# 1. Ép kiểu dữ liệu nhanh hàng loạt (viết bằng C nên rất tối ưu):
numbers = [1, 2, 3, 4]
strings = list(map(str, numbers))
print("map(str):", strings)  # ['1', '2', '3', '4']

# 2. Biến đổi dữ liệu với hàm tự định nghĩa hoặc lambda:
celsius = [0, 10, 20, 30, 40]


def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


fahrenheit = list(map(to_fahrenheit, celsius))
print("map() Celsius to Fahrenheit:", fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# 3. Áp dụng cùng lúc nhiều mảng (dừng ở mảng ngắn nhất, tương tự zip):
a = [1, 2, 3]
b = [10, 20, 30]
total = list(map(lambda x, y: x + y, a, b))
print("map multiple lists:", total)  # [11, 22, 33]

# 4. Cơ chế "Lazy Evaluation" (Đánh giá lười):
# map() trả về một map object (iterator), chỉ tính toán khi duyệt qua giúp tiết kiệm bộ nhớ RAM
lazy_res = map(str, numbers)
print("Lazy map object:", lazy_res)  # <map object at 0x...>
print("Evaluated list:", list(lazy_res))  # ['1', '2', '3', '4']

# 5. So sánh với List Comprehension:
# - map(): Ngắn gọn, chạy nhanh nhất với hàm có sẵn như map(int, arr), map(str, arr)
# - List Comp [f(x) for x in arr]: Dễ đọc hơn khi có logic tính toán phức tạp hoặc lọc điều kiện if/else


# Hàm sum(iterable, [start=0]) - Tính tổng danh sách
sum_numbers = [5, 10, 15, 20]
total = sum(sum_numbers)
print("sum():", total)  # 50

# start dưới dạng đối số vị trí (positional argument):
print("sum(numbers, 10):", sum(sum_numbers, 10))  # 60

# start dưới dạng đối số từ khóa (keyword argument - rõ ràng, minh bạch hơn):
print("sum(numbers, start=10):", sum(sum_numbers, start=10))  # 60

# Hàm all() và any() - Kiểm tra điều kiện trên toàn bộ iterable
# - all(): Trả về True nếu TẤT CẢ phần tử đều là truthy
# - any(): Trả về True nếu CÓ ÍT NHẤT 1 phần tử là truthy
truthy = [1, 2, 3]
falsy = [0, 1, 2, 3]
print("all(truthy):", all(truthy))  # True
print("all(falsy):", all(falsy))  # False (do số 0 là falsy)
print("any(falsy):", any(falsy))  # True (do có 1, 2, 3 là truthy)

# Ví dụ: List Comprehension kết hợp Ternary Operator và Tuple Unpacking
# CPython dùng opcode LIST_APPEND ở cấp độ C, tối ưu hơn for-loop và append() thủ công:
data_pairs = [(18, 20), (45, 2), (61, 12), (37, 6), (78, 9)]
categories = ["High" if val1 >= 55 and val2 > 7 else "Low" for val1, val2 in data_pairs]
print("List comp with unpacking:", categories)  # ['Low', 'Low', 'High', 'Low', 'High']
