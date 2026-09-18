# Khai báo biến (Toán tử gán '=')
user_name = 'John Doe'
user_age = 25
total_score = 100

# Quy tắc đặt tên biến (Rules):
# - Bắt đầu bằng chữ cái hoặc dấu gạch dưới (_), KHÔNG bắt đầu bằng số (ví dụ '5name' gây SyntaxError).
# - Chỉ chứa chữ cái (a-z, A-Z), chữ số (0-9) và dấu gạch dưới (_).
# - Phân biệt hoa/thường (Case-sensitive): age, Age, AGE là các biến hoàn toàn khác nhau.
# - Không trùng với từ khóa của Python (reserved keywords như: if, class, def, v.v.).

# Quy ước đặt tên (Conventions):
# - Dùng snake_case: các từ viết thường nối nhau bởi dấu gạch dưới (ví dụ: my_variable_name, user_age).
# - Đặt tên biến rõ nghĩa, tránh dùng tên 1 ký tự (như x = 56) vì không truyền tải được mục đích dữ liệu.

# Comments trong Python:
# - Dùng dấu '#' cho comment đơn dòng (Python sẽ bỏ qua toàn bộ phần sau dấu '#' trên dòng đó).
# - Comment nhiều dòng được tạo bằng nhiều dòng '#' liên tiếp.

# In dữ liệu ra màn hình với hàm print()
# - Chuỗi có thể đặt trong dấu nháy đơn ('...') hoặc nháy kép ("...").
# - Phân tách nhiều giá trị bằng dấu phẩy, print() tự động chèn khoảng trắng ở giữa:
print('Hello world!')
print('My favorite colors are', 'blue', 'green', 'red')
print('User info:', user_name, user_age, total_score)

# Kiểu dữ liệu động (Dynamically-typed):
# - Python tự nhận diện kiểu dữ liệu dựa trên giá trị được gán.
# - Biến có thể được gán lại bằng giá trị thuộc kiểu dữ liệu khác:
dynamic_var = 25             # Khởi tạo kiểu int
print('Initial value:', dynamic_var)

dynamic_var = 'Twenty-five'  # Gán lại kiểu str
print('Reassigned value:', dynamic_var)

# 4 kiểu dữ liệu cơ bản trong Python:
my_integer_var = 10          # Integer (Số nguyên không có phần thập phân: 10, -5)
my_float_var = 4.50          # Float (Số thực có phần thập phân: 4.50, -0.4)
my_string_var = 'hello'      # String (Chuỗi ký tự đặt trong cặp nháy đơn hoặc kép)
my_boolean_var = True        # Boolean (Kiểu logic chỉ nhận True hoặc False)
empty_val = None             # NoneType (Đại diện cho giá trị rỗng / không có)

print('Integer:', my_integer_var)
print('Float:', my_float_var)
print('String:', my_string_var)
print('Boolean:', my_boolean_var)
print('None:', empty_val)