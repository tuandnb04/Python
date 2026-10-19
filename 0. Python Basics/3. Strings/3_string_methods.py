text = '  hello world  '

# Biến đổi chữ hoa / thường
s = 'hello world'
print(s.upper())  # 'HELLO WORLD'
print(s.lower())  # 'hello world'
print(s.capitalize())  # 'Hello world'
print(s.title())  # 'Hello World'

# Phân biệt capitalize() vs title() với từ có dấu nháy đơn hoặc ký tự đặc biệt:
# - title(): Viết hoa sau mọi ký tự không phải chữ cái (kể cả dấu nháy đơn: "they're" -> "They'Re").
# - capitalize(): Chỉ viết hoa ký tự đầu tiên của chuỗi ("they're" -> "They're").
contraction = "they're"
print(contraction.title())  # "They'Re"
print(contraction.capitalize())  # "They're"

# Chuỗi phương thức liên tiếp (Method Chaining): Vừa cắt khoảng trắng vừa viết hoa
messy_name = '  sARaH dAVis  '
clean_name = messy_name.strip().title()
print(f"Original name: '{messy_name}'")
print(f"Cleaned name: '{clean_name}'")  # 'Sarah Davis'

# Cắt khoảng trắng & Thay thế
print(text.strip())  # 'hello world'
print(s.replace('hello', 'hi'))  # 'hi world'
print(s.replace(' ', '', 1))  # 'helloworld' (tham số count: chỉ thay thế 1 lần đầu tiên)

# Xóa khoảng trắng: .replace(" ", "") vs "".join(s.split())
# - s.replace(" ", ""): Chỉ xóa dấu cách đơn ' ' (bỏ sót \t, \n, \r)
# - "".join(s.split()): Xóa mọi loại whitespace (space, tab, newline)
mixed_space = "Hello \t world \n !"
print("replace(' ', ''):", mixed_space.replace(" ", ""))  # 'Hello\tworld\n!' (còn sót \t, \n)
print("join(split()):   ", "".join(mixed_space.split()))  # 'Helloworld!' (sạch hoàn toàn whitespace)

# Thay thế / Xóa ký tự hàng loạt với str.maketrans & str.translate:
# Tham số 1 & 2: ánh xạ từng ký tự; Tham số 3: các ký tự muốn xóa sạch
clean_table = str.maketrans("", "", "!?,.")
raw_input = "Hello, World! How's it going?"
print("Clean text:", raw_input.translate(clean_table))  # "Hello World How's it going"

# Nối chuỗi với str.join() và Tách chuỗi:
words = s.split()  # Mặc định: tách theo khoảng trắng
print(words)
print("Joined with hyphen:", "-".join(words))  # 'hello-world'
print("Joined with comma: ", ", ".join(words))  # 'hello, world'

# Tách chuỗi với dấu phân cách tùy biến (.split(sep)):
full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print("Address parts:", address_parts)  # ['123 Main Street', 'Springfield', 'IL']
print("Rejoined:     ", ' | '.join(address_parts))  # '123 Main Street | Springfield | IL'

# Tách dòng: splitlines() vs split('\n') vs split()
poem = "Hello world\nPython code\n"
print(poem.splitlines())  # ['Hello world', 'Python code'] (tự bỏ dòng trống ở cuối)
print(poem.splitlines(True))  # ['Hello world\n', 'Python code\n'] (keepends=True: giữ ký tự \n)
print(poem.split('\n'))  # ['Hello world', 'Python code', ''] (Thừa '' ở cuối nếu có \n)
print(poem.split())  # ['Hello', 'world', 'Python', 'code'] (Tách theo từng từ)

# Nhân bản ký tự / chuỗi: 'c' * n (khi n <= 0 trả về chuỗi rỗng '')
print('x' * 3)  # 'xxx'
print('x' * 0)  # ''

# Tìm kiếm, Đếm & Kiểm tra tiền tố/hậu tố
print(s.find('world'))  # 6 (trả về -1 nếu không thấy)

# Cắt chuỗi theo chỉ số động từ .find(): string[:var_index]
email = 'alice.johnson@company.com'
print(f'Email: {email}')

at_position = email.find('@')
print(f'Position of @: {at_position}')

username = email[:at_position]
print(f'Username: {username}')

# Tạo tên hiển thị từ username (kết hợp .replace và .title):
display_name = username.replace('.', ' ').title()
print(f'Display name: {display_name}')  # 'Alice Johnson'

# Kiểm tra tiền tố, hậu tố & Đếm số lần xuất hiện (.count):
print(s.startswith('hello'))  # True
print(s.endswith('world'))  # True
print(s.endswith('N'))  # False (câu hỏi trắc nghiệm)

print("Count 'l':", s.count('l'))  # 2
print("Count 'o':", s.count('o'))  # 2

# Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())  # False True

# Kiểm tra loại ký tự (Character Classification: isalpha, isdigit, isalnum, isspace, isdecimal):
num_str = '123'
print(num_str.isdecimal())  # True
print("'abc'.isalpha():", 'abc'.isalpha())  # True (chỉ chứa chữ cái)
print("'123'.isdigit():", '123'.isdigit())  # True (chỉ chứa chữ số)
print("'user_1'.isalnum():", 'user_1'.isalnum())  # False (do có ký tự gạch dưới '_')
print("'user1'.isalnum():", 'user1'.isalnum())  # True (chỉ gồm chữ và số)
print("'   '.isspace():", '   '.isspace())  # True (toàn bộ là whitespace)

# Phân biệt find() vs index():
# - .find(): Trả về -1 nếu không tìm thấy (an toàn khi tìm kiếm)
# - .index(): Ném ngoại lệ ValueError nếu không tìm thấy
sample = "Python"
print("find('th'):", sample.find('th'))  # 2
print("find('z'):", sample.find('z'))    # -1
# sample.index('z')                      # ValueError: substring not found

# Tách chuỗi 3 phần với partition(sep): trả về tuple (trước, sep, sau)
user_email = "admin@example.com"
username_part, sep_part, domain_part = user_email.partition("@")
print("partition('@'):", username_part, "|", domain_part)  # admin | example.com

# Chèn số 0 ở đầu với zfill(width):
order_id = "42"
print("zfill(5):", order_id.zfill(5))  # '00042'

