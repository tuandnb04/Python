# Truthy và Falsy (Kiểm tra bằng hàm bool)
# Falsy: 0, 0.0, '', None, False | Truthy: Các giá trị còn lại (1, 'Hello', 'False')
print(bool(0), bool(''), bool('Hello'), bool(1))  # False False True True

# Toán tử logic & Short-circuiting (and, or, not)
# and: Trả về falsy đầu tiên hoặc giá trị cuối
print(True and 25)  # 25

# or: Trả về truthy đầu tiên hoặc giá trị cuối
print(19 or False)  # 19

# not: Đảo ngược giá trị boolean
print(not '', not 'Hi')  # True False

# Toán tử so sánh (Trả về True / False)
print(3 > 4)  # False
print(3 == 4)  # type: ignore # False
print(3 != 4)  # type: ignore # True
print(3 <= 4)  # True

# Lưu ý về so sánh Boolean và Số nguyên:
# Trong Python, False == 0 và True == 1 đều là True khi so sánh giá trị.
# Để phân biệt chính xác False với 0, ta dùng toán tử identity 'is' hoặc kiểm tra 'type(x) is bool':
val = 0
print(False == val, True == 1)  # type: ignore # True True
print(False is val)  # type: ignore # False (False và 0 là hai đối tượng khác nhau)
print(type(False) is bool)  # True

# Mẹo Pythonic: Đếm số điều kiện thỏa mãn bằng cộng Boolean (True tương đương 1, False tương đương 0):
# Ví dụ kiểm tra có đúng 2 trong 3 số là số dương:
a, b, c = 5, -2, 3
is_two_positive = (a > 0) + (b > 0) + (c > 0) == 2
print("Are exactly two positive:", is_two_positive)  # True

# Phân biệt isinstance() vs type() is (Kiểm tra kiểu dữ liệu):
# - isinstance(True, int) trả về True vì bool được coi như dạng số nguyên trong Python.
# - type(True) is int trả về False vì kiểm tra chính xác kiểu dữ liệu thuần túy.
print("isinstance(True, int):", isinstance(True, int))  # True
print("type(True) is int:    ", type(True) is int)  # False (chính xác kiểu số nguyên)

# Kiểm tra an toàn trước khi xử lý (không nhầm lẫn True/False với 1/0):
test_val = True
if type(test_val) is int:
    print("Exact integer:", test_val)
else:
    print("Not an integer (type is bool or other):", type(test_val).__name__)


# Câu lệnh điều kiện if - elif - else & từ khóa pass
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

# Toán tử 3 ngôi (Ternary Operator): val_if_true if condition else val_if_false
status = 'Adult' if age >= 18 else 'Minor'
print("Ternary status:", status)  # 'Minor'

# 'pass' dùng làm placeholder khi chưa viết code cho block
if age < 0:
    pass

# if lồng nhau (Nested if)
if age < 18:
    if age < 13:
        print('Child under 13')

# Cấu trúc if - elif - else nhiều nhánh với toán tử logic (and, or, not)
score = 75
if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 50:
    grade = 'C'
else:
    grade = 'F'
print("Grade result:", grade)  # 'B'

# Structural Pattern Matching (match - case) trong Python 3.10+ (PEP 634)
# Khớp giá trị cụ thể (Literal Matching)
status_code = 404

match status_code:
    case 200:
        print("Success: OK")
    case 400:
        print("Error: Bad Request")
    case 404:
        print("Error: Not Found")
    case 500:
        print("Error: Internal Server Error")
    case _:
        print("Unknown Status Code")  # case _ tương đương 'else'

# Khớp mẫu với điều kiện bổ sung (Guards với từ khóa 'if')
score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 80:
        print("Grade: B")
    case s if s >= 70:
        print("Grade: C")
    case _:
        print("Grade: F")

# Khớp mẫu với nhiều giá trị (OR pattern với '|')
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Unknown day")

# Khớp mẫu kết hợp gán biến (as pattern)
role = "admin"

match role:
    case "admin" | "superuser" as privileged_role:
        print(f"Privileged access granted for: {privileged_role}")
    case "guest":
        print("Guest access only")
    case _:
        print("Standard user access")

