# Nối chuỗi (+) và Lặp chuỗi (*)
print('Hello' + ' ' + 'World')  # 'Hello World'
print('ha' * 3)                 # 'hahaha'

# Nối chuỗi với số bằng hàm str()
name, age = 'John', 26
print(name + str(age))          # 'John26'

# Định dạng chuỗi với F-string (String Interpolation - Chuẩn hiện đại)
# => TẠI SAO F-STRING LÀ LỰA CHỌN TỐT NHẤT?
#    + Nhanh hơn 2-3 lần (tính toán trực tiếp ở cấp bytecode thay vì gọi hàm format động).
#    + Dễ đọc, dễ bảo trì (biến được đặt trực tiếp bên trong chuỗi).
#    + Cho phép thực thi biểu thức toán học hoặc gọi hàm trực tiếp bên trong {}.
print(f"Name: {name}, Age: {age}") # 'Name: John, Age: 26'
print(f"5 + 10 = {5 + 10}")        # '5 + 10 = 15'