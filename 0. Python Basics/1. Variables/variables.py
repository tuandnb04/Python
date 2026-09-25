# 1. Khai báo biến & Các kiểu dữ liệu cơ bản (str, int, float, bool, None)
user_name = 'Alice'        # str
user_age = 20              # int
total_score = 100          # int
score = 80.5               # float
is_student = True          # bool
empty_val = None           # NoneType

# 2. Hàm print(): In ra terminal (dấu phẩy tự chèn khoảng trắng)
print('User info:', user_name, user_age, total_score)

# 3. Dynamic typing: Tự nhận diện kiểu, có thể gán lại bằng kiểu khác
age = 20
age = 'Twenty'
print('Reassigned age:', age)

# 4. Kiểm tra kiểu: type() và isinstance()
print(type(user_name))                 # <class 'str'>
print(type(user_age))                  # <class 'int'>
print(type(score))                     # <class 'float'>
print(type(is_student))                # <class 'bool'>
print(type(empty_val))                 # <class 'NoneType'>

print(isinstance(score, float))        # True
print(isinstance(user_name, int))      # False
print(isinstance(score, int | float))  # type: ignore # True (kiểm tra nhiều kiểu với toán tử |)

# 5. Ép kiểu dữ liệu (Type Casting)
print(str(100))                        # '100'
print(bool(1), bool(0))                # True False
print(bool('hello'), bool(''))         # True False