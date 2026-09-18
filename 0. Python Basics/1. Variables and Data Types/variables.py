# Khai báo biến (Toán tử gán '=')
user_name = 'John Doe'
user_age = 25
total_score = 100

# Quy tắc đặt tên biến (Rules):
# - Bắt đầu bằng chữ cái hoặc dấu gạch dưới (_), KHÔNG bắt đầu bằng số (ví dụ '5name' gây SyntaxError).
# - Chỉ chứa chữ cái (a-z, A-Z), chữ số (0-9) và dấu gạch dưới (_).
# - Phân biệt hoa/thường (Case-sensitive): age, Age, AGE là các biến hoàn toàn khác nhau.
# - Không trùng với từ khóa của Python (reserved keywords như: if, class, def, v.v.).

# Quy ước đặt tên (Conventions):
# - Dùng snake_case: các từ viết thường nối nhau bởi dấu gạch dưới (ví dụ: my_variable_name, user_age).
# - Đặt tên biến rõ nghĩa, tránh dùng tên 1 ký tự (như x = 56) vì không truyền tải được mục đích dữ liệu.

# Comments trong Python:
# - Dùng dấu '#' cho comment đơn dòng (Python sẽ bỏ qua toàn bộ phần sau dấu '#' trên dòng đó).
# - Comment nhiều dòng được tạo bằng nhiều dòng '#' liên tiếp.

# In dữ liệu ra màn hình terminal với hàm built-in print()
# - Dấu nháy đơn ('...') hoặc nháy kép ("...") định nghĩa chuỗi (string) làm đối số (argument).
# - Phân tách nhiều đối số bằng dấu phẩy, print() tự động chèn khoảng trắng ở giữa:
print('Hello world!')
print('Hello', 'world!')                                # In ra: Hello world!
print('My favorite colors are', 'blue', 'green', 'red') # In ra: My favorite colors are blue green red
print('User info:', user_name, user_age, total_score)

# Kiểu dữ liệu động (Dynamically-typed):
# - Python tự nhận diện kiểu dữ liệu dựa trên giá trị được gán (không cần chỉ định kiểu trước).
# - Biến có thể được gán lại bằng giá trị thuộc kiểu dữ liệu khác bất cứ lúc nào:
age = 25             # Ban đầu là kiểu int (số nguyên)
print('Initial age:', age)

age = 'Twenty-five'  # Gán lại giá trị kiểu str (chuỗi ký tự)
print('Reassigned age:', age)

# 4 kiểu dữ liệu cơ bản trong Python:
my_integer_var = 10          # Integer (Số nguyên không có phần thập phân: 10, -5)
my_float_var = 4.50          # Float (Số thực có phần thập phân: 4.50, -0.4)
my_string_var = 'hello'      # String (Chuỗi ký tự đặt trong cặp nháy đơn hoặc kép)
my_boolean_var = True        # Boolean (Kiểu logic chỉ nhận True hoặc False)
empty_val = None             # NoneType (Đại diện cho giá trị rỗng / không có)

print('Integer:', my_integer_var)
print('Float:', my_float_var)
print('String:', my_string_var)
print('Boolean:', my_boolean_var)
print('None:', empty_val)

# Kiểm tra kiểu dữ liệu với hàm type() và isinstance()

# Hàm type(): Trả về kiểu dữ liệu cụ thể của đối tượng
# Lưu ý: type() nhận 1 đối số (gọi không truyền đối số sẽ gây TypeError).
developer = 'Devin'
print(type(developer))       # <class 'str'>
print(type(my_integer_var))  # <class 'int'>
print(type(my_float_var))    # <class 'float'>
print(type(my_string_var))   # <class 'str'>
print(type(my_boolean_var))  # <class 'bool'>

# Vì sao cần kiểm tra kiểu dữ liệu trước khi thực hiện thao tác:
# Thao tác tính toán trên chuỗi '12' / 2 sẽ gây lỗi:
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
account_balance = '12'

# Hàm isinstance(): Kiểm tra biến có khớp với kiểu dữ liệu hay không (trả về bool)
print(isinstance(account_balance, int)) # False

# Kiểm tra nhiều kiểu dữ liệu với toán tử Union '|' (Chuẩn Python mới nhất):
account_balance = 12
print(isinstance(account_balance, int | float)) # True (nếu là 12 hoặc 12.0 đều trả về True)