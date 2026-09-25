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

# Lưu ý: bool là lớp con của int trong Python (issubclass(bool, int) -> True)
# Do đó: False == 0 và True == 1 đều là True.
# Để phân biệt chính xác False với 0, cần dùng identity: `x is False` hoặc `type(x) is bool`.
val = 0
print(issubclass(bool, int))  # type: ignore # True
print(False == val, True == 1)  # type: ignore # True True
print(False is val)  # type: ignore # False (so sánh identity: False và 0 trỏ tới 2 đối tượng khác nhau)
print(type(False) is bool)  # True

# Mẹo Pythonic: Đếm số điều kiện thỏa mãn nhanh nhất bằng cộng Boolean (True == 1, False == 0):
# Ví dụ kiểm tra có đúng 2 trong 3 số là số dương:
a, b, c = 5, -2, 3
is_two_positive = (a > 0) + (b > 0) + (c > 0) == 2
print("Are exactly two positive:", is_two_positive)  # True

# Phân biệt isinstance() vs type() is Class (Bẫy lọc kiểu dữ liệu):
# - isinstance(x, int): Chấp nhận cả lớp con kế thừa (nên isinstance(True, int) -> True).
# - type(x) is int: Kiểm tra chính xác kiểu dữ liệu, loại bỏ lớp con (type(True) is int -> False).
print("isinstance(True, int):", isinstance(True, int))  # True (nguy cơ nhận nhầm bool là int)
print("type(True) is int:    ", type(True) is int)  # False (chính xác int thuần túy)

# Ứng dụng: Lọc danh sách chỉ lấy số nguyên, loại bỏ boolean và chuỗi:
mixed_list = [1, 'a', 'b', 0, 15, False, True]
integers_only = [x for x in mixed_list if type(x) is int]
print("Integers only:", integers_only)  # [1, 0, 15] (False và True bị loại bỏ an toàn)

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
