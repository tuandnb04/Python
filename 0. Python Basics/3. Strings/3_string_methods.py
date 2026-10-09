text = '  hello world  '

# Biến đổi chữ hoa / thường
s = 'hello world'
print(s.upper())       # 'HELLO WORLD' - chuyển toàn bộ sang chữ hoa
print(s.lower())       # 'hello world' - chuyển toàn bộ sang chữ thường
print(s.capitalize())  # 'Hello world' - viết hoa chữ cái đầu tiên
print(s.title())       # 'Hello World' - viết hoa chữ cái đầu của mỗi từ

# Phân biệt capitalize() vs title() với từ có dấu nháy đơn hoặc ký tự đặc biệt:
# - title(): Viết hoa sau mọi ký tự không phải chữ cái (kể cả dấu nháy đơn: "they're" -> "They'Re").
# - capitalize(): Chỉ viết hoa ký tự đầu tiên của chuỗi ("they're" -> "They're").
contraction = "they're"
print(contraction.title())       # "They'Re"  (lỗi chính tả do viết hoa sau dấu nháy)
print(contraction.capitalize())  # "They're"  (chuẩn ngữ pháp)

# Ứng dụng .title(): Chuyển đổi snake_case / kebab-case sang camelCase nhanh nhất (C-level):
# .title() tự viết hoa chữ cái sau '-' và '_', sau đó chỉ cần .replace() xóa dấu phân cách
camel_sample = "the-stealth_warrior"
res_camel = camel_sample[:1] + camel_sample.title().replace("-", "").replace("_", "")[1:]
print("CamelCase:", res_camel)  # 'theStealthWarrior'


# Cắt khoảng trắng & Thay thế
print(text.strip())                # 'hello world'
print(s.replace('hello', 'hi'))    # 'hi world'
print(s.replace(' ', '', 1))       # 'helloworld' (tham số count: chỉ thay thế 1 lần đầu tiên)

# Xóa khoảng trắng: .replace(" ", "") vs "".join(s.split())
# - s.replace(" ", ""): Cực nhanh (C-level), nhưng CHỈ xóa dấu cách đơn ' ' (bỏ sót \t, \n, \r)
# - "".join(s.split()): Chuẩn Pythonic xóa MỌI loại whitespace (space, tab, newline)
mixed_space = "Hello \t world \n !"
print("replace(' ', ''):", mixed_space.replace(" ", ""))     # 'Hello\tworld\n!' (còn sót \t, \n)
print("join(split()):   ", "".join(mixed_space.split()))     # 'Helloworld!' (sạch hoàn toàn whitespace)


# Thay thế / Xóa ký tự hàng loạt với str.maketrans & str.translate (Chuẩn thực tế: làm sạch dữ liệu):
# Tham số 1 & 2: ánh xạ từng ký tự; Tham số 3: các ký tự muốn xóa sạch
clean_table = str.maketrans("", "", "!?,.")
raw_input = "Hello, World! How's it going?"
print("Clean text:", raw_input.translate(clean_table))  # "Hello World How's it going"


# Nối chuỗi với str.join():
words = s.split()
print(words)
print("Joined with hyphen:", "-".join(words))  # 'hello-world'
print("Joined with comma: ", ", ".join(words))  # 'hello, world'

# Tách dòng: splitlines() vs split('\n') vs split()
poem = "Hello world\nPython code\n"
print(poem.splitlines())        # ['Hello world', 'Python code'] (Chuẩn nhất: tự bỏ dòng trống ở cuối)
print(poem.splitlines(True))    # ['Hello world\n', 'Python code\n'] (keepends=True: giữ ký tự \n)
print(poem.split('\n'))         # ['Hello world', 'Python code', ''] (Thừa '' ở cuối nếu có \n)
print(poem.split())             # ['Hello', 'world', 'Python', 'code'] (Tách theo từng từ)

# Nhân bản ký tự / chuỗi: 'c' * n (khi n <= 0 trả về chuỗi rỗng '')
print('x' * 3)   # 'xxx'
print('x' * 0)   # ''



# Tìm kiếm, Đếm & Kiểm tra tiền tố/hậu tố
print(s.find('world'))             # 6 (trả về -1 nếu không thấy)

# Cắt chuỗi theo chỉ số động từ .find(): string[:var_index]
email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

print(s.count('o'))                # 2
print(s.startswith('hello'))       # True
print(s.endswith('world'))         # True
print(s.endswith('N'))             # False (câu hỏi trắc nghiệm)

# Đếm số lượng ký tự với .count():
print("Count 'l':", s.count('l'))  # 2
print("Count 'o':", s.count('o'))  # 2


# Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())    # False True

# Kiểm tra chuỗi số: isdecimal() là chuẩn tốt nhất (vừa nhanh hơn .isdigit(), vừa an toàn tuyệt đối trước khi int())
num_str = '123'
print(num_str.isdecimal())         # True