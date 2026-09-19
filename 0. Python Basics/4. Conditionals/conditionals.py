# Truthy và Falsy (Kiểm tra bằng hàm bool)
# Falsy: 0, 0.0, '', None, False | Truthy: Các giá trị còn lại (1, 'Hello', 'False')
print(bool(0), bool(''), bool('Hello'), bool(1))  # False False True True

# Toán tử logic & Short-circuiting (and, or, not)
# and: Trả về falsy đầu tiên hoặc giá trị cuối
print(True and 25)      # 25

# or: Trả về truthy đầu tiên hoặc giá trị cuối
print(19 or False)      # 19

# not: Đảo ngược giá trị boolean
print(not '', not 'Hi') # True False

# Toán tử so sánh (Trả về True / False)
print(3 > 4)    # False
print(3 == 4)   # False
print(3 != 4)   # True
print(3 <= 4)   # True

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
print("Ternary status:", status)    # 'Minor'

# 'pass' dùng làm placeholder khi chưa viết code cho block
if age < 0:
    pass

# if lồng nhau (Nested if)
if age < 18:
    if age < 13:
        print('Child under 13')

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
        print("Unknown Status Code")       # case _ tương đương 'else'

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