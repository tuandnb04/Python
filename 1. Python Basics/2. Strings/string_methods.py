text = '  hello world  '

# 1. Biến đổi chữ hoa / thường
s = 'hello world'
print(s.upper())       # 'HELLO WORLD'
print(s.lower())       # 'hello world'
print(s.capitalize())  # 'Hello world'
print(s.title())       # 'Hello World'

# 2. Cắt khoảng trắng & Thay thế
print(text.strip())                # 'hello world'
print(s.replace('hello', 'hi'))    # 'hi world'
# str.maketrans('abc', '123')      # Tạo bảng dịch 1-1 ký tự (dùng với s.translate())

# 3. Tách (split) & Nối (join)
words = s.split()                  # ['hello', 'world']
print(words)
print('-'.join(words))             # 'hello-world'

# 4. Tách dòng: splitlines() vs split('\n') vs split()
poem = "Hello world\nPython code\n"
print(poem.splitlines())        # ['Hello world', 'Python code'] (Chuẩn nhất: tự bỏ dòng trống ở cuối)
print(poem.splitlines(True))    # ['Hello world\n', 'Python code\n'] (keepends=True: giữ ký tự \n)
print(poem.split('\n'))         # ['Hello world', 'Python code', ''] (Thừa '' ở cuối nếu có \n)
print(poem.split())             # ['Hello', 'world', 'Python', 'code'] (Tách theo từng từ)

# 5. Tìm kiếm, Đếm & Kiểm tra tiền tố/hậu tố
print(s.find('world'))             # 6 (trả về -1 nếu không thấy)
print(s.count('o'))                # 2
print(s.startswith('hello'))       # True
print(s.endswith('world'))         # True
print(s.endswith('N'))             # False (câu hỏi trắc nghiệm)

# 6. Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())    # False True

# 7. Dịch ký tự 1-1 với str.maketrans() & .translate() (Ứng dụng giải mã Caesar / ROT13)
trans_table = str.maketrans('abc', '123')
print('cab'.translate(trans_table)) # '312' (thay thế c->3, a->1, b->2)