# Cú pháp import cơ bản (import module_name)
import math
import random
import re

print("math.sqrt(36):", math.sqrt(36))  # 6.0 (Căn bậc hai float)
print("math.isqrt(36):", math.isqrt(36))  # 6 (Căn nguyên chính xác int cho số nguyên lớn)
print("random.randint(1, 10):", random.randint(1, 10))

# Module re - Xử lý Regular Expressions (Biểu thức chính quy)
# 1. re.search(): Tìm mẫu regex đầu tiên trong chuỗi (trả về match object hoặc None)
greeting = "Hello there!"
print("re.search('Hi'):", re.search('Hi', greeting))  # None
print("re.search('Hello'):", re.search('Hello', greeting))  # <re.Match object; span=(0, 5), match='Hello'>
# Tham số flags: re.IGNORECASE (hoặc re.I) để không phân biệt hoa/thường
print("re.search('hello', ignorecase):", re.search('hello', greeting, re.IGNORECASE))  # Match 'Hello'

# Special sequences & Quantifiers: \d (chữ số 0-9), + (lặp 1 hoặc nhiều lần)
book = "Fahrenheit 451"
print(r"re.search('\d'):", re.search(r'\d', book))  # Match '4' (span=(11, 12))
print(r"re.search('\d+'):", re.search(r'\d+', book))  # Match '451' (span=(11, 14))

# 2. re.fullmatch(): Khớp khi TOÀN BỘ chuỗi khớp hoàn toàn với mẫu regex
print(r"re.fullmatch('\d+'):", re.fullmatch(r'\d+', book))  # None (vì có chữ 'Fahrenheit ')
print(r"re.fullmatch('Fahrenheit \d+'):", re.fullmatch(r'Fahrenheit \d+', book))  # Match 'Fahrenheit 451'

# 3. re.findall(): Tìm TẤT CẢ các đoạn khớp và trả về list[str]
# Ví dụ: Chia chuỗi thành các cặp 2 ký tự (tự động bù '_' nếu độ dài lẻ):
pair_sample = "abcde"
pairs = re.findall(r".{2}", pair_sample + "_")
print("re.findall pairs (.{2}):", pairs)  # ['ab', 'cd', 'e_']

# 4. re.sub(): Thay thế chuỗi theo mẫu regex & callback function
# Ví dụ đảo ngược các từ có độ dài >= 5 ký tự mà vẫn giữ nguyên khoảng trắng:
spin_sample = "Hey fellow warriors"
spun = re.sub(r"\w{5,}", lambda m: m.group()[::-1], spin_sample)
print("re.sub spun words:", spun)  # 'Hey wollef sroirraw'

# Đặt bí danh cho module (import module_name as alias)
import datetime as dt

birthday = dt.date(1995, 7, 15)
print(f"Date: {birthday.year}-{birthday.month}-{birthday.day}")

# dt.datetime.now(): Lấy thời gian hiện tại
# .strftime(format): Định dạng thời gian (%Y: năm, %m: tháng, %d: ngày, %H: giờ, %M: phút, %S: giây)
now = dt.datetime.now()
print("Formatted Date:", now.strftime("%Y-%m-%d"))  # vd: 2026-09-05
print("Formatted Time:", now.strftime("%H:%M:%S"))  # vd: 15:48:00

# Chuẩn hiện đại: Timezone-aware Datetime với dt.UTC (Python 3.11+)
# Lưu ý: Từ Python 3.12+, dt.datetime.utcnow() đã bị deprecated vì tạo naive datetime dễ gây lỗi lệch giờ.
now_utc = dt.datetime.now(dt.UTC)
print("UTC Time (Python 3.11+ aware):", now_utc.strftime("%Y-%m-%d %H:%M:%S %Z"))

# Import các hàm/hằng số cụ thể (from module_name import func / as alias)
# Gọi trực tiếp tên hàm giúp tránh bước tra cứu qua dấu chấm (attribute lookup: module.func)
from statistics import mean
from math import radians, sin
from math import pow as math_pow

scores = [85, 90, 78, 92]
print("statistics.mean:", mean(scores))  # 86.25
print("sin(radians(40)):", sin(radians(40)))  # 0.6427876096865393

# Lưu ý: math.pow() luôn trả về float (16.0), còn built-in pow(2, 4) trả về int (16) và hỗ trợ tham số thứ 3 modulo.
print("math_pow(2, 4):", math_pow(2, 4))  # 16.0

# Lưu ý: Tránh dùng 'from module import *' vì dễ gây xung đột tên (namespace collision)


# Idiom: if __name__ == '__main__':
# Phân biệt khi file được chạy trực tiếp hay được import như 1 module
if __name__ == '__main__':
    print("Script dang duoc chay truc tiep!")
