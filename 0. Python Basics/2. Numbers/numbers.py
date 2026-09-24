# Các phép toán cơ bản (+, -, *, /) và nâng cao (// chia nguyên, % chia dư, ** lũy thừa)
a, b = 10, 3
print(a + b, a - b, a * b, a / b) # 13 7 30 3.3333333333333335 (chia / luôn ra float)
print(a // b)                     # 3 (chia lấy nguyên làm tròn xuống)
print(a % b)                      # 1 (chia lấy phần dư)
print(a ** b)                     # 1000 (10 lũy thừa 3)

# Tối ưu toán học: Chuyển phép chia (/) sang phép nhân (*) khi so sánh
# Thay vì `val > sum(arr) / len(arr)` (dễ dính sai số float precision & tốn chu kỳ CPU),
# biến đổi thành: `val * len(arr) > sum(arr)` (giữ nguyên độ chính xác int tuyệt đối)
scores = [70, 80, 90]
my_score = 85
is_better = my_score * len(scores) > sum(scores)
print("Is score better than average:", is_better)  # True


# Ép kiểu dữ liệu (int, float)
print(int('45'), int(12.9))       # 45 12 (int cắt bỏ phần thập phân)
print(float('7.8'), float(5))     # 7.8 5.0

# Hàm divmod(a, b) - Tính cả thương (//) và số dư (%) trong 1 chỉ lệnh CPU duy nhất:
q, r = divmod(17, 5)
print(f"divmod(17, 5): Quotient = {q}, Remainder = {r}")  # Quotient = 3, Remainder = 2

# Chuyển đổi số thành danh sách các chữ số (Nhanh & Tinh gọn với C-level map + unpacking):
digits = [*map(int, str(13579))]
print("Digits:", digits)                                    # [1, 3, 5, 7, 9]

# Lấy số lượng chữ số nhanh nhất (O(1) struct access qua C level):
num_digits = len(str(13579))
print("Number of digits:", num_digits)                      # 5

# Tính tổng các chữ số trong chuỗi nhanh nhất (nhanh gấp ~10 lần so với sum(map(int, s))):
# Thay vì ép từng ký tự sang int, tính tổng mã ASCII bằng C rồi trừ 48 * len(s) đúng 1 lần duy nhất:
digit_str = "13579"
sum_digits_fast = sum(digit_str.encode()) - 48 * len(digit_str)
print("Fastest digit sum:", sum_digits_fast)                # 25 (1 + 3 + 5 + 7 + 9)




# Các hàm toán học: round (làm tròn), abs (giá trị tuyệt đối)
print(round(4.756, 2))            # 4.76 (làm tròn 2 chữ số thập phân)
print(abs(-15))                   # 15

# Hàm pow(base, exp, mod) - Tính lũy thừa theo modulo: (base ** exp) % mod
# Thuật toán Modular Exponentiation O(log exp): tính cực nhanh, không gây tràn bộ nhớ với số mũ khổng lồ
print(pow(2, 3))                  # 8 (tương đương 2 ** 3)
print(pow(7, 100, 10))            # 1 (tìm chữ số tận cùng của 7^100 mà không cần tính ra số khổng lồ)

# Tính tổng tất cả các lũy thừa a^0 + a^1 + ... + a^n nhanh nhất (Cấp số nhân O(1)):
# Thay vì chạy vòng lặp O(n), áp dụng công thức: (a^(n+1) - 1) // (a - 1)
base, max_exp = 2, 4  # 2^0 + 2^1 + 2^2 + 2^3 + 2^4 = 1 + 2 + 4 + 8 + 16 = 31
sum_powers_fast = (pow(base, max_exp + 1) - 1) // (base - 1) if base != 1 else max_exp + 1
print(f"Sum of powers (2^0 to 2^{max_exp}):", sum_powers_fast)  # 31


# Phương thức is_integer(): Kiểm tra số có mang giá trị nguyên hay không
print((4.0).is_integer())         # True
print((4.5).is_integer())         # False
print((5).is_integer())           # True (Python 3.12+)

# Hệ cơ số (Nhị phân 0b, Thập lục phân 0x) & Toán tử Bitwise (&, |, ^, ~, <<, >>)
bin_num, hex_num = 0b1010, 0x1F       # 10 và 31
print(bin_num & 0b1100)               # 8 (0b1000 - Bitwise AND)
print(bin_num | 0b0101)               # 15 (0b1111 - Bitwise OR)
print(1 << 4)                         # 16 (Dịch trái 4 bit, tương đương 1 * 2^4)
print(16 >> 2)                        # 4 (Dịch phải 2 bit, tương đương 16 // 2^2)

# Bitwise Trick: Đếm số lượng thừa số 2 trong O(1) không cần vòng lặp while:
# (n & -n) trích xuất bit 1 thấp nhất (Lowest Set Bit), .bit_length() - 1 cho ra số mũ của 2
val = 24  # 24 = 2^3 * 3
power_of_two = (val & -val).bit_length() - 1
print("Power of 2 in 24:", power_of_two)  # 3 (2^3 = 8 chia hết cho 24)

# Kỹ thuật Bitmask Set & int.bit_count() (Python 3.10+ POPCNT Hardware Instruction):
# - Dùng số nguyên thay thế cấu trúc `set()` để lưu trữ trạng thái xuất hiện với O(1) Memory tuyệt đối.
# - int.bit_count() dùng chỉ lệnh phần cứng vi xử lý (POPCNT) đếm số bit 1 trong vài nano giây.
text_bytes = b"indivisibility"
seen_mask, dup_mask = 0, 0
for byte in text_bytes:
    m = 1 << byte
    dup_mask |= seen_mask & m   # Bật bit nếu đã thấy trước đó
    seen_mask |= m              # Đánh dấu bit đã xuất hiện
print("Unique duplicate chars count (bit_count):", dup_mask.bit_count()) # 1 (chữ 'i')



# Toán tử gán kết hợp (Augmented Assignment: +=, -=, *=, /=, //=, %=, **=)
# Lưu ý: Python không hỗ trợ toán tử ++ hoặc -- như C/C++/Java
total = 100
total += 25     # tương đương total = total + 25 -> 125
total *= 2      # tương đương total = total * 2  -> 250
total //= 4     # tương đương total = total // 4 -> 62
print("Augmented assignment result:", total) # 62

