# Số nguyên (int) & Số thực (float)
a, b = 10, 3.5
print(type(a), type(b))        # <class 'int'> <class 'float'>

# Các phép toán cơ bản (+, -, *, /)
# Phép chia (/) luôn trả về float, kết hợp int + float ra float
print(a + b, a - b, a * 2, a / 2) # 13.5 6.5 20 5.0

# Phép toán nâng cao: // (chia lấy nguyên làm tròn xuống), % (chia lấy dư), ** (lũy thừa)
print(10 // 3)                 # 3 (Floor division: chia và làm tròn xuống số nguyên gần nhất)
print(10 % 3)                  # 1 (Modulo: chia lấy phần dư)
print(4 ** 2)                  # 16 (Exponentiation: lũy thừa 4^2 = 16)

# Ép kiểu dữ liệu (int, float)
print(int('45'), int(12.9))    # 45 12
print(float('7.8'), float(5))  # 7.8 5.0

# Các hàm toán học có sẵn: round, abs, pow
print(round(4.7))              # 5 (Làm tròn đến số nguyên gần nhất)
print(round(4.756, 1))         # 4.8 (Làm tròn 1 chữ số thập phân)
print(abs(-15))                # 15 (Giá trị tuyệt đối)
print(pow(2, 3))               # 8 (Tương đương 2 ** 3)
