from typing import TypeIs

# Kiểm tra kiểu dữ liệu với type() và isinstance()
developer = 'Devin'
raw_balance: object = '12'

# Hàm type(): Trả về kiểu dữ liệu cụ thể của một đối tượng
# Lưu ý: type() nhận 1 đối số (hoặc 3 đối số khi tạo class động), gọi không tham số sẽ gây TypeError.
print("type(developer):", type(developer))                   # <class 'str'>
print(type(10), type(4.50), type(True), type(None))         # <class 'int'> <class 'float'> <class 'bool'> <class 'NoneType'>

# Kiểm tra kiểu dữ liệu trước khi tính toán để tránh ngoại lệ runtime:
try:
    if not isinstance(raw_balance, int | float):
        raise TypeError(f"unsupported operand type(s) for /: '{type(raw_balance).__name__}' and 'int'")
    _ = raw_balance / 2
except TypeError as err:
    print("Caught expected TypeError:", err)

# Hàm isinstance(): Kiểm tra đối tượng có khớp với kiểu dữ liệu hay không (trả về bool)
print("isinstance(raw_balance, int):", isinstance(raw_balance, int)) # False

# Kiểm tra nhiều kiểu dữ liệu bằng toán tử Union '|' (Python 3.10+ PEP 604):
sample_data: object = 12
print("isinstance with union (int | float):", isinstance(sample_data, int | float))   # True

# Kiểm tra trường tùy chọn (Cho phép kiểu dữ liệu hoặc None với PEP 604):
optional_value: object = None
print("Optional field (str | None):", isinstance(optional_value, str | None))        # True

# Cạm bẫy kế thừa bool từ int:
# - Trong Python, bool là lớp con của int (issubclass(bool, int) == True).
# - Do đó, isinstance(True, int) trả về True:
print("isinstance(True, int):", isinstance(True, int))           # True (Cạm bẫy kế thừa!)
print("type(True) is bool:", type(True) is bool)                 # True (Kiểm tra chính xác danh tính lớp)

# Định nghĩa Type Alias (Python 3.12+ PEP 695) & Type Narrowing với TypeIs (Python 3.13+ PEP 742):
# Hàm type guard chuẩn xác, loại trừ bool và thu hẹp kiểu cho Type Checker:
type Numeric = int | float

def is_numeric(value: object) -> TypeIs[Numeric]:
    return isinstance(value, int | float) and not isinstance(value, bool)

test_val: object = True
print("is_numeric(True):", is_numeric(test_val))                 # False
print("is_numeric(42):", is_numeric(42))                         # True

# Chú thích kiểu dữ liệu cho biến (Type Annotations / Type Hints):
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
