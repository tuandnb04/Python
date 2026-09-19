# Built-in functions: print(), input(), int()
# int() chuyển đổi float, numeric string, và boolean sang integer
print(int(3.14))       # 3
print(int('42'))       # 42
print(int(True))       # 1
print(int(False))      # 0

# Định nghĩa hàm (def) & Thụt lề (Indentation)
def hello() -> None:
    print('Hello World')

hello()                # Hello World

# Parameters (Tham số) vs Arguments (Đối số)
def print_sum(a: int, b: int) -> None:
    print(a + b)

# Từ khóa return vs Giá trị mặc định None (NoneType)
# Hàm chỉ print() mà không có return thì mặc định trả về None
result = print_sum(3, 1)              # In: 4
print("Result:", result)              # Result: None

# Dùng return để trả kết quả về biến lưu trữ
def calculate_area(width: int | float, height: int | float) -> int | float:
    return width * height

area = calculate_area(5, 3.5)
print("Area:", area)                  # Area: 17.5

# Docstrings (Tài liệu hóa hàm với 3 dấu nháy kép)
def is_even(num: int) -> bool:
    """Check whether an integer is even."""
    return num % 2 == 0

print("is_even(4):", is_even(4))      # True
print("Docstring:", is_even.__doc__)  # Check whether an integer is even.


# Type Hints, Tham số mặc định (Default Parameter) & Đối số theo tên (Keyword Argument)
def greet(name: str, greeting: str = 'Hello') -> str:
    return f"{greeting}, {name}"

print(greet('Alice'))                          # Hello, Alice (dùng giá trị mặc định)
print(greet('Bob', greeting='Hi'))             # Hi, Bob (truyền đối số theo tên)

# Positional-only (trước '/') & Keyword-only (sau '*') (Python 3.8+)
def format_user(name: str, /, age: int, *, role: str = 'Dev') -> str:
    return f"{name} ({age}) - {role}"

print(format_user('Alice', 25, role='Admin'))  # name bắt buộc truyền vị trí, role bắt buộc truyền tên

# Kiểu kết hợp Union / Optional (Python 3.10+ dùng '|')
def divide(a: int | float, b: int | float) -> float | None:
    if b == 0:
        return None
    return a / b

print("divide(10, 2):", divide(10, 2)) # 5.0
print("divide(10, 0):", divide(10, 0)) # None

# Scope (Phạm vi truy cập): Global Scope vs Local Scope
tax_rate: float = 0.1                 # Biến toàn cục (Global Scope)

def calculate_tax(price: float) -> float:
    tax: float = price * tax_rate     # price và tax là biến cục bộ (Local Scope)
    return tax

print("Tax (50$):", calculate_tax(50.0)) # 5.0
print("Tax rate:", tax_rate)             # 0.1
# print(tax)                             # NameError: Không thể truy cập biến local từ bên ngoài