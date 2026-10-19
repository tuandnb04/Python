# 1. Từ khóa import & Module tích hợp sẵn (math)
# Dùng từ khóa import để nạp module. Sau khi import, truy cập hàm hoặc hằng số qua tên module:
import math

p = math.pi
print("math.pi:", p)
# math.sqrt(x): Căn bậc hai (chỉ nhận số >= 0, luôn trả về float)
print("math.sqrt(16):", math.sqrt(16))  # 4.0
print("math.sqrt(10):", math.sqrt(10))  # 3.1622776601683795

# Làm tròn: floor (xuống) và ceil (lên)
print("math.floor(3.9):", math.floor(3.9))    # 3 (làm tròn xuống)
print("math.floor(-2.1):", math.floor(-2.1))  # -3
print("math.ceil(3.1):", math.ceil(3.1))      # 4 (làm tròn lên)
print("math.ceil(-2.9):", math.ceil(-2.9))    # -2

# math.pow(x, y) vs toán tử **:
# math.pow() luôn trả về float; toán tử ** giữ nguyên kiểu int chính xác tuyệt đối với số rất lớn
print("math.pow(2, 3):", math.pow(2, 3))  # 8.0 (float)
print("Operator 2 ** 3:", 2 ** 3)         # 8 (int)

# 2. Import trực tiếp thành phần cụ thể (from module import ...)
# Gọi trực tiếp không cần tiền tố math. Có thể import nhiều mục cùng lúc:
from math import pi, sqrt

print("pi:", pi)
print("sqrt(25):", sqrt(25))

# 3. Đặt bí danh (as - alias)
# Rút gọn tên gọi cho module (như np, pd, plt) hoặc thành phần cụ thể:
import math as m
from math import sqrt as s

print("m.pi:", m.pi)
print("s(64):", s(64))

# 4. Thư viện sinh số ngẫu nhiên (random)
# Tích hợp sẵn trong Python, không cần cài đặt:
import random

print("random.random():", random.random())              # Số thực trong khoảng [0.0, 1.0)
print("random.randint(1, 10):", random.randint(1, 10))  # Số nguyên từ 1 đến 10 (bao gồm cả 1 và 10)
print("random.uniform(1, 10):", random.uniform(1, 10))  # Số thực trong khoảng [1.0, 10.0]
fruits = ["apple", "banana", "cherry"]
print("random.choice(fruits):", random.choice(fruits))  # Chọn ngẫu nhiên 1 phần tử từ danh sách

# random.choices(): Lấy mẫu có trọng số (weights) và có hoàn lại
days = ["Mon", "Tue"]
print("random.choices(weights=[3, 1]):", random.choices(days, weights=[3, 1], k=10))

# random.sample(): Lấy mẫu không hoàn lại (không trùng phần tử), k <= len(danh sách)
numbers = [1, 2, 3, 4, 5]
print("random.sample(k=4):", random.sample(numbers, k=4))

# 5. Thư viện bên ngoài (Third-party packages) & công cụ pip
# Dùng lệnh terminal: pip install numpy để cài đặt thư viện vào môi trường
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("numpy array:", arr)
print("array type:", type(arr))

# 6. Khối kiểm tra if __name__ == "__main__":
# Đoạn mã trong khối này chỉ chạy khi thực thi trực tiếp file, bỏ qua nếu bị file khác import:
if __name__ == "__main__":
    print("Script is running directly!")
