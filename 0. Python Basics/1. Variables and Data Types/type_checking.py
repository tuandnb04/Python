# Kiểm tra kiểu dữ liệu với hàm type() và isinstance()

# Hàm type(): Xem kiểu dữ liệu của biến
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

# Vì sao cần kiểm tra kiểu dữ liệu:
# Biến chứa chuỗi ký tự '12' không thể thực hiện phép chia toán học / 2.
account_balance = '12'

# Hàm isinstance(): Kiểm tra biến có khớp với kiểu dữ liệu hay không (trả về bool)
print(isinstance(account_balance, int)) # False

# Kiểm tra biến khớp với một kiểu dữ liệu cụ thể:
account_balance = 12
print(isinstance(account_balance, str))  # False
