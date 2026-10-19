# 1. Định nghĩa và gọi hàm cơ bản (def):
# Hàm là khối mã có thể tái sử dụng nhiều lần. Khối lệnh bên trong phải thụt lề:
def myfunc():
    print("Hello!")

myfunc()  # Gọi hàm thực thi bằng tên kèm cặp ngoặc tròn ()

# Câu lệnh 'pass': giữ chỗ không làm gì, tránh lỗi SyntaxError khi hàm chưa viết mã:
def empty_func():
    pass

empty_func()

# 2. Tham số (Parameter) vs Đối số (Argument):
# - Parameter: biến được đặt trong định nghĩa hàm (name, age)
# - Argument: giá trị thực tế truyền vào khi gọi hàm ("Linus", 19)
def introduce(name, age):
    print(f"My name is {name} and I'm {age}")

introduce("Linus", 19)

# 3. Giá trị trả về (return) và kết thúc hàm:
# 'return' gửi kết quả về nơi gọi và DỪNG HÀM NGAY LẬP TỨC (mã phía sau sẽ không chạy):
def add(a, b):
    return a + b
    # Dòng dưới đây sẽ không bao giờ được thực thi:
    print("This will never run")

print("Result of add(3, 5):", add(3, 5))

# 4. Tham số có giá trị mặc định (Default Parameter):
# Gán giá trị mặc định bằng dấu '=' khi người dùng không truyền đối số:
def greet_default(name="World"):
    print("Hello", name)

greet_default()         # Không truyền đối số: tự động dùng mặc định 'World'
greet_default("Alice")  # Có truyền đối số: ghi đè giá trị 'Alice'

# Lưu ý quan trọng: Tham số có mặc định PHẢI đứng sau tham số không có mặc định:
def create_user(name, role="Member"):
    return f"User: {name} | Role: {role}"

print(create_user("Bob"))  # Dùng role mặc định 'Member'

# 5. Đối số từ khóa (Keyword Arguments):
# Truyền giá trị theo tên tham số thay vì thứ tự; thứ tự truyền lúc này không quan trọng:
def display_profile(name, age):
    print(f"Name: {name}, Age: {age}")

display_profile(age=18, name="Linus")  # Đổi thứ tự vẫn gán chính xác

# Lưu ý: Khi kết hợp, đối số vị trí (positional) PHẢI đứng trước đối số từ khóa (keyword):
display_profile("Linus", age=18)       # Hợp lệ

# 6. Nhận số lượng đối số linh hoạt (*args và **kwargs):
# Dấu '*' gom toàn bộ đối số vị trí truyền vào thành một Tuple:
def show_kids(*kids):
    print(f"Total kids: {len(kids)}, youngest is: {kids[-1]}")

show_kids("Emil", "Tobias", "Linus")

# Dấu '**' gom toàn bộ đối số từ khóa truyền vào thành một Dictionary:
def show_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is {value}")

show_user_info(name="Linus", age=18)

# 7. Phạm vi biến: Cục bộ (Local) vs Toàn cục (Global):
x = "Hi"  # Biến toàn cục (Global)

def demo_scope():
    y = "Bye"  # Biến cục bộ (Local, chỉ tồn tại trong hàm này)
    print("Global inside:", x)
    print("Local inside:", y)

demo_scope()

# Khi trùng tên, Python luôn ưu tiên tìm biến cục bộ (Local) trước:
def local_priority():
    x = "Bye"  # Biến local riêng, không ảnh hưởng global x bên ngoài
    print("Local priority x:", x)

local_priority()

# Dùng từ khóa 'global' khi muốn sửa giá trị của biến toàn cục từ bên trong hàm:
def update_global():
    global x
    x = "Modified"

update_global()
print("Global x after update:", x)
