# Kiểm tra kiểu dữ liệu với type() và isinstance()
developer = 'Devin'
account_balance = '12'

# Hàm type(): Trả về kiểu dữ liệu cụ thể của một đối tượng
# Lưu ý: type() nhận 1 đối số (hoặc 3 đối số khi định nghĩa class động), gọi không tham số sẽ gây TypeError.
print("type(developer):", type(developer))                   # <class 'str'>
print(type(10), type(4.50), type(True), type(None))         # <class 'int'> <class 'float'> <class 'bool'> <class 'NoneType'>

# Vì sao cần kiểm tra kiểu dữ liệu trước khi tính toán?
# Ví dụ: account_balance / 2 sẽ gây lỗi "TypeError: unsupported operand type(s) for /: 'str' and 'int'"
try:
    _ = account_balance / 2
except TypeError as err:
    print("Caught TypeError:", err)

# Hàm isinstance(): Kiểm tra biến có khớp với kiểu dữ liệu hay không (trả về bool True/False)
print("isinstance(account_balance, int):", isinstance(account_balance, int)) # False

# Kiểm tra một trong nhiều kiểu dữ liệu:
# - Cú pháp truyền tuple (Truyền thống):
balance_num = 12
print("isinstance with tuple (int, float):", isinstance(balance_num, (int, float))) # True

# - Cú pháp toán tử '|' (Hiện đại, Python 3.10+):
print("isinstance with union (int | float):", isinstance(balance_num, int | float)) # True

# Kiểm tra trường tùy chọn (Cho phép kiểu dữ liệu hoặc None):
diagnosis = None
print("Optional field (str | None):", isinstance(diagnosis, str | type(None)))       # True

# Cạm bẫy bool kế thừa từ int:
# - isinstance(True, int) trả về True vì bool là lớp con của int (issubclass(bool, int) == True).
# - Dùng 'type(x) in (int, float)' để kiểm tra chính xác kiểu số và loại trừ bool:
print("isinstance(True, int):", isinstance(True, int))           # True (Cạm bẫy!)
print("type(True) in (int, float):", type(True) in (int, float)) # False (Chính xác & an toàn)

# Chú thích kiểu dữ liệu cho biến (Type Annotations / Type Hints)
# - Type hints giúp IDE autocomplete, linter (Mypy) bắt lỗi và tài liệu hóa mã nguồn.
# - Python KHÔNG ép kiểu hay báo lỗi ở runtime nếu gán sai kiểu với type hint.

user_name: str = "Alice"
user_age: int = 25
user_rating: float = 4.8
is_active: bool = True

# Khai báo kiểu trước khi gán giá trị:
user_id: int
user_id = 101

# Kiểu kết hợp nhiều loại dữ liệu (Union với toán tử '|'):
score: int | float = 95.5
score = 100

print("Annotated variables:", user_name, user_age, user_rating, is_active, user_id, score)
