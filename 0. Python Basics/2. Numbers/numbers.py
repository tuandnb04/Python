# 1. Các phép toán số học cơ bản (+, -, *, /) và nâng cao (// chia nguyên, % chia dư, ** lũy thừa)
a, b = 10, 3
print(a + b, a - b, a * b, a / b)  # 13 7 30 3.3333333333333335 (phép chia / luôn trả về float)
print(56 + 5.4)  # 61.4 (kết hợp int và float luôn tự động chuyển thành float)
print(0.1 + 0.2)  # 0.30000000000000004 (sai số dấu phẩy động do biểu diễn nhị phân)
print(-a)  # -10 (đổi dấu số)
print(a // b)  # 3 (chia lấy phần nguyên làm tròn xuống - floor division)
print(a % b)  # 1 (chia lấy phần dư)
print(a ** b)  # 1000 (10 lũy thừa 3)

# 2. Ép kiểu & Các kiểu dữ liệu số (int, float, complex)
print(int('45'), int(12.9))  # 45 12 (int cắt bỏ phần thập phân)
print(float('7.8'), float(5))  # 7.8 5.0
print((4.0).is_integer())  # True (kiểm tra float có mang giá trị nguyên không)
print((4.5).is_integer())  # False
print((5).is_integer())  # True

# Số thực dạng khoa học (Scientific notation với 'e' hoặc 'E' biểu thị lũy thừa 10):
sci_num = 35e3  # 35 * 10^3 = 35000.0 (luôn mang kiểu float)
print("Scientific notation (35e3):", sci_num)  # 35000.0

# Số phức (Complex numbers: int/float + phần ảo với chữ cái 'j')
z = 3 + 4j
z_from_func = complex(3, 4)
print("Complex number:", z)  # (3+4j)
print("Real part (.real):", z.real)  # 3.0 (phần thực)
print("Imaginary part (.imag):", z.imag)  # 4.0 (phần ảo)
print("Complex conjugate:", z.conjugate())  # (3-4j) (số phức liên hợp)
# Lưu ý: Có thể ép int/float -> complex (complex(5) -> 5+0j), nhưng KHÔNG THỂ ép ngược complex -> int/float (sẽ báo TypeError)



# 3. Toán tử gán kết hợp (Augmented Assignment: +=, -=, *=, /=, //=, %=, **=)
total = 100
total += 25  # 125 (total = total + 25)
total -= 15  # 110 (total = total - 15)
total *= 2   # 220 (total = total * 2)
total /= 4   # 55.0 (total = total / 4 - phép chia luôn trả về float)
total //= 5  # 11.0 (total = total // 5)
total %= 4   # 3.0 (total = total % 4)
total **= 3  # 27.0 (total = total ** 3)
print("Augmented assignment result:", total)  # 27.0

# 4. Các hàm toán học tích hợp sẵn (Built-in Math Functions)
print(round(4.756, 2))  # 4.76 (làm tròn 2 chữ số thập phân)
print(abs(-15))  # 15 (giá trị tuyệt đối)

# Hàm divmod(a, b): Tính cả thương (//) và số dư (%) cùng lúc
q, r = divmod(17, 5)
print(f"divmod(17, 5): Quotient = {q}, Remainder = {r}")  # Quotient = 3, Remainder = 2

# Hàm pow(base, exp, mod): Tính lũy thừa theo modulo (base ** exp) % mod
print(pow(2, 3))  # 8
print(pow(7, 100, 10))  # 1 (chữ số tận cùng của 7^100 mà không gây tràn bộ nhớ)

# Tối ưu toán học: Chuyển phép chia sang phép nhân khi so sánh giá trị trung bình
# Thay vì `my_score > (score1 + score2 + score3) / 3` (dễ dính sai số float),
# viết dưới dạng nhân: `my_score * 3 > score1 + score2 + score3`
score1, score2, score3 = 70, 80, 90
count = 3
my_score = 85
is_better = my_score * count > (score1 + score2 + score3)
print("Is score better than average:", is_better)  # True

# 5. Xử lý các chữ số của một số bằng toán tử số học (Digit Manipulation)
# Lấy chữ số cuối cùng bằng chia dư (%), loại bỏ chữ số cuối bằng chia nguyên (//):
num_input = 13579
last_digit = num_input % 10  # 9 (hàng đơn vị)
remaining = num_input // 10  # 1357 (phần còn lại)
second_last = remaining % 10  # 7 (hàng chục)
print("Last digit (n % 10):", last_digit)
print("Remaining (n // 10):", remaining)
print("Second to last:", second_last)

# 6. Hệ cơ số & Toán tử Bitwise (Bitwise Operators)
# Làm việc trực tiếp trên từng bit nhị phân của số nguyên:
# - '&'  (AND) : Đặt bit là 1 nếu CẢ HAI bit đều là 1
# - '|'  (OR)  : Đặt bit là 1 nếu ÍT NHẤT MỘT trong hai bit là 1
# - '^'  (XOR) : Đặt bit là 1 nếu CHỈ CÓ MỘT trong hai bit là 1 (khác nhau thì bằng 1)
# - '~'  (NOT) : Đảo ngược toàn bộ bit (~x tương đương công thức -(x + 1) theo chuẩn bù 2)
# - '<<' (Zero-fill Left Shift) : Dịch các bit sang trái, điền số 0 vào bên phải (x << n tương đương x * 2^n)
# - '>>' (Signed Right Shift)   : Dịch các bit sang phải (x >> n tương đương x // 2^n)

# Minh họa chi tiết cấp độ bit với 6 (0b0110) và 3 (0b0011):
x_bit, y_bit = 6, 3  # 6 = 0b0110, 3 = 0b0011
print("Bitwise AND (6 & 3):       ", x_bit & y_bit)   # 2  (0b0010)
print("Bitwise OR  (6 | 3):       ", x_bit | y_bit)   # 7  (0b0111)
print("Bitwise XOR (6 ^ 3):       ", x_bit ^ y_bit)   # 5  (0b0101)
print("Bitwise NOT (~6):          ", ~x_bit)          # -7 (-(6 + 1))
print("Bitwise Left Shift (6 << 2):", x_bit << 2)     # 24 (6 * 2^2 = 24 -> 0b011000)
print("Bitwise Right Shift (6 >> 1):", x_bit >> 1)    # 3  (6 // 2^1 = 3 -> 0b0011)

# Chuyển đổi hệ cơ số & In dạng chuỗi nhị phân:
bin_num, hex_num = 0b1010, 0x1F  # 10 và 31
dec_val = 11
print("Binary string (11 to :b):  ", f"{dec_val:b}")   # '1011'

# Toán tử gán Bitwise kết hợp (&=, |=, ^=, >>=, <<=):
bit_val = 0b1010   # 10
bit_val &= 0b1100  # 8  (tương đương bit_val = bit_val & 0b1100)
bit_val |= 0b0011  # 11 (tương đương bit_val = bit_val | 0b0011)
bit_val ^= 0b0001  # 10 (tương đương bit_val = bit_val ^ 0b0001)
bit_val <<= 2      # 40 (tương đương bit_val = bit_val << 2)
bit_val >>= 1      # 20 (tương đương bit_val = bit_val >> 1)
print("Bitwise assignment result:", bit_val)  # 20

# Kiểm tra chẵn / lẻ nhanh bằng Bitwise AND (& 1):
num_check = 42
print(f"Is {num_check} even:", not (num_check & 1))  # True

# Đếm số lượng thừa số 2 trong O(1):
val = 24  # 24 = 2^3 * 3
power_of_two = (val & -val).bit_length() - 1
print("Power of 2 in 24:", power_of_two)  # 3

# int.bit_count(): Đếm số bit 1 trong O(1)
n_sample = 1234
print(f"Bits '1' of {n_sample}:", n_sample.bit_count())  # 5
print(f"Bit length of {n_sample}:", n_sample.bit_length())  # 11

# Kiểm tra số chính phương bằng lũy thừa số học:
check_num = 144
sqrt_val = int(check_num ** 0.5)
is_square = (sqrt_val * sqrt_val == check_num)
print("Is 144 square:", is_square)  # True

# 7. Thứ tự ưu tiên của toán tử (Operator Precedence & Associativity)
# Bảng thứ tự ưu tiên từ cao xuống thấp (Precedence Table):
# 1. ()                       : Dấu ngoặc đơn (Parentheses) - Cao nhất
# 2. **                       : Lũy thừa (Exponentiation)
# 3. +x, -x, ~x               : Dấu đơn (Unary plus/minus) và đảo bit (Bitwise NOT)
# 4. *, /, //, %              : Nhân, chia thực, chia nguyên, chia dư
# 5. +, -                     : Phép cộng, phép trừ
# 6. <<, >>                   : Dịch bit trái / phải
# 7. &                        : Bitwise AND
# 8. ^                        : Bitwise XOR
# 9. |                        : Bitwise OR
# 10. ==, !=, >, >=, <, <=    : Toán tử so sánh, Identity (is, is not), Membership (in, not in)
# 11. not                     : Phủ định logic
# 12. and                     : Logic AND
# 13. or                      : Logic OR - Thấp nhất

# 1. Dấu ngoặc () có độ ưu tiên cao nhất, luôn được tính trước:
print("Parentheses priority:", (6 + 3) - (6 + 3))   # (9) - (9) = 0

# 2. Phép nhân (*) ưu tiên cao hơn phép cộng (+):
print("Multiply over add:", 100 + 5 * 3)           # 100 + 15 = 115

# 3. Quy tắc kết hợp từ trái sang phải (Left-to-Right evaluation):
# Khi các toán tử có cùng mức ưu tiên (như + và -):
print("Left-to-right (+ and -):", 5 + 4 - 7 + 3)   # ((5 + 4) - 7) + 3 = 5

# 4. Ngoại lệ quan trọng - Lũy thừa (**) kết hợp từ phải sang trái (Right-to-Left):
# 2 ** 3 ** 2 được tính là 2 ** (3 ** 2) = 2 ** 9 = 512 (chứ không phải (2 ** 3) ** 2 = 64):
print("Right-to-left power (2 ** 3 ** 2):", 2 ** 3 ** 2)  # 512

# 5. Phối hợp giữa lũy thừa (**), dấu âm đơn (-) và phép dịch bit / cộng:
# -3 ** 2 được tính là -(3 ** 2) = -9 vì lũy thừa (**) có độ ưu tiên cao hơn dấu âm đơn (-)
print("Unary minus vs power (-3 ** 2):    ", -3 ** 2)        # -9
print("Parentheses override ((-3) ** 2):  ", (-3) ** 2)      # 9
# Phép cộng (+) có độ ưu tiên cao hơn phép dịch bit (<<):
print("Shift vs Add (1 << 2 + 3):         ", 1 << 2 + 3)    # 32 (tính 2 + 3 = 5, rồi 1 << 5 = 32)
