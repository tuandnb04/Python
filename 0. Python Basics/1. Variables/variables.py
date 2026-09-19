# Khai báo biến (Quy ước snake_case, bắt đầu bằng chữ cái hoặc gạch dưới)
user_name = 'Alice'
user_age = 20
total_score = 100
print('User info:', user_name, user_age, total_score) # Dấu phẩy tự chèn khoảng trắng

# Dynamic typing: Tự nhận diện kiểu, có thể gán lại bằng kiểu khác
age = 20
print('Initial age:', age)
age = 'Twenty'
print('Reassigned age:', age)

# Các kiểu dữ liệu cơ bản & Hàm type() kiểm tra kiểu
name = 'Alice'
print(name, type(name))               # Alice <class 'str'>

age = 20
print(age, type(age))                 # 20 <class 'int'>

score = 80.5
print(score, type(score))             # 80.5 <class 'float'>

is_student = True
print(is_student, type(is_student))   # True <class 'bool'>

empty_val = None
print(empty_val, type(empty_val))     # None <class 'NoneType'>

# Hàm isinstance(): Kiểm tra kiểu dữ liệu của biến (trả về bool)
print(isinstance(score, float))       # True
print(isinstance(name, int))          # False (chuỗi không phải số nguyên)
print(isinstance(score, int | float)) # True (toán tử | cho phép kiểm tra nhiều kiểu)