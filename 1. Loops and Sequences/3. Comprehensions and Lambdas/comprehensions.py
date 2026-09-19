# List Comprehension cơ bản: [expression for item in iterable if condition]
# Tạo danh sách nhanh gọn trong 1 dòng thay vì tạo list rỗng và append trong vòng lặp for
even_numbers = [num for num in range(21) if num % 2 == 0]
print("Even numbers:", even_numbers)

# List Comprehension với if - else (Ternary Operator):
# Cú pháp: [val_if_true if condition else val_if_false for item in iterable]
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print("Even or Odd result:", result)
# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# [TỐI ƯU HIỆU NĂNG]: Toán tử gán Walrus (:=) trong List Comprehension (Python 3.8+)
# Vừa gán giá trị vừa kiểm tra điều kiện để tránh phải gọi hàm/tính toán 2 lần (ví dụ: len(w)):
words_sample = ["python", "ast", "codegraph", "ai"]
word_lengths = [(w, length) for w in words_sample if (length := len(w)) > 3]
print("Walrus in List Comp:", word_lengths) # [('python', 6), ('codegraph', 9)]


# [MỞ RỘNG PYTHONIC]: Dict, Set Comprehension & Generator Expression
# Cùng nguyên lý với List Comprehension nhưng sinh ra Dict, Set hoặc Generator:

# - Dict Comprehension: {key_expr: value_expr for item in iterable}
names = ['Alice', 'Bob', 'Charlie']
name_lengths = {name: len(name) for name in names}
print("Dict Comprehension:", name_lengths) # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# - Set Comprehension: {expression for item in iterable} (Tự động loại bỏ trùng lặp)
duplicate_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_squares = {x ** 2 for x in duplicate_numbers}
print("Set Comprehension:", unique_squares) # {1, 4, 9, 16, 25}

# - Generator Expression: (expression for item in iterable)
# Sinh dữ liệu lười (Lazy Evaluation), không tạo cả danh sách trong RAM như List Comp:
gen_squares = (x ** 2 for x in duplicate_numbers)
print("Generator Object:", gen_squares)                    # <generator object ...>
print("Generator Sum:", sum(gen_squares))                  # 47
print("Join with Generator:", "-".join(str(x) for x in range(5))) # '0-1-2-3-4'

# Hàm filter(func, iterable) - Lọc các phần tử thỏa mãn điều kiện trả về True
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print("filter() with function:", long_words) # ['mountain', 'river', 'cloud']

# Hàm map(func, *iterables) - Áp dụng hàm lên từng phần tử của iterable
# 1. Ép kiểu dữ liệu nhanh hàng loạt (viết bằng C nên rất tối ưu):
numbers = [1, 2, 3, 4]
strings = list(map(str, numbers))
print("map(str):", strings)                    # ['1', '2', '3', '4']

# 2. Biến đổi dữ liệu với hàm tự định nghĩa hoặc lambda:
celsius = [0, 10, 20, 30, 40]
def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print("map() Celsius to Fahrenheit:", fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# 3. Áp dụng cùng lúc nhiều mảng (dừng ở mảng ngắn nhất, tương tự zip):
a = [1, 2, 3]
b = [10, 20, 30]
total = list(map(lambda x, y: x + y, a, b))
print("map multiple lists:", total)            # [11, 22, 33]

# 4. Cơ chế "Lazy Evaluation" (Đánh giá lười):
# map() trả về một map object (iterator), chỉ tính toán khi duyệt qua giúp tiết kiệm bộ nhớ RAM
lazy_res = map(str, numbers)
print("Lazy map object:", lazy_res)            # <map object at 0x...>
print("Evaluated list:", list(lazy_res))       # ['1', '2', '3', '4']

# 5. So sánh với List Comprehension:
# - map(): Ngắn gọn, chạy nhanh nhất với hàm có sẵn như map(int, arr), map(str, arr)
# - List Comp [f(x) for x in arr]: Dễ đọc hơn khi có logic tính toán phức tạp hoặc lọc điều kiện if/else


# Hàm sum(iterable, [start=0]) - Tính tổng danh sách
sum_numbers = [5, 10, 15, 20]
total = sum(sum_numbers)
print("sum():", total)                           # 50

# start dưới dạng đối số vị trí (positional argument):
print("sum(numbers, 10):", sum(sum_numbers, 10)) # 60

# start dưới dạng đối số từ khóa (keyword argument - rõ ràng, minh bạch hơn):
print("sum(numbers, start=10):", sum(sum_numbers, start=10)) # 60

# Hàm all() và any() - Kiểm tra điều kiện trên toàn bộ iterable
# - all(): Trả về True nếu TẤT CẢ phần tử đều là truthy
# - any(): Trả về True nếu CÓ ÍT NHẤT 1 phần tử là truthy
truthy = [1, 2, 3]
falsy = [0, 1, 2, 3]
print("all(truthy):", all(truthy))               # True
print("all(falsy):", all(falsy))                 # False (do số 0 là falsy)
print("any(falsy):", any(falsy))                 # True (do có 1, 2, 3 là truthy)
