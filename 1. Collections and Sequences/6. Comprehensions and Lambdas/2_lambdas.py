# Từ hàm chính quy (def) sang hàm ẩn danh (lambda)
# Hàm thông thường có tên:
def square(num):
    return num ** 2


print("Regular function:", square(4))  # 16

# Chuyển đổi thành Lambda: lambda arguments: expression (Không có tên hàm, tự động return)
square_lambda = lambda num: num ** 2
print("Lambda function:", square_lambda(4))  # 16

# Sử dụng Lambda trong Higher-Order Functions (filter, map, sorted)
numbers = [1, 2, 3, 4, 5]

# Lọc số chẵn với filter():
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("filter() with lambda:", even_numbers)  # [2, 4]

# Bình phương danh sách với map():
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("map() with lambda:", squared_numbers)  # [1, 4, 9, 16, 25]

# Truyền trực tiếp Unbound Method / Constructor vào map() (không cần lambda):
# Thay vì `map(lambda w: w.capitalize(), words)`, dùng thẳng `str.capitalize`
raw_words = ['hello', 'world', 'python']
capitalized = list(map(str.capitalize, raw_words))
print("map(str.capitalize):", capitalized)  # ['Hello', 'World', 'Python']

# Ép kiểu chuỗi số thành int hàng loạt:
str_nums = ['10', '20', '30']
parsed_nums = list(map(int, str_nums))
print("map(int):", parsed_nums)  # [10, 20, 30]

# Dùng làm key function ngắn gọn trong sorted():
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
print("sorted() with lambda key:", sorted(pairs, key=lambda item: item[1]))


# Khi logic phức tạp, ưu tiên dùng def thay vì lambda:
def calculate_expression(x):
    if x > 0:
        return x ** 2 + 2 * x - 1
    else:
        return x ** 3 - x + 4


print("calculate_expression(3):", calculate_expression(3))  # 14
