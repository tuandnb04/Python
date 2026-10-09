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

# Chuỗi phương thức liên tiếp (Method Chaining): Vừa cắt khoảng trắng vừa viết hoa
messy_name = '  sARaH dAVis  '
clean_name = messy_name.strip().title()
print(f"Original name: '{messy_name}'")
print(f"Cleaned name: '{clean_name}'")  # 'Sarah Davis'


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


# Nối chuỗi với str.join() và Tách chuỗi:
words = s.split()                  # Mặc định: tách theo khoảng trắng
print(words)
print("Joined with hyphen:", "-".join(words))  # 'hello-world'
print("Joined with comma: ", ", ".join(words))  # 'hello, world'

# Tách chuỗi với dấu phân cách tùy biến (.split(sep)):
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print("Address parts:", address_parts)         # ['123 Main Street', 'Springfield', 'IL']
print("Rejoined:     ", ' | '.join(address_parts)) # '123 Main Street | Springfield | IL'

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

# Chuẩn hóa tên hiển thị từ username (kết hợp .replace và .title):
display_name = username.replace('.', ' ').title()
print(f'Display name: {display_name}')  # 'Alice Johnson'

# Kiểm tra tiền tố, hậu tố & Đếm số lần xuất hiện (.count):
print(s.startswith('hello'))       # True
print(s.endswith('world'))         # True
print(s.endswith('N'))             # False (câu hỏi trắc nghiệm)

print("Count 'l':", s.count('l'))  # 2
print("Count 'o':", s.count('o'))  # 2



# Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())    # False True

# Kiểm tra chuỗi số: isdecimal() là chuẩn tốt nhất (vừa nhanh hơn .isdigit(), vừa an toàn tuyệt đối trước khi int())
num_str = '123'
print(num_str.isdecimal())         # True