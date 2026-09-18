# Cải tiến f-strings trong Python 3.12+ (PEP 701)
# => TẠI SAO CẢI TIẾN NÀY TỐT HƠN TRƯỚC?
#    + Trước Python 3.12: Không thể tái sử dụng cùng loại dấu ngoặc kép bên trong {}, 
#      phải đổi sang ngoặc đơn '', không cho phép lồng f-string hoặc dùng ký tự '\'.
#    + Từ Python 3.12: Bộ phân tích cú pháp mới cho phép viết f-string tự nhiên như code Python thông thường.

# Tái sử dụng cùng loại dấu ngoặc kép bên trong biểu thức
user_data = {"name": "Antigravity", "role": "AI Assistant"}
print(f"User: {user_data['name']} with role: {user_data['role']}")

# Lồng f-string bên trong f-string (Nested f-strings)
items = ["apple", "banana", "cherry"]
formatted_list = f"Items: {', '.join([f'item_{i}:{item}' for i, item in enumerate(items)])}"
print(formatted_list)

# Biểu thức nhiều dòng và ký tự backslash '\' bên trong {}
names = ["Alice", "Bob", "Charlie"]
print(f"List:\n{'\n'.join([f'- {n}' for n in names])}")
