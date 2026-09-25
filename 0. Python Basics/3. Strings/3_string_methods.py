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

# Thay thế / Xóa ký tự hàng loạt với str.maketrans & str.translate (Chuẩn thực tế: làm sạch dữ liệu):
# Tham số 1 & 2: ánh xạ từng ký tự; Tham số 3: các ký tự muốn xóa sạch
clean_table = str.maketrans("", "", "!?,.")
raw_input = "Hello, World! How's it going?"
print("Clean text:", raw_input.translate(clean_table))  # "Hello World How's it going"


# Tách (split) & Nối (join) chuỗi
words = s.split()                  # ['hello', 'world']
print(words)
print('-'.join(words))             # 'hello-world'

# Mẫu hình Pythonic: Biến đổi từng từ trong câu và giữ nguyên khoảng cách gốc (dùng split(' ') + generator expression):
sentence_demo = "the of and python"
capitalized_words = " ".join(w.capitalize() if len(w) > 2 else w for w in sentence_demo.split(" "))
print("Pythonic word transformation:", capitalized_words) # 'the of and Python'

# Tách dòng: splitlines() vs split('\n') vs split()
poem = "Hello world\nPython code\n"
print(poem.splitlines())        # ['Hello world', 'Python code'] (Chuẩn nhất: tự bỏ dòng trống ở cuối)
print(poem.splitlines(True))    # ['Hello world\n', 'Python code\n'] (keepends=True: giữ ký tự \n)
print(poem.split('\n'))         # ['Hello world', 'Python code', ''] (Thừa '' ở cuối nếu có \n)
print(poem.split())             # ['Hello', 'world', 'Python', 'code'] (Tách theo từng từ)

# Hiệu năng nối chuỗi & nhân bản ký tự (Best Practices)
# 1. Nhân bản ký tự/chuỗi (String replication): 'c' * n (khi n <= 0 trả về chuỗi rỗng '')
print('x' * 3)   # 'xxx'
print('x' * 0)   # '' (hữu ích khi kết hợp với index trong loop/comprehension)

# 2. str.join() vs toán tử '+' (+=):
# - Chuỗi trong Python là IMMUTABLE: Nối bằng '+=' trong vòng lặp liên tục tạo object mới -> O(N^2).
# - Dùng str.join() gom dữ liệu trước và cấp phát bộ nhớ 1 lần duy nhất -> O(N).
# Ví dụ thực chiến (bài toán accum: 'abcd' -> 'A-Bb-Ccc-Dddd'):
s_sample = 'abcd'
# c.upper() + c.lower() * i (chỉ biến đổi hoa/thường 1 ký tự, tránh gọi .capitalize() trên cả chuỗi dài)
accum_fast = "-".join(c.upper() + c.lower() * i for i, c in enumerate(s_sample))
print(accum_fast)  # 'A-Bb-Ccc-Dddd'

# 3. Chuyển list số thành chuỗi nhanh nhất: "".join(map(str, arr))
# map(str, arr) chạy hoàn toàn ở tầng C, nhanh hơn cả List Comprehension [str(x) for x in arr]
digits_list = [0, 0, 0, 1]
print("".join(map(str, digits_list)))  # '0001'


# Tìm kiếm, Đếm & Kiểm tra tiền tố/hậu tố
print(s.find('world'))             # 6 (trả về -1 nếu không thấy)
print(s.count('o'))                # 2
print(s.startswith('hello'))       # True
print(s.endswith('world'))         # True
print(s.endswith('N'))             # False (câu hỏi trắc nghiệm)

# Đếm số lượng ký tự thuộc một tập hợp (ví dụ nguyên âm 'aeiou'):
vowel_count = sum(s.count(v) for v in 'aeiou')
print("Vowels count:", vowel_count)  # 3 ('e', 'o', 'o')


# Kiểm tra định dạng (isupper, islower)
print(s.isupper(), s.islower())    # False True

# Kiểm tra chuỗi số: isdecimal() là chuẩn tốt nhất (vừa nhanh hơn .isdigit(), vừa an toàn tuyệt đối trước khi int())
num_str = '123'
print(num_str.isdecimal())         # True