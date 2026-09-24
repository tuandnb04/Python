text = '  hello world  '

# Biến đổi chữ hoa / thường
s = 'hello world'
print(s.upper())       # 'HELLO WORLD'
print(s.lower())       # 'hello world'
print(s.capitalize())  # 'Hello world'
print(s.title())       # 'Hello World'

# Phân biệt capitalize() vs title() với từ có dấu nháy đơn hoặc ký tự đặc biệt:
# - title(): Viết hoa sau mọi ký tự không phải chữ cái (kể cả dấu nháy đơn: "they're" -> "They'Re").
# - capitalize(): Chỉ viết hoa ký tự đầu tiên của chuỗi ("they're" -> "They're").
contraction = "they're"
print(contraction.title())       # "They'Re"  (lỗi chính tả do viết hoa sau dấu nháy)
print(contraction.capitalize())  # "They're"  (chuẩn ngữ pháp)


# Cắt khoảng trắng & Thay thế
print(text.strip())                # 'hello world'
print(s.replace('hello', 'hi'))    # 'hi world'
# str.maketrans('abc', '123')      # Tạo bảng dịch 1-1 ký tự (dùng với s.translate())

# Tách (split) & Nối (join)
words = s.split()                  # ['hello', 'world']
print(words)
print('-'.join(words))             # 'hello-world'

# Tách dòng: splitlines() vs split('\n') vs split()
poem = "Hello world\nPython code\n"
print(poem.splitlines())        # ['Hello world', 'Python code'] (Chuẩn nhất: tự bỏ dòng trống ở cuối)
print(poem.splitlines(True))    # ['Hello world\n', 'Python code\n'] (keepends=True: giữ ký tự \n)
print(poem.split('\n'))         # ['Hello world', 'Python code', ''] (Thừa '' ở cuối nếu có \n)
print(poem.split())             # ['Hello', 'world', 'Python', 'code'] (Tách theo từng từ)

# Tìm kiếm, Đếm & Kiểm tra tiền tố/hậu tố
print(s.find('world'))             # 6 (trả về -1 nếu không thấy)
print(s.count('o'))                # 2
print(s.startswith('hello'))       # True
print(s.endswith('world'))         # True
print(s.endswith('N'))             # False (câu hỏi trắc nghiệm)

# Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())    # False True

# Phân biệt các hàm kiểm tra số: isdecimal() vs isdigit() vs isnumeric()
# - isdecimal(): Chỉ chữ số thập phân chuẩn (0-9). An toàn nhất khi ép kiểu int()!
# - isdigit(): Gồm cả số mũ (ví dụ: '²'.isdigit() -> True, nhưng int('²') văng ValueError).
# - isnumeric(): Gồm cả phân số Unicode (ví dụ: '½'.isnumeric() -> True).
num_str, sup_str, frac_str = '123', '²', '½'
print(num_str.isdecimal(), sup_str.isdecimal())  # True False
print(sup_str.isdigit(), frac_str.isnumeric())    # True True


# Dịch ký tự 1-1 với str.maketrans() & .translate():
trans_table = str.maketrans('abc', '123')
print('cab'.translate(trans_table)) # '312' (thay thế c->3, a->1, b->2)

# Căn lề chuỗi (Text alignment): center(), ljust(), rjust()
title = 'Python'

print(title.center(10))        # '  Python  ' (căn giữa trong độ rộng 10)
print(title.center(10, '-'))   # '--Python--' (căn giữa, bù ký tự '-')
print(title.ljust(10, '.'))    # 'Python....' (căn trái)
print(title.rjust(10, '.'))    # '....Python' (căn phải)