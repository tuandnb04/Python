import sys

# Khai báo biến (Toán tử gán '=')
user_name = 'John Doe'
user_age = 25
total_score = 100

# Quy tắc đặt tên biến (Rules):
# - Bắt đầu bằng chữ cái hoặc dấu gạch dưới (_), không bắt đầu bằng số.
# - Chỉ chứa chữ cái (a-z, A-Z), chữ số (0-9) và dấu gạch dưới (_).
# - Phân biệt hoa/thường (Case-sensitive): age, Age, AGE là các biến khác nhau.
# - Không trùng với từ khóa của Python (reserved keywords như: if, class, def, v.v.).

# Quy ước đặt tên (Conventions):
# - Dùng snake_case: các từ viết thường nối nhau bởi dấu gạch dưới (_).
# - Đặt tên biến rõ nghĩa, tránh đặt 1 ký tự khó hiểu.

# In dữ liệu cơ bản ra màn hình
print("Hello world!")
print("User info:", user_name, user_age, total_score)

# Xuất dữ liệu qua luồng sys.stdout.write() (Cấp thấp hơn print)
# - sys.stdout.write() không tự động thêm ký tự xuống dòng (\n) hay khoảng trắng.
# - Tham số truyền vào bắt buộc phải là chuỗi (str).
sys.stdout.write(f"[stdout] User: {user_name} | Age: {user_age}\n")

# Các kiểu dữ liệu phổ biến trong Python (Dynamically-typed):

# Kiểu nguyên thủy (Primitive Types) & Giá trị rỗng
num_int = 10                       # int (Số nguyên)
num_float = 4.5                    # float (Số thực)
text = 'hello'                     # str (Chuỗi)
is_valid = True                    # bool (True / False)
empty_val = None                   # NoneType (Không có giá trị)

# Tập hợp (Collections) & Trình tự (Sequences)
items_list = [22, 'hello', True]   # list (Có thứ tự, mutable)
items_tuple = (7, 'hello', 8.5)    # tuple (Có thứ tự, immutable)
items_set = {7, 'hello', 8.5}      # set (Tập hợp không trùng lặp)
user_dict = {'name': 'Alice', 'age': 25} # dict (Cặp key-value)
num_range = range(5)               # range (Dãy số 0 -> 4)

print("Primitives:", num_int, num_float, text, is_valid, empty_val)
print("Collections:", items_list, items_tuple, items_set, user_dict, list(num_range))