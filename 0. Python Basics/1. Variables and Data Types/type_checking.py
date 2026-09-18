# Kiểm tra kiểu dữ liệu với hàm type() và isinstance() (Không cần import)

# Hàm type(): Trả về kiểu dữ liệu cụ thể của đối tượng
# Lưu ý: type() nhận 1 đối số (hoặc 3 đối số khi tạo class động).
developer = 'Devin'
print("type(developer):", type(developer))           # <class 'str'>

my_integer_var = 10
my_float_var = 4.50
my_string_var = 'hello'
my_boolean_var = True

print("type(my_integer_var):", type(my_integer_var)) # <class 'int'>
print("type(my_float_var):", type(my_float_var))     # <class 'float'>
print("type(my_string_var):", type(my_string_var))   # <class 'str'>
print("type(my_boolean_var):", type(my_boolean_var)) # <class 'bool'>

# Vì sao cần kiểm tra kiểu dữ liệu:
# Biến chứa chuỗi ký tự '12' không thể thực hiện phép chia toán học / 2.
# Cần xác thực kiểu dữ liệu trước khi thực hiện các phép toán:
account_balance: object = '12'

# Hàm isinstance(): Kiểm tra biến có khớp với kiểu dữ liệu hay không (trả về bool)
print("isinstance(account_balance, int):", isinstance(account_balance, int)) # False

# Kiểm tra nhiều kiểu dữ liệu với toán tử '|':
valid_balance: object = 12
print("isinstance(valid_balance, int | float):", isinstance(valid_balance, int | float)) # True

# Kiểm tra trường tùy chọn (Cho phép kiểu dữ liệu hoặc None):
diagnosis: object = None
print("isinstance(diagnosis, str | None):", isinstance(diagnosis, str | None))           # True

# Cạm bẫy kế thừa bool từ int:
# Trong Python, bool là lớp con của int, do đó isinstance(True, int) trả về True.
# Sử dụng 'type(val) is bool' để kiểm tra chính xác danh tính lớp:
print("isinstance(True, int):", isinstance(True, int)) # True (Cạm bẫy kế thừa!)
print("type(True) is bool:", type(True) is bool)       # True (Kiểm tra chính xác danh tính lớp)
