# Khai báo biến
user_name = 'John Doe'
user_age = 25
total_score = 100

# Quy tắc: Bắt đầu bằng chữ cái/gạch dưới (không bắt đầu bằng số), case-sensitive, không trùng từ khóa
# Quy ước: Dùng snake_case, đặt tên có ý nghĩa (tránh tên 1 ký tự như x = 56)
# Comment: Dùng '#' cho comment đơn dòng hoặc nhiều dòng liên tiếp

# Hàm print(): Chuỗi dùng '...' hoặc "...", dấu phẩy tự chèn khoảng trắng
print('Hello world!')
print('Hello', 'world!')                                # Hello world!
print('My favorite colors are', 'blue', 'green', 'red') # My favorite colors are blue green red
print('User info:', user_name, user_age, total_score)

# Dynamic typing: Tự nhận diện kiểu, có thể gán lại bằng kiểu khác
age = 25
print('Initial age:', age)

age = 'Twenty-five'
print('Reassigned age:', age)

# Các kiểu dữ liệu cơ bản
my_integer_var = 10          # int: số nguyên
my_float_var = 4.50          # float: số thực
my_string_var = 'hello'      # str: chuỗi
my_boolean_var = True        # bool: True / False
empty_val = None             # NoneType: rỗng

print('Integer:', my_integer_var)
print('Float:', my_float_var)
print('String:', my_string_var)
print('Boolean:', my_boolean_var)
print('None:', empty_val)

# Hàm type(): Xem kiểu dữ liệu của biến
developer = 'Devin'
print(type(developer))       # <class 'str'>
print(type(my_integer_var))  # <class 'int'>
print(type(my_float_var))    # <class 'float'>
print(type(my_string_var))   # <class 'str'>
print(type(my_boolean_var))  # <class 'bool'>

# Chuỗi '12' không chia được cho 2 (gây TypeError), cần kiểm tra kiểu trước:
account_balance = '12'

# Hàm isinstance(): Kiểm tra kiểu dữ liệu (trả về bool)
print(isinstance(account_balance, int)) # False

# Kiểm tra nhiều kiểu với toán tử '|' (int hoặc float)
account_balance = 12
print(isinstance(account_balance, int | float)) # True