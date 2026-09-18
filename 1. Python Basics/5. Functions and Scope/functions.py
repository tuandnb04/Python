# 1. Built-in functions: print(), input(), int()
# int() chuyển đổi float, numeric string, và boolean sang integer:
print(int(3.14))       # 3
print(int('42'))       # 42
print(int(True))       # 1
print(int(False))      # 0
# name = input('What is your name? ') # Nhận input từ người dùng (trả về chuỗi str)

# 2. Định nghĩa hàm (def), Thân hàm (Body) & Thụt lề (Indentation)
# - Khai báo hàm bằng từ khóa 'def'. Khối lệnh thân hàm nhận diện bằng thụt lề.
# - '-> None' biểu thị hàm chỉ thực thi hành động mà không trả về dữ liệu.
def hello() -> None:
    print('Hello World')

hello()                # Hello World

# 3. Parameters (Tham số) vs Arguments (Đối số) & Lỗi TypeError
# - Parameter: Biến giữ chỗ khi định nghĩa hàm (có kèm kiểu dữ liệu: a: int, b: int).
# - Argument: Giá trị thực tế truyền vào khi gọi hàm (3, 1).
def print_sum(a: int, b: int) -> None:
    print(a + b)

# Gọi thiếu argument sẽ gây lỗi TypeError:
# print_sum()          # TypeError: print_sum() missing 2 required positional arguments: 'a' and 'b'

# 4. Từ khóa return vs Giá trị mặc định None (NoneType)
# - None là giá trị duy nhất của NoneType (bất biến, falsy, đại diện cho sự vắng mặt của giá trị).
# - Hàm chỉ dùng print() mà không có return thì mặc định trả về None:
my_val = print_sum(3, 1) # In ra: 4
print(my_val)            # In ra: None

# - Dùng 'return' để trả kết quả về biến lưu trữ (kết hợp toán tử '|' cho nhiều kiểu dữ liệu):
def calculate_sum(a: int | float, b: int | float) -> int | float:
    return a + b

my_sum = calculate_sum(3, 1)
print("my_sum:", my_sum) # 4

# 5. Docstrings (Tài liệu hóa hàm / class)
# Docstring đặt ở dòng đầu tiên của hàm/class, thường dùng 3 dấu nháy kép (""").
def add(x: int | float, y: int | float) -> int | float:
    """A function that returns the sum of two numbers."""
    return x + y

print("Docstring:", add.__doc__) # A function that returns the sum of two numbers.
# help(add)                      # Bỏ comment để xem tài liệu chi tiết qua hàm help()

# 6. Type Hints (Gợi ý kiểu dữ liệu)
# - Type hints là các chú thích KHÔNG bắt buộc (optional signals), giúp lập trình viên và IDE
#   biết kiểu dữ liệu mong đợi của biến, tham số hoặc giá trị trả về của hàm.
# - LƯU Ý QUAN TRỌNG: Python KHÔNG tự động ép kiểu hay báo lỗi ở runtime nếu truyền sai kiểu.
#   Type hints chủ yếu phục vụ autocomplete, tài liệu hóa code và công cụ kiểm tra tĩnh (như mypy).

# a. Type hint cho tham số và giá trị trả về của hàm:
def greet(name: str) -> str:
    return 'Hello, ' + name

print(greet('Alice'))            # Hello, Alice

# b. Type hint cho biến thông thường:
age: int = 25
is_active: bool = True

# c. Kiểu kết hợp Union / Optional (Python 3.10+ dùng toán tử '|'):
# Có thể nhận int hoặc float; trả về int, float hoặc None:
def divide(a: int | float, b: int | float) -> float | None:
    if b == 0:
        return None
    return a / b

print("divide(10, 2):", divide(10, 2))  # 5.0
print("divide(10, 0):", divide(10, 0))  # None