# Định nghĩa hàm (def) & Thụt lề (Indentation)
def hello() -> None:
    print('Hello World')

hello()                # Hello World

# Parameters (Tham số) vs Arguments (Đối số)
def print_sum(a: int, b: int) -> None:
    print(a + b)

# Từ khóa return vs Giá trị mặc định None (NoneType)
# Hàm chỉ print() mà không có return thì mặc định trả về None
result = print_sum(3, 1)
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
# Định nghĩa Type Alias hiện đại với từ khóa 'type' (Python 3.12+ PEP 695)
type Number = int | float

def divide(a: Number, b: Number) -> float | None:
    if b == 0:
        return None
    return a / b

print("divide(10, 2):", divide(10, 2)) # 5.0
print("divide(10, 0):", divide(10, 0)) # None


# Scope & Variable Binding: Global vs Local vs Nonlocal
tax_rate: float = 0.1                 # Biến toàn cục (Global Scope)

def update_tax_rate(new_rate: float) -> None:
    global tax_rate                   # Từ khóa 'global': cho phép sửa đổi biến ngoài scope
    tax_rate = new_rate

def calculate_tax(price: float) -> float:
    tax: float = price * tax_rate     # price và tax là biến cục bộ (Local Scope)
    return tax

print("Tax (50$):", calculate_tax(50.0)) # 5.0
update_tax_rate(0.15)
print("New Tax rate:", tax_rate)         # 0.15
print("Tax after update:", calculate_tax(50.0)) # 7.5

# CƠ CHẾ TRUYỀN ĐỐI SỐ: Pass-by-assignment & Variable Shadowing
# - Với kiểu Immutable (int, float, str, bool): Gán lại tham số bên trong hàm chỉ làm trỏ biến local sang object mới,
#   không làm đổi biến gốc bên ngoài. Muốn cập nhật ra ngoài, caller BẮT BUỘC phải gán lại giá trị trả về: x = func(x).
# - Tên tham số trùng tên biến ngoài scope sẽ che khuất biến ngoài đó (Variable Shadowing).


# Closure & từ khóa 'nonlocal' (can thiệp biến của hàm bao bọc)
def create_counter(start: int = 0):
    count = start
    def step() -> int:
        nonlocal count                # 'nonlocal': sửa đổi biến của hàm cha ngoài frame hiện tại
        count += 1
        return count
    return step

counter = create_counter(10)
print("Counter call 1:", counter())   # 11
print("Counter call 2:", counter())   # 12


# Generic Functions với cú pháp Type Parameter [T] (Python 3.12+ PEP 695)
# Thay thế hoàn toàn cách dùng TypeVar cũ từ thư viện 'typing'
def identity[T](value: T) -> T:
    """Hàm generic: Giữ nguyên kiểu dữ liệu của tham số truyền vào."""
    return value

def choose_first[T](first: T, second: T) -> T:
    """Hàm generic: Nhận hai giá trị cùng kiểu và chọn giá trị đầu tiên."""
    return first

print("Generic identity (int):", identity(42))            # 42
print("Generic identity (str):", identity("Hello"))       # Hello
print("Generic choose_first:", choose_first(100, 200))    # 100


# Đối số tùy biến số lượng: *args & **kwargs
def make_label(prefix: str, *tags: str, sep: str = " | ") -> str:
    """*tags thu thập các đối số vị trí tùy biến."""
    return prefix + sep + sep.join(tags)

print(make_label("Report", "2026", "Q1", "Draft"))        # Report | 2026 | Q1 | Draft

def log_event(event_name: str, **attributes: str) -> None:
    """**attributes thu thập các đối số từ khóa tùy biến."""
    print(f"Event: {event_name}, attribute count: {len(attributes)}")

log_event("LOGIN", user="Alice", status="SUCCESS")