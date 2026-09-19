# Các phép toán cơ bản (+, -, *, /) và nâng cao (// chia nguyên, % chia dư, ** lũy thừa)
a, b = 10, 3
print(a + b, a - b, a * b, a / b) # 13 7 30 3.3333333333333335 (chia / luôn ra float)
print(a // b)                     # 3 (chia lấy nguyên làm tròn xuống)
print(a % b)                      # 1 (chia lấy phần dư)
print(a ** b)                     # 1000 (10 lũy thừa 3)

# Ép kiểu dữ liệu (int, float)
print(int('45'), int(12.9))       # 45 12 (int cắt bỏ phần thập phân)
print(float('7.8'), float(5))     # 7.8 5.0

# Các hàm toán học: round (làm tròn), abs (giá trị tuyệt đối)
print(round(4.756, 2))            # 4.76 (làm tròn 2 chữ số thập phân)
print(abs(-15))                   # 15

# Phương thức is_integer(): Kiểm tra số có mang giá trị nguyên hay không
print((4.0).is_integer())         # True
print((4.5).is_integer())         # False
print((5).is_integer())           # True (Python 3.12+)

# Toán tử gán kết hợp (+=, v.v. - Lưu ý: Python không hỗ trợ ++ / --)
# Ứng dụng: Tính toán hóa đơn & chia tiền tip (Bill & Tip Splitter)
running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', round(final_bill, 2))
