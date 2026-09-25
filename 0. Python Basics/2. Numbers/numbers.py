# 1. Các phép toán số học cơ bản (+, -, *, /) và nâng cao (// chia nguyên, % chia dư, ** lũy thừa)
a, b = 10, 3
print(a + b, a - b, a * b, a / b) # 13 7 30 3.3333333333333335 (phép chia / luôn trả về float)
print(56 + 5.4)                   # 61.4 (kết hợp int và float luôn tự động chuyển thành float)
print(0.1 + 0.2)                  # 0.30000000000000004 (sai số dấu phẩy động do biểu diễn nhị phân)
print(-a)                         # -10 (đổi dấu số)
print(a // b)                     # 3 (chia lấy phần nguyên làm tròn xuống - floor division)
print(a % b)                      # 1 (chia lấy phần dư)
print(a ** b)                     # 1000 (10 lũy thừa 3)

# 2. Ép kiểu dữ liệu số (Type Casting: int, float)
print(int('45'), int(12.9))       # 45 12 (int cắt bỏ phần thập phân)
print(float('7.8'), float(5))     # 7.8 5.0
print((4.0).is_integer())         # True (kiểm tra float có mang giá trị nguyên không)
print((4.5).is_integer())         # False
print((5).is_integer())           # True (Python 3.12+)

# 3. Toán tử gán kết hợp (Augmented Assignment: +=, -=, *=, /=, //=, %=, **=)
total = 100
total += 25     # total = total + 25 -> 125
total *= 2      # total = total * 2  -> 250
total //= 4     # total = total // 4 -> 62
print("Augmented assignment result:", total) # 62

# 4. Các hàm toán học tích hợp sẵn (Built-in Math Functions)
print(round(4.756, 2))            # 4.76 (làm tròn 2 chữ số thập phân)
print(abs(-15))                   # 15 (giá trị tuyệt đối)

# Hàm divmod(a, b): Tính cả thương (//) và số dư (%) cùng lúc
q, r = divmod(17, 5)
print(f"divmod(17, 5): Quotient = {q}, Remainder = {r}")  # Quotient = 3, Remainder = 2

# Hàm pow(base, exp, mod): Tính lũy thừa theo modulo (base ** exp) % mod
print(pow(2, 3))                  # 8 (tương đương 2 ** 3)
print(pow(7, 100, 10))            # 1 (chữ số tận cùng của 7^100 mà không gây tràn bộ nhớ)

# Tối ưu toán học: Chuyển phép chia sang phép nhân khi so sánh giá trị trung bình
# Thay vì `val > sum(arr) / len(arr)` (dễ dính sai số float), viết: `val * len(arr) > sum(arr)`
scores = [70, 80, 90]
my_score = 85
is_better = my_score * len(scores) > sum(scores)
print("Is score better than average:", is_better)  # True

# 5. Xử lý các chữ số của một số (Digit Manipulation)
num_input = 13579
digits = [int(d) for d in str(num_input)]
print("Digits:", digits)                                    # [1, 3, 5, 7, 9]
print("Number of digits:", len(str(num_input)))             # 5
print("Sum of digits:", sum(digits))                        # 25

# 6. Hệ cơ số & Toán tử Bitwise (Dành cho xử lý nhị phân và tối ưu hiệu năng)
bin_num, hex_num = 0b1010, 0x1F       # 10 và 31

# Đổi thập phân sang chuỗi nhị phân (f-string :b)
dec_val = 11
bin_str = f"{dec_val:b}"
print("Binary string:", bin_str)      # '1011'

print(bin_num & 0b1100)               # 8 (Bitwise AND)
print(bin_num | 0b0101)               # 15 (Bitwise OR)
print(1 << 4)                         # 16 (Dịch trái 4 bit, tương đương 1 * 2^4)
print(16 >> 2)                        # 4 (Dịch phải 2 bit, tương đương 16 // 2^2)

# Kiểm tra chẵn / lẻ nhanh bằng Bitwise AND (& 1):
num_check = 42
print(f"Is {num_check} even:", not (num_check & 1))  # True

# Chuyển mảng bit [1, 0, 1, 1] sang số nguyên:
bits_arr = [1, 0, 1, 1]
bin_accum = 0
for b in bits_arr:
    bin_accum = (bin_accum << 1) | b
print(f"Binary array {bits_arr} to int:", bin_accum)  # 11

# Đếm số lượng thừa số 2 trong O(1):
val = 24  # 24 = 2^3 * 3
power_of_two = (val & -val).bit_length() - 1
print("Power of 2 in 24:", power_of_two)  # 3

# Gosper's Hack: Tìm số nguyên lớn hơn tiếp theo có cùng số lượng bit 1 trong O(1):
def next_higher_bits(n: int) -> int:
    c = n & -n
    r = n + c
    return (((r ^ n) >> 2) // c) | r

print("Next higher with same set bits (129 -> 130):", next_higher_bits(129)) # 130

# int.bit_count() (Python 3.10+): Đếm số bit 1 trong O(1)
n_sample = 1234
print(f"Bits '1' of {n_sample}:", n_sample.bit_count())    # 5
print(f"Bit length of {n_sample}:", n_sample.bit_length()) # 11

# Bộ lọc số chính phương siêu tốc bằng Bitmask:
from math import isqrt

_SQUARE_MASK = 0x2613

def is_square(n): # type: ignore
    if n < 0 or not (_SQUARE_MASK & (1 << (n & 15))):
        return False
    r = isqrt(n)
    return r * r == n # type: ignore

print("Is 144 square (Bitmask filter):", is_square(144)) # True
print("Is 145 square (Bitmask filter):", is_square(145)) # False
