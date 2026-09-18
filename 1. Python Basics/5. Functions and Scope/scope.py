# Scope (Phạm vi truy cập) xác định nơi bạn có thể sử dụng một biến trong mã nguồn.

# 1. Biến toàn cục (Global Scope)
# - Khai báo bên ngoài hàm, có thể sử dụng ở cả bên trong lẫn bên ngoài hàm.
tax_rate: float = 0.1  # Global variable

# 2. Biến cục bộ (Local Scope)
# - Biến khai báo bên trong hàm và các tham số (parameters) đều là biến cục bộ.
# - Chỉ tồn tại và sử dụng được trong lúc hàm đang thực thi.
def calculate_tax(price: float) -> float:
    tax: float = price * tax_rate  # price và tax là local variables; hàm đọc được biến global tax_rate
    return tax

# 3. Thực thi và kiểm tra phạm vi
print("Tax (50$):", calculate_tax(50.0)) # 5.0
print("Tax rate:", tax_rate)             # 0.1 (Truy cập hợp lệ từ global scope)

# 4. Lỗi NameError khi truy cập biến Local ở bên ngoài hàm
# print(tax) # NameError: name 'tax' is not defined. Did you mean: 'tax_rate'?