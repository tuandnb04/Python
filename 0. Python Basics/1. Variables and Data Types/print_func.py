# In chuỗi đơn giản ra màn hình
print('Hello world!')

# In nhiều giá trị (ngăn cách bằng dấu phẩy, Python tự chèn khoảng trắng ở giữa)
print('My favorite colors are', 'blue', 'green', 'red')
print('Hello', 'world!') # 'Hello world!'

# Xuất dữ liệu qua luồng sys.stdout.write() (Cấp độ thấp hơn print)
# - sys.stdout.write() KHÔNG tự động thêm ký tự xuống dòng (\n) hay khoảng trắng.
# - Chỉ nhận một đối số duy nhất là chuỗi (str).
import sys

name, age, score = 'Alice', 20, 80.5
sys.stdout.write(
    f"Name: {name} ({type(name).__name__})\n"
    f"Age: {age} ({type(age).__name__})\n"
    f"Score is float: {isinstance(score, float)}\n"
)