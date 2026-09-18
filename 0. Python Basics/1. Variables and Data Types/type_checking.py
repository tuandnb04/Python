# Kiểm tra kiểu dữ liệu với type() và isinstance()
name = 'Devin'
balance = 12

# Hàm type(): Trả về kiểu dữ liệu chính xác của đối tượng
print("type(name):", type(name))                            # <class 'str'>
print(type(10), type(3.14), type(None))                     # <class 'int'> <class 'float'> <class 'NoneType'>

# Hàm isinstance(): Kiểm tra đối tượng có thuộc kiểu chỉ định hay không (hỗ trợ kế thừa)
print("isinstance(balance, int):", isinstance(balance, int)) # True
print("isinstance(balance, str):", isinstance(balance, str)) # False

# Kiểm tra nhiều kiểu bằng toán tử '|' (Python 3.10+)
print("Check balance (int | float):", isinstance(balance, int | float)) # True

# Kiểm tra trường tùy chọn (Cho phép kiểu dữ liệu hoặc None)
diagnosis = None
print("Optional field (str | None):", isinstance(diagnosis, str | type(None))) # True

# Cạm bẫy bool là lớp con của int:
# - isinstance(True, int) trả về True do issubclass(bool, int) == True.
# - Dùng 'type(x) in (int, float)' để kiểm tra chính xác và loại trừ bool:
print("isinstance(True, int):", isinstance(True, int))           # True (Cạm bẫy!)
print("type(True) in (int, float):", type(True) in (int, float)) # False (Chính xác)

# Chú thích kiểu dữ liệu cho biến (Type Annotations / Type Hints)
# Lưu ý: Type hints dùng để tài liệu hóa code và hỗ trợ IDE/linter, Python không ép kiểu ở runtime.

user_name: str = "Alice"
user_age: int = 25
user_rating: float = 4.8
is_active: bool = True

# Khai báo kiểu trước khi gán giá trị
user_id: int
user_id = 101

# Kiểu kết hợp (Union với toán tử '|')
score: int | float = 95.5
score = 100

print("Annotated variables:", user_name, user_age, user_rating, is_active, user_id, score)
