# Khai báo chuỗi (Đơn, đôi, multiline)
s = "Hello world"
multiline1 = """Line 1
Line 2"""
multiline2 = '''Line 1
Line 2'''                       # Dùng 3 dấu nháy đơn

# Lồng dấu nháy: Dùng nháy ngược loại hoặc ký tự thoát \
quote1 = "It's a sunny day"
quote2 = 'It\'s a sunny day'    # Escape nháy đơn
quote3 = "She said: \"Hello!\"" # Escape nháy kép

# Kiểm tra (in), độ dài (len) & Indexing
print('Hello' in s, 'xyz' in s) # True False
print(len(s))                   # 11

print(s[0], s[-1])              # 'H' 'd' (indexing dương và âm)

# Lưu ý với hàm len()
print(len("a b"))               # 3 (tính cả dấu cách)
print(len("hello\n"))           # 6 (tính cả ký tự thoát \n)
print(len("😊"))                # 1 (emoji là 1 Unicode code point)
print(len(""))                  # 0 (chuỗi rỗng)

# Ký tự (Unicode code points) vs Số byte bộ nhớ
# len() đếm số ký tự, dùng .encode() để đếm số byte thực tế
s_vn = "chào"
print(len(s_vn))                 # 4 ký tự
print(len(s_vn.encode("utf-8"))) # 5 bytes (ký tự 'à' tốn 2 bytes trong UTF-8)

# Cắt lát chuỗi (Slicing [start:stop])
print(s[1:4])          # 'ell' (từ index 1 đến trước 4)
print(s[:5])           # 'Hello' (từ đầu đến trước 5)
print(s[6:])           # 'world' (từ index 6 đến hết)
print('Hello'[2:])     # 'llo' (cắt từ index 2 đến hết)

# Slicing với bước nhảy [start:stop:step]
print(s[::2])          # 'Hlowrd' (bước nhảy 2)
print(s[::-1])         # 'dlrow olleH' (đảo ngược chuỗi)

# Ví dụ: Cắt chuỗi theo khoảng index [start:stop]
code = 'DEV-2026-JD-001'
dept = code[:3]        # 'DEV' (3 ký tự đầu)
year = code[4:8]       # '2026' (từ index 4 đến trước 8)
initials = code[9:11]  # 'JD'
seq_num = code[-3:]    # '001' (3 ký tự cuối cùng)
print(f"Dept: {dept}, Year: {year}, Initials: {initials}, Num: {seq_num}")


# Tính bất biến (Immutability): str, int, float, bool đều là immutable
# Chuỗi có thể gán lại nhưng không thể sửa đổi từng ký tự tại chỗ
greeting = 'hi'
greeting = 'hello'              # Hợp lệ (reassignment)
# greeting[0] = 'H'             # TypeError: 'str' object does not support item assignment
print(greeting)                 # 'hello'
