# Toán tử gán kết hợp với số (+=, -=, *=, /=, //=, %=, **=)
num = 10
num += 5       # 15 (num = num + 5)
num *= 2       # 30 (num = num * 2)
num **= 2      # 900 (num = num ** 2)
print(num)     # 900

# Gán kết hợp với chuỗi (+ nối chuỗi, * lặp chuỗi)
text = 'Hello'
text += ' World'
text *= 2
print(text)    # 'Hello WorldHello World'

# Python không hỗ trợ ++ / -- (phải dùng += 1 hoặc -= 1)
x = 5
print(++x)     # 5 (chỉ là toán tử dấu unary, không tăng giá trị)
x += 1
print(x)       # 6

# Ứng dụng thực tế: Tính toán hóa đơn & chia tiền tip (Bill & Tip Splitter)
running_total = 0.0
running_total += (37.89 + 57.34 + 39.39 + 64.21)  # Cộng dồn các món ăn vào tổng (+=)
tip = running_total * 0.25                         # Tiền tip 25%
total_with_tip = running_total + tip               # Tổng bill gồm tip
each_pays = round(total_with_tip / 4, 2)           # Chia đều cho 4 người và làm tròn 2 chữ số
print(f"Total bill: {total_with_tip:.2f} | Each pays: {each_pays}")
