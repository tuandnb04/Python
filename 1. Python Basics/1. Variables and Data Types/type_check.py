# 1. Hàm type() - Kiểm tra kiểu dữ liệu của biến
name = 'Devin'
print(type(name))                       # <class 'str'>
print(type(10), type(3.14), type(None)) # <class 'int'> <class 'float'> <class 'NoneType'>

# 2. Hàm isinstance() - Kiểm tra biến có khớp với kiểu dữ liệu hay không (trả về bool)
balance = 12
print(isinstance(balance, int))         # True
print(isinstance(balance, str))         # False

# 3. Kiểm tra biến khớp với một trong nhiều kiểu bằng toán tử '|'
# Cú pháp ngắn gọn, trực quan, không cần khởi tạo tuple trong bộ nhớ:
print("Check balance (int | float):", isinstance(balance, int | float)) # True

# Kiểm tra trường tùy chọn (cho phép kiểu dữ liệu hoặc None):
diagnosis = None
print("Optional field (str | None):", isinstance(diagnosis, str | type(None))) # True

# 4. Cạm bẫy bool là lớp con của int & Tối ưu hiệu năng ở tầng C:
# - isinstance(True, int) sẽ trả về True (do issubclass(bool, int) == True).
# => Dùng 'type(x) in (int, float)' nhanh hơn và loại trừ được bool:
print("isinstance(True, int):", isinstance(True, int))           # True (Cạm bẫy!)
print("type(True) in (int, float):", type(True) in (int, float)) # False (Chính xác & Nhanh hơn)