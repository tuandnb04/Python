import sys

# Khai báo biến (Toán tử gán '=')
user_name = 'John Doe'
user_age = 25
total_score = 100

# Quy tắc đặt tên biến (Rules):
# - Bắt đầu bằng chữ cái hoặc dấu gạch dưới (_), KHÔNG bắt đầu bằng số (ví dụ '5name' sẽ gây SyntaxError).
# - Chỉ chứa chữ cái (a-z, A-Z), chữ số (0-9) và dấu gạch dưới (_).
# - Phân biệt hoa/thường (Case-sensitive): age, Age, AGE là các biến hoàn toàn khác nhau.
# - Không trùng với từ khóa của Python (reserved keywords như: if, class, def, v.v.).

# Quy ước đặt tên (Conventions):
# - Dùng snake_case: các từ viết thường nối nhau bởi dấu gạch dưới (ví dụ: my_variable_name, user_age).
# - Đặt tên biến rõ nghĩa, tránh dùng tên 1 ký tự (như x = 56) vì không truyền tải được mục đích dữ liệu.

# Comments trong Python:
# - Dùng dấu '#' cho comment đơn dòng (Python sẽ bỏ qua toàn bộ phần sau dấu '#' trên dòng đó).
# - Comment nhiều dòng được tạo bằng nhiều dòng '#' liên tiếp.

# In dữ liệu cơ bản ra màn hình với print()
# - Chuỗi có thể dùng nháy đơn ('...') hoặc nháy kép ("...").
# - Nhiều đối số phân tách bởi dấu phẩy sẽ được tự động chèn khoảng trắng ở giữa:
print('Hello world!')
print('My favorite colors are', 'blue', 'green', 'red')
print('User info:', user_name, user_age, total_score)

# Xuất dữ liệu qua luồng sys.stdout.write() (Cấp thấp hơn print)
# - Không tự động thêm ký tự xuống dòng (\n) hay khoảng trắng.
# - Tham số truyền vào bắt buộc phải là chuỗi (str).
sys.stdout.write(f"[stdout] User: {user_name} | Age: {user_age}\n")

# Kiểu dữ liệu động (Dynamically-typed):
# - Python tự xác định kiểu dựa trên giá trị được gán.
# - Biến có thể gán lại bằng giá trị thuộc kiểu dữ liệu khác bất cứ lúc nào:
dynamic_var = 25             # Lúc này mang kiểu int
dynamic_var = 'Twenty-five'  # Đổi sang kiểu str hợp lệ

# Các kiểu dữ liệu cơ bản (Primitive Types) & Giá trị rỗng
num_int = 10                       # int (Số nguyên không có phần thập phân: 10, -5)
num_float = 4.5                    # float (Số thực có phần thập phân: 4.50, -0.4)
text = 'hello'                     # str (Chuỗi ký tự)
is_valid = True                    # bool (Giá trị logic True hoặc False)
empty_val = None                   # NoneType (Đại diện cho giá trị rỗng / không có)

# Tập hợp (Collections) & Trình tự (Sequences)
items_list = [22, 'hello', True]   # list (Danh sách có thứ tự, mutable)
items_tuple = (7, 'hello', 8.5)    # tuple (Bộ dữ liệu cố định, immutable)
items_set = {7, 'hello', 8.5}      # set (Tập hợp các phần tử duy nhất)
user_dict = {'name': 'Alice', 'age': 25} # dict (Từ điển ánh xạ key-value)
num_range = range(5)               # range (Dãy số tuần tự)

print("Primitives:", num_int, num_float, text, is_valid, empty_val)
print("Collections:", items_list, items_tuple, items_set, user_dict, list(num_range))