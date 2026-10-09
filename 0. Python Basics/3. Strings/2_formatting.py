# 1. Nối chuỗi (+, +=) và Nhân bản chuỗi (*, *=)
print('Hello' + ' ' + 'World')        # 'Hello World'
print('ha' * 3)                       # 'hahaha'

# Gán kết hợp (Augmented assignment) với chuỗi:
greeting = 'Hello'
greeting += ' World'                  # "Hello World" (tương đương greeting = greeting + " World")
greeting *= 2                         # 'Hello WorldHello World' (lặp chuỗi 2 lần)
# greeting -= 'World'                 # TypeError: unsupported operand type(s) for -=: 'str' and 'str'

# print('Age: ' + 26)                 # Lỗi TypeError: can only concatenate str (not "int") to str
print('Age: ' + str(26))              # 'Age: 26' (phải ép kiểu str() trước khi nối bằng '+')

# 2. Định dạng chuỗi với F-string (Chuẩn hiện đại, tự động convert kiểu, trực quan)
name, age = 'John', 26
print(f"Name: {name}, Age: {age}") # 'Name: John, Age: 26'
print(f"5 + 10 = {5 + 10}")        # '5 + 10 = 15'

# Cải tiến f-strings trong Python 3.12+ (PEP 701)
# Cho phép tái sử dụng cùng loại dấu ngoặc kép bên trong biểu thức {}
print(f"Inline method: {'Hello World'.lower()}")

# Lồng biểu thức định dạng bên trong f-string (Dynamic format specifiers)
value = 12.3456
precision = 2
print(f"Dynamic precision: {value:.{precision}f}") # '12.35'

# Định dạng chuỗi số điện thoại bằng Slicing và F-string:
raw_phone = "1234567890"
formatted_phone = f"({raw_phone[:3]}) {raw_phone[3:6]}-{raw_phone[6:]}"
print("Formatted phone:", formatted_phone) # '(123) 456-7890'



# Căn lề và định dạng khoảng đệm với F-string (Format Specifiers: <, >, ^)
text, width = "Tower", 11
print(f"{text:<{width}}")   # 'Tower      ' (căn trái)
print(f"{text:>{width}}")   # '      Tower' (căn phải)
print(f"{text:^{width}}")   # '   Tower   ' (căn giữa)
print(f"{text:*^{width}}")  # '***Tower***' (căn giữa với ký tự lấp đầy '*')