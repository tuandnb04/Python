# Khai báo chuỗi (Đơn, đôi, multiline, escape)
msg = "It's a sunny day"
multiline = """Line 1
Line 2"""
escaped = 'She said: "Hello!"'

# Kiểm tra (in), độ dài (len) & Indexing
s = 'Hello world'
print('Hello' in s, 'xyz' in s) # True False
print(len(s))                   # 11
print(s[0], s[-1])              # 'H' 'd'

# Tính bất biến (Immutability)
# Chuỗi có thể gán lại (reassignment) nhưng không thể sửa từng ký tự
greeting = 'hi'
greeting = 'hello'              # Hợp lệ
# greeting[0] = 'H'             # TypeError: 'str' object does not support item assignment
print(greeting)                 # 'hello'