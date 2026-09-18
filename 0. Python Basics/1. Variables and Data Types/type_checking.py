try:
    from typing import TypeIs
except ImportError:
    # Fallback cho các phiên bản Python trước 3.13 (cần pip install typing_extensions)
    from typing_extensions import TypeIs  # type: ignore[assignment]

# Kiểm tra kiểu dữ liệu với type() và isinstance()
developer = 'Devin'
raw_balance: object = '12'

# Hàm type(): Trả về kiểu dữ liệu cụ thể của một đối tượng
# Lưu ý: type() nhận 1 đối số (hoặc 3 đối số khi tạo class động), gọi không tham số sẽ gây TypeError.
print("type(developer):", type(developer))                   # <class 'str'>
print(type(10), type(4.50), type(True), type(None))         # <class 'int'> <class 'float'> <class 'bool'> <class 'NoneType'>

# Vì sao cần kiểm tra kiểu dữ liệu trước khi tính toán?
# Thao tác tính toán trên kiểu không tương thích sẽ phát sinh ngoại lệ TypeError:
try:
    if not isinstance(raw_balance, (int, float)):
        raise TypeError(f"unsupported operand type(s) for /: '{type(raw_balance).__name__}' and 'int'")
    _ = raw_balance / 2
except TypeError as err:
    print("Caught expected TypeError:", err)

# Hàm isinstance(): Kiểm tra đối tượng có khớp với kiểu dữ liệu hay không (trả về bool True/False)
print("isinstance(raw_balance, int):", isinstance(raw_balance, int)) # False


# SO SÁNH VỚI PYTHON MỚI NHẤT (PYTHON 3.10 -> 3.14):

# Cách truyền thống (Trước Python 3.10): Dùng tuple chứa các kiểu
sample_data: object = 12
print("Legacy tuple syntax - (int, float):", isinstance(sample_data, (int, float))) # True

# Cú pháp hiện đại (Python 3.10+ PEP 604): Dùng toán tử Union '|' trực tiếp trong isinstance()
# Không cần tạo tuple, cú pháp tự nhiên và đồng nhất với type hints:
print("Modern union syntax - int | float:", isinstance(sample_data, int | float))   # True

# Kiểm tra trường tùy chọn (Cho phép kiểu dữ liệu hoặc None trong Python 3.10+):
# PEP 604 cho phép truyền trực tiếp 'str | None' vào isinstance():
optional_value: object = None
print("Optional field (str | None):", isinstance(optional_value, str | None))        # True

# Khai báo Type Alias bằng từ khóa 'type' (Python 3.12+ PEP 695):
# Lưu ý: Type alias tạo bởi 'type' là đối tượng TypeAliasType cho static typing.
# Tại runtime, để dùng với isinstance() cần truy cập qua thuộc tính .__value__:
type Numeric = int | float

val: object = 99.5
print("Numeric.__value__:", Numeric.__value__)                                       # int | float
print("isinstance with Numeric.__value__:", isinstance(val, Numeric.__value__))      # True

# Cạm bẫy bool kế thừa từ int:
# - Trong Python, bool là lớp con của int (issubclass(bool, int) == True).
# - Do đó, isinstance(True, int) trả về True!
print("isinstance(True, int):", isinstance(True, int))           # True (Cạm bẫy kế thừa!)
print("type(True) is bool:", type(True) is bool)                 # True (Kiểm tra chính xác danh tính lớp)
print("type(True) in (int, float):", type(True) in (int, float)) # False (Loại trừ an toàn bool)

# Type Narrowing chuyên nghiệp với TypeIs (Python 3.13+ PEP 742):
# Hàm kiểm tra kiểu tuỳ chỉnh giúp Type Checker (Pyright/Mypy) thu hẹp kiểu chính xác cả khi True và False:
def is_numeric(value: object) -> TypeIs[Numeric]:
    return isinstance(value, int | float) and not isinstance(value, bool)

test_val: object = True
print("is_numeric(True):", is_numeric(test_val))                 # False
print("is_numeric(42):", is_numeric(42))                         # True


# Chú thích kiểu dữ liệu cho biến (Type Annotations / Type Hints)
# - Type hints hỗ trợ công cụ kiểm tra tĩnh (Pyright, Mypy), autocomplete trên IDE.
# - Python không ép kiểu hay báo lỗi ở runtime nếu gán sai kiểu.

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
