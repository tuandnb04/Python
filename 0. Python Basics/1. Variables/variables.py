# 0. Câu lệnh (Statements) & Chú thích (Comments)
# - Câu lệnh (Statement) kết thúc khi hết dòng (newline), không bắt buộc dùng dấu chấm phẩy `;`.
# - Các câu lệnh được thực thi tuần tự từ trên xuống dưới.
# - Dấu chấm phẩy `;` là tùy chọn, chỉ dùng khi viết nhiều câu lệnh trên 1 dòng (vd: x = 1; y = 2).
#   Nếu viết nhiều lệnh trên 1 dòng mà thiếu dấu phân cách (newline hoặc `;`) sẽ bị lỗi: SyntaxError.
# - Dòng chú thích (Comment) bắt đầu bằng dấu thăng `#`, trình thông dịch sẽ bỏ qua.
# - Chú thích cùng dòng (Inline comment): PEP 8 khuyến nghị cách lệnh code ít nhất 2 khoảng trắng.
# - Chú thích nhiều dòng: Dùng chuỗi 3 dấu nháy đơn hoặc kép ''' ... ''' hoặc """ ... """

# 1. Khai báo biến & Các kiểu dữ liệu cơ bản (str, int, float, bool, None)
user_name = 'Alice'  # str
user_age = 20  # int
total_score = 100  # int
score = 80.5  # float
is_student = True  # bool
empty_val = None  # NoneType

# 2. Hàm print(): In ra terminal (dấu phẩy tự chèn khoảng trắng)
print('User info:', user_name, user_age, total_score)
print('Sep parameter (sep="-"):', end=' ')
print('2026', '10', '13', sep='-')  # 2026-10-13 (thay đổi ký tự phân tách)
print('End parameter (end="... "):', end='... ')  # thay đổi ký tự kết thúc (mặc định là xuống dòng \n)
print('Done!')

# 3. Dynamic typing: Tự nhận diện kiểu, có thể gán lại bằng kiểu khác
age = 20
age = 'Twenty'
print('Reassigned age:', age)

# 4. Kiểm tra kiểu: type() và isinstance()
print(type(user_name))  # <class 'str'>
print(type(user_age))  # <class 'int'>
print(type(score))  # <class 'float'>
print(type(is_student))  # <class 'bool'>
print(type(empty_val))  # <class 'NoneType'>

print(isinstance(score, float))  # True
print(isinstance(user_name, int))  # False
print(isinstance(score, int | float))  # type: ignore # True (kiểm tra nhiều kiểu với toán tử |)

# 5. Ép kiểu dữ liệu (Type Casting)
print(str(100))  # '100'
print(bool(1), bool(0))  # True False
print(bool('hello'), bool(''))  # True False

# 6. Quy tắc đặt tên biến & Hằng số (PEP 8 Conventions & Constants)
# - Bắt đầu bằng chữ cái hoặc dấu gạch dưới `_`, KHÔNG được bắt đầu bằng số (vd: `2name` -> SyntaxError).
# - Không chứa ký tự đặc biệt (@, $, %, -...) ngoại trừ dấu gạch dưới.
# - Phân biệt hoa thường (Case-sensitive): 'user', 'User' và 'USER' là 3 biến khác nhau:
user = "Alice"
User = "Bob"
USER = "Charlie"
print("Case-sensitive variables:", user, User, USER)  # Alice Bob Charlie

# - Chuẩn đặt tên PEP 8:
#   + Biến & hàm: dùng snake_case (vd: `first_name`, `total_amount`)
#   + Lớp (Class): dùng PascalCase (vd: `UserProfile`, `DogBreed`)
#   + Hằng số (Constants): dùng UPPER_SNAKE_CASE (Python không có từ khóa `const`, quy ước viết hoa toàn bộ để báo hiệu không sửa đổi)
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT = 30
PI = 3.14159

# 7. Từ khóa bảo lưu trong Python (Reserved Keywords)
# Không được dùng các từ khóa có sẵn của Python để đặt tên biến (như `if`, `for`, `class`, `def`, `pass`...)
import keyword

print("Total keywords in Python:", len(keyword.kwlist))
print("Is 'pass' a keyword?:", keyword.iskeyword('pass'))  # True
print("Is 'student' a keyword?:", keyword.iskeyword('student'))  # False

# 8. Kỹ thuật gán biến nâng cao (Multiple Assignment & Variable Operations)
# - Gán nhiều giá trị cùng lúc (Unpacking):
x, y, z = 10, 20, 30
print(f"Unpacked variables: x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# - Hoán đổi giá trị 2 biến trực tiếp (không cần biến trung gian 'temp'):
a, b = 5, 99
a, b = b, a
print(f"Swapped values: a={a}, b={b}")  # a=99, b=5

# - Gán cùng một giá trị cho nhiều biến (Chained assignment):
counter1 = counter2 = counter3 = 0
print(f"Chained assignment: {counter1}, {counter2}, {counter3}")  # 0, 0, 0

# - Xóa biến khỏi bộ nhớ bằng từ khóa 'del':
temp_token = "auth_xyz"
del temp_token
# print(temp_token) -> NameError: name 'temp_token' is not defined

# 9. Toán tử gán (Assignment Operators) & Toán tử Walrus (:=)
# - Bảng các toán tử gán phổ biến trong Python:
#   + '='    : x = 5          (Gán cơ bản)
#   + '+='   : x += 3         (Tương đương: x = x + 3)
#   + '-='   : x -= 3         (Tương đương: x = x - 3)
#   + '*='   : x *= 3         (Tương đương: x = x * 3)
#   + '/='   : x /= 3         (Tương đương: x = x / 3)
#   + '%='   : x %= 3         (Tương đương: x = x % 3)
#   + '//='  : x //= 3        (Tương đương: x = x // 3)
#   + '**='  : x **= 3        (Tương đương: x = x ** 3)
#   + '&='   : x &= 3         (Tương đương: x = x & 3   - Bitwise AND)
#   + '|='   : x |= 3         (Tương đương: x = x | 3   - Bitwise OR)
#   + '^='   : x ^= 3         (Tương đương: x = x ^ 3   - Bitwise XOR)
#   + '>>='  : x >>= 3        (Tương đương: x = x >> 3  - Dịch phải)
#   + '<<='  : x <<= 3        (Tương đương: x = x << 3  - Dịch trái)
num_demo = 10
num_demo += 5   # 15
num_demo *= 2   # 30
num_demo //= 4  # 7
print("Assignment operators demo (num_demo):", num_demo)  # 7

# - Toán tử Walrus (:=) (Assignment Expression, Python 3.8+):
#   Gán giá trị cho biến ngay bên trong một biểu thức lớn hơn
print("Walrus print expression:", (walrus_val := 3))  # In ra 3 và đồng thời gán walrus_val = 3
total_score = (base_score := 80) + 15
print("Walrus in math expression:", total_score, "| base_score:", base_score)  # 95 | 80

# 10. Nhập dữ liệu với input() & Ép kiểu dữ liệu (Standard Input)
# - Hàm input() luôn trả về kiểu dữ liệu là chuỗi (str)
# - Ép kiểu số:
#   age_input = int(input("Enter age: "))
#   price_input = float(input("Enter price: "))
# - Kỹ thuật nhập nhiều giá trị trên 1 dòng (dùng split):
#   x, y = input().split()                 # Tách chuỗi theo khoảng trắng
#   a, b = map(int, input().split())        # Ép kiểu int cho từng phần tử
#   nums = list(map(int, input().split()))  # Nhập mảng số nguyên


