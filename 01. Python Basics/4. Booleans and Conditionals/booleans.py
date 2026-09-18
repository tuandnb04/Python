# 1. Truthy và Falsy (Kiểm tra bằng hàm bool)
# Falsy: 0, 0.0, '', None, False | Truthy: Các giá trị còn lại (1, 'Hello', 'False')
print(bool(0), bool(''), bool('Hello'), bool(1))  # False False True True

# 2. Toán tử logic & Short-circuiting (and, or, not)
# and: Trả về falsy đầu tiên hoặc giá trị cuối
print(True and 25)      # 25

# or: Trả về truthy đầu tiên hoặc giá trị cuối
print(19 or False)      # 19

# not: Đảo ngược giá trị boolean
print(not '', not 'Hi') # True False

# 3. Ứng dụng trong câu lệnh điều kiện
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print('You can watch the movie.')