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
items = ["apple", "banana", "cherry"]
formatted_list = f"Items: {', '.join([f'item_{i}:{item}' for i, item in enumerate(items)])}"
print(formatted_list)

# Ký tự backslash '\' bên trong biểu thức {}
names = ["Alice", "Bob", "Charlie"]
print(f"List:\n{'\n'.join([f'- {n}' for n in names])}")

# Kỹ thuật Unpacking (*) vào mẫu chuỗi với str.format()
# Tự động điền phần tử và ép kiểu số thành chuỗi ở cấp độ C
phone_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

print(create_phone_number(phone_nums)) # '(123) 456-7890'