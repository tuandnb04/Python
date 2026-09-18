# Kiểm tra kiểu dữ liệu với hàm type() và isinstance()

# Hàm type(): Trả về kiểu dữ liệu cụ thể của đối tượng
# Lưu ý: type() nhận 1 đối số (gọi không truyền đối số sẽ gây TypeError).
developer = 'Devin'
print(type(developer))       # <class 'str'>

my_integer_var = 10
my_float_var = 4.50
my_string_var = 'hello'
my_boolean_var = True

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

# Kiểm tra nhiều kiểu dữ liệu cùng lúc (truyền tuple các kiểu):
account_balance = 12
print(isinstance(account_balance, (int, float))) # True (nếu là 12 hoặc 12.0 đều trả về True)
