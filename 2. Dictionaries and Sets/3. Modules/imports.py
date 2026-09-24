# Cú pháp import cơ bản (import module_name)
import math
import random   # Module sinh số ngẫu nhiên
import re       # Module xử lý Regular Expressions (Biểu thức chính quy)

print("math.sqrt(36):", math.sqrt(36))        # 6.0 (Căn bậc hai float)
print("math.isqrt(36):", math.isqrt(36))      # 6 (Căn nguyên chính xác int cho số nguyên lớn)
print("random.randint(1, 10):", random.randint(1, 10))

# re.search(pattern, string, flags=0) - Tìm mẫu regex trong chuỗi (trả về match object hoặc None)
greeting = "Hello there!"
print("re.search('Hi'):", re.search('Hi', greeting))       # None
print("re.search('Hello'):", re.search('Hello', greeting)) # <re.Match object; span=(0, 5), match='Hello'>
# Tham số thứ 3 (flags): ví dụ re.IGNORECASE (hoặc re.I) để bỏ qua phân biệt hoa/thường
print("re.search('hello', ignorecase):", re.search('hello', greeting, re.IGNORECASE)) # Match 'Hello'
# Special sequences & Quantifiers:
# - \d: khớp 1 chữ số (0-9)
# - +: khớp 1 hoặc nhiều lần ký tự liền trước (vd: \d+ khớp chuỗi số '451')
book = "Fahrenheit 451"
print(r"re.search('\d'):", re.search(r'\d', book))          # Match '4' (span=(11, 12))
print(r"re.search('\d+'):", re.search(r'\d+', book))        # Match '451' (span=(11, 14))

# re.fullmatch(pattern, string) - Chỉ khớp khi TOÀN BỘ chuỗi khớp hoàn toàn với mẫu regex
print(r"re.fullmatch('\d+'):", re.fullmatch(r'\d+', book))                         # None (vì chuỗi còn có chữ 'Fahrenheit ')
print(r"re.fullmatch('Fahrenheit \d+'):", re.fullmatch(r'Fahrenheit \d+', book))  # Match 'Fahrenheit 451' (span=(0, 14))

# Đặt bí danh cho module (import module_name as alias)
import datetime as dt
birthday = dt.date(1995, 7, 15)
print(f"Date: {birthday.year}-{birthday.month}-{birthday.day}")

# dt.datetime.now(): Lấy thời gian hiện tại
# .strftime(format): Định dạng thời gian thành chuỗi (%Y: năm, %m: tháng, %d: ngày, %H: giờ, %M: phút, %S: giây)
now = dt.datetime.now()
print("Formatted Date:", now.strftime("%Y-%m-%d"))  # vd: 2026-09-05
print("Formatted Time:", now.strftime("%H:%M:%S"))  # vd: 15:48:00


# Import các hàm/hằng số cụ thể (from module_name import func)
from statistics import mean
from math import radians, sin, cos

scores = [85, 90, 78, 92]
print("statistics.mean:", mean(scores))       # 86.25
print("sin(radians(40)):", sin(radians(40))) # 0.6427876096865393

# Import với bí danh (from module import func as alias)
from math import pow as math_pow
print("math_pow(2, 4):", math_pow(2, 4))      # 16.0

# Lưu ý: Tránh dùng 'from module import *' vì dễ gây xung đột tên (namespace collision)

# Idiom: if __name__ == '__main__':
# Phân biệt khi file được chạy trực tiếp hay được import như 1 module
if __name__ == '__main__':
    print("Script dang duoc chay truc tiep!")
