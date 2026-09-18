from operator import itemgetter

# Từ hàm chính quy (def) sang hàm ẩn danh (lambda)
# Hàm thông thường có tên:
def square(num):
    return num ** 2

print("Regular function:", square(4)) # 16

# Chuyển đổi thành Lambda: lambda arguments: expression (Không có tên hàm, tự động return)
square_lambda = lambda num: num ** 2
print("Lambda function:", square_lambda(4)) # 16

# Sử dụng Lambda trong Higher-Order Functions (filter, map, sorted)
numbers = [1, 2, 3, 4, 5]

# Lọc số chẵn với filter():
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("filter() with lambda:", even_numbers)  # [2, 4]

# Bình phương danh sách với map():
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("map() with lambda:", squared_numbers)  # [1, 4, 9, 16, 25]

# Dùng làm key function ngắn gọn trong sorted():
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
print("sorted() with lambda key:", sorted(pairs, key=lambda item: item[1]))

# [CÁCH LÀM TỐT HƠN VỚI OPERATOR]: operator.itemgetter
# Thay vì viết `lambda x: x[1]`, dùng `itemgetter(1)` nhanh hơn (viết bằng C) và chuẩn Pythonic hơn
print("sorted() with itemgetter: ", sorted(pairs, key=itemgetter(1)))

# Best Practices khi dùng Lambda (Quy tắc thực hành chuẩn PEP 8)
# - KHÔNG NÊN: Gán lambda vào một biến (square = lambda x: x ** 2).
#   Lý do: Làm mất đi ý nghĩa của "hàm ẩn danh" (anonymous). Khi cần hàm có tên tái sử dụng, hãy dùng 'def'.
# - KHÔNG NÊN: Viết lambda quá phức tạp, lồng if/else nhiều nhánh.
#   Ví dụ xấu: (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3) -> Khó đọc và khó bảo trì!

# Cách viết chuẩn khi logic phức tạp: Tách thành hàm có tên rõ ràng
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print("calculate_expression(3):", calculate_expression(3)) # 14

# So sánh với List Comprehension hiện đại:
# - Trong Python hiện đại, List Comprehension thường được ưu tiên hơn map/filter + lambda:
even_comp = [x for x in numbers if x % 2 == 0]
squared_comp = [x ** 2 for x in numbers]
# Lí do: Hiệu năng cao hơn ở cấp độ C (không tốn chi phí function call overhead) và cú pháp Pythonic hơn.
