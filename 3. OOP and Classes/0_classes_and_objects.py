# 1. Khái niệm Class (Khuôn mẫu) & Object (Thực thể / Instance)
# Class là khuôn mẫu (template). Object là một thực thể được tạo ra từ class đó:
class MyClass:
    x = 5
    y = 10

obj1 = MyClass()
obj2 = MyClass()

print("obj1.x:", obj1.x)
print("obj2.y:", obj2.y)

# 2. Phương thức khởi tạo __init__() và từ khóa self
# - self đại diện cho chính đối tượng hiện tại đang thực thi.
# - Mọi phương thức của đối tượng đều phải có self làm tham số đầu tiên.
# - Khi gọi phương thức (dog.bark()), Python tự động truyền đối tượng vào self (không truyền thủ công):
class Dog:
    def __init__(self, name: str):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Fido")
dog.bark()

# Phương thức đối tượng (Object Method) có thể tính toán và trả về kết quả:
class Calc:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def multiply(self) -> int:
        return self.a * self.b

x = Calc(5, 10)
print("x.multiply():", x.multiply())

# 3. Class hoàn chỉnh: Thuộc tính (Properties), Phương thức và từ khóa self
# Thuộc tính lưu trữ dữ liệu (chuỗi, số, list...). Khởi tạo trong __init__ bằng self.name = value:
class Person:
    # Biến cấp lớp (Class Variable): dùng chung cho tất cả các đối tượng tạo từ Person
    species = "Homo sapiens"

    # Phương thức khởi tạo __init__: tự động gọi khi tạo đối tượng mới
    # 'self' đại diện cho chính đối tượng cụ thể đang được tạo hoặc thao tác
    def __init__(self, name: str, age: int):
        # Biến cá thể (Instance Variable): riêng biệt cho từng đối tượng
        self.name = name
        self.age = age

    # Instance Method: nhận self, thao tác trên dữ liệu của đối tượng
    def greet(self):
        print("Hello", self.name)

    # Phương thức đặc biệt __str__: Điều khiển nội dung xuất ra khi gọi print() (phải trả về chuỗi)
    def __str__(self):
        return f"{self.name} ({self.age})"

    def is_adult(self) -> bool:
        return self.age >= 18

    # Class Method: nhận cls, thường dùng làm hàm khởi tạo thay thế (Alternative Constructor)
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        return cls(name, 2026 - birth_year)

    # Static Method: hàm tiện ích độc lập gắn trong class, không nhận self hay cls
    @staticmethod
    def is_valid_name(name: str) -> bool:
        return len(name.strip()) >= 2 and not any(c.isdigit() for c in name)


# Khởi tạo và sử dụng các đối tượng Person:
p1 = Person("Emil", 25)
p2 = Person("Tobias", 22)
p3 = Person("Linus", 18)

print(p1.name)
print(p2.name)
print(p3.name)
p1.greet()
print("print(p1):", p1)

# Thay đổi thuộc tính từ bên ngoài (chỉ ảnh hưởng p1, các đối tượng khác giữ nguyên):
p1.name = "Emil Peterson"
print("Updated p1.name:", p1.name)
print("Unchanged p2.name:", p2.name)

# Gán thêm thuộc tính mới sau khi tạo (chỉ thuộc về riêng đối tượng p1):
p1.city = "Stockholm"
print("p1.city (dynamically added):", p1.city)

# Xóa thuộc tính bằng từ khóa del (gây lỗi AttributeError nếu cố tình truy cập sau đó):
del p1.city
try:
    print(p1.city)
except AttributeError:
    print("p1.city was removed with 'del' (AttributeError raised)")

# Thay đổi thuộc tính từ bên trong method bằng self.name = value:
class Toggle:
    def __init__(self, x: bool):
        self.val = x

    def change(self):
        self.val = not self.val

sw = Toggle(True)
print("Toggle initial:", sw.val)
sw.change()
print("Toggle after change():", sw.val)

# 4. Sử dụng các phương thức nâng cao (Instance, Class, Static method):
print(f"Is {p1.name} an adult? ->", p1.is_adult())

# Tạo đối tượng qua class method:
p4 = Person.from_birth_year("Charlie", 2000)
print(f"Created via classmethod: {p4.name}, age {p4.age}")

# Gọi static method:
print("Is 'Linus' valid name?", Person.is_valid_name("Linus"))
