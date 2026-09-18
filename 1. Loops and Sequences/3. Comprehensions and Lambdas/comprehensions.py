# 1. List Comprehension cơ bản: [expression for item in iterable if condition]
# Tạo danh sách nhanh gọn trong 1 dòng thay vì tạo list rỗng và append trong vòng lặp for
even_numbers = [num for num in range(21) if num % 2 == 0]
print("Even numbers:", even_numbers)

# 2. List Comprehension với if - else (Ternary Operator):
# Cú pháp: [val_if_true if condition else val_if_false for item in iterable]
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print("Even or Odd result:", result)
# [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]

# 3. [MỞ RỘNG PYTHONIC]: Dict Comprehension & Set Comprehension
# Cùng nguyên lý với List Comprehension nhưng sinh ra Dict hoặc Set trực tiếp:

# - Dict Comprehension: {key_expr: value_expr for item in iterable}
names = ['Alice', 'Bob', 'Charlie']
name_lengths = {name: len(name) for name in names}
print("Dict Comprehension:", name_lengths) # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# - Set Comprehension: {expression for item in iterable} (Tự động loại bỏ trùng lặp)
duplicate_numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_squares = {x ** 2 for x in duplicate_numbers}
print("Set Comprehension:", unique_squares) # {1, 4, 9, 16, 25}

# 4. Hàm filter(func, iterable) - Lọc các phần tử thỏa mãn điều kiện trả về True
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print("filter() with function:", long_words) # ['mountain', 'river', 'cloud']

# 5. Hàm map(func, iterable) - Áp dụng hàm lên từng phần tử của iterable
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print("map() Celsius to Fahrenheit:", fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]

# 6. Hàm sum(iterable, [start=0]) - Tính tổng danh sách
sum_numbers = [5, 10, 15, 20]
total = sum(sum_numbers)
print("sum():", total)                           # 50

# start dưới dạng đối số vị trí (positional argument):
print("sum(numbers, 10):", sum(sum_numbers, 10)) # 60

# start dưới dạng đối số từ khóa (keyword argument - rõ ràng, minh bạch hơn):
print("sum(numbers, start=10):", sum(sum_numbers, start=10)) # 60

# 7. Hàm all() và any() - Kiểm tra điều kiện trên toàn bộ iterable
# - all(): Trả về True nếu TẤT CẢ phần tử đều là truthy
# - any(): Trả về True nếu CÓ ÍT NHẤT 1 phần tử là truthy
truthy = [1, 2, 3]
falsy = [0, 1, 2, 3]
print("all(truthy):", all(truthy))               # True
print("all(falsy):", all(falsy))                 # False (do số 0 là falsy)
print("any(falsy):", any(falsy))                 # True (do có 1, 2, 3 là truthy)
