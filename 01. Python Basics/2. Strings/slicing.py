s = 'Hello world'

# 1. Indexing (Dương & Âm)
print(s[0], s[-1])     # 'H' 'd'

# 2. Slicing [start:stop] (stop không bao gồm)
print(s[1:4])          # 'ell' (từ index 1 đến trước 4)
print(s[:5])           # 'Hello' (từ đầu đến trước 5)
print(s[6:])           # 'world' (từ index 6 đến hết)
print('Hello'[2:])     # 'llo' (cắt từ index 2 đến hết)

# 3. Slicing với bước nhảy [start:stop:step]
print(s[::2])          # 'Hlowrd' (bước nhảy 2)
print(s[::-1])         # 'dlrow olleH' (đảo ngược chuỗi)

# 4. Ứng dụng thực tế: Tách các trường thông tin từ mã định danh (Code parsing)
code = 'DEV-2026-JD-001'
dept = code[:3]        # 'DEV' (3 ký tự đầu - phòng ban)
year = code[4:8]       # '2026' (năm từ index 4 đến trước 8)
initials = code[9:11]  # 'JD' (viết tắt tên từ index 9 đến trước 11)
seq_num = code[-3:]    # '001' (3 ký tự cuối cùng bằng negative index)
print(f"Dept: {dept}, Year: {year}, Initials: {initials}, Num: {seq_num}")