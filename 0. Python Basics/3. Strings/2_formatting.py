# Nối chuỗi (+) và Lặp chuỗi (*)
print('Hello' + ' ' + 'World')  # 'Hello World'
print('ha' * 3)                 # 'hahaha'
# print('John' + 26)            # TypeError: chỉ nối được str với str (không nối được int)
print('John' + str(26))         # 'John26' (cách cũ: phải ép kiểu str thủ công)

# Định dạng chuỗi với F-string (Chuẩn hiện đại, nhanh và trực quan)
name, age = 'John', 26
print(f"Name: {name}, Age: {age}") # 'Name: John, Age: 26'
print(f"5 + 10 = {5 + 10}")        # '5 + 10 = 15'

# Cải tiến f-strings trong Python 3.12+ (PEP 701)
# Tái sử dụng cùng loại dấu ngoặc kép bên trong biểu thức
user_data = {"name": "Antigravity", "role": "AI Assistant"}
print(f"User: {user_data['name']} with role: {user_data['role']}")

# Lồng f-string bên trong f-string (Nested f-strings)
# Cách viết Clean Code: Tách bước xử lý list ra trước giúp code dễ đọc hơn thay vì nhồi nhét
items = ["apple", "banana", "cherry"]
item_tags = [f"item_{i}:{item}" for i, item in enumerate(items)]
formatted_list = f"Items: {', '.join(item_tags)}"
print(formatted_list)


# Ký tự backslash '\' bên trong biểu thức {}
names = ["Alice", "Bob", "Charlie"]
print(f"List:\n{'\n'.join([f'- {n}' for n in names])}")

# Định dạng số điện thoại chuẩn hiện đại với F-string & Slicing:
# (Thay thế cách cũ dùng `str.format(*n)` vốn chậm và khó bảo trì)
phone_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
    s = ''.join(map(str, n))
    return f"({s[:3]}) {s[3:6]}-{s[6:]}"

print(create_phone_number(phone_nums)) # '(123) 456-7890'


# Căn lề và định dạng khoảng đệm với F-string (Format Specifiers: <, >, ^)
text, width = "Tower", 11
print(f"{text:<{width}}")   # 'Tower      ' (căn trái)
print(f"{text:>{width}}")   # '      Tower' (căn phải)
print(f"{text:^{width}}")   # '   Tower   ' (căn giữa)
print(f"{text:*^{width}}")  # '***Tower***' (căn giữa với ký tự lấp đầy '*')