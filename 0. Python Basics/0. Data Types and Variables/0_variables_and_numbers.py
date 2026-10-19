# 1. Xuất dữ liệu với print() và chú thích (#)
print("Hello, World!")
print("My favorite colors are", "blue", "green", "red")  # In nhiều giá trị

# 2. Khai báo biến và quy tắc đặt tên (snake_case)
# Biến dùng để lưu trữ dữ liệu; dùng snake_case, không bắt đầu bằng số:
name = "Tobias"
age = 25
total_score = 100
print("Name:", name, "| Age:", age)

# 3. Các kiểu dữ liệu cơ bản và hàm kiểm tra type()
# 4 kiểu dữ liệu nền tảng: int (nguyên), float (thực), str (chuỗi), bool (đúng/sai):
int_num = 5
float_num = 3.14
message = "Python"
is_active = True

print(type(int_num))     # <class 'int'>
print(type(float_num))   # <class 'float'>
print(type(message))     # <class 'str'>
print(type(is_active))   # <class 'bool'>

# 4. Ép kiểu dữ liệu (Type Casting: int, float, str)
print("int(3.14):", int(3.14))              # 3 (cắt bỏ phần thập phân)
print("float(5):", float(5))                # 5.0 (thêm phần thập phân)
print("int('55'):", int("55"))              # 55 (chuyển chuỗi số sang int)
print("str(22):", "Emil is " + str(22))     # 'Emil is 22' (ép số sang chuỗi để nối)

# 5. Phép toán số học và thứ tự ưu tiên (Operator Precedence)
# Thứ tự: Ngoặc tròn () -> Nhân/Chia (* /) -> Cộng/Trừ (+ -):
print("Precedence (100 + 5 * 3):", 100 + 5 * 3)            # 115
print("With parentheses ((100 + 5) * 3):", (100 + 5) * 3)  # 315
print("Division (9 / 3):", 9 / 3)                          # 3.0 (phép / luôn ra float)
print("Floor division (10 // 3):", 10 // 3)               # 3 (chia lấy phần nguyên)
print("Remainder (10 % 3):", 10 % 3)                      # 1 (chia lấy phần dư)
print("Power (2 ** 3):", 2 ** 3)                          # 8 (lũy thừa)

# 6. Toán tử gán kết hợp (+=, -=) và làm tròn round()
score = 10
score += 5  # score = score + 5
print("Updated score:", score)                    # 15
print("Round to 2 decimals:", round(3.14159, 2))  # 3.14
