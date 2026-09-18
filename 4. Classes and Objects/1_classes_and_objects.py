# Class = Blueprint (Bản thiết kế) | Object = Instance (Đối tượng tạo từ bản thiết kế)
# Quy ước đặt tên Class: PascalCase (ClassName, DogBreed, ...)

# 1. Cú pháp cơ bản của Class
class ClassName:
    def __init__(self, name, age):
        self.name = name          # Attribute (Thuộc tính lưu dữ liệu)
        self.age = age

    def sample_method(self):      # Method (Phương thức hành vi)
        print(self.name.upper())


# 2. Ví dụ thực tế với Class Dog
class Dog:
    # __init__: Phương thức đặc biệt tự động gọi khi tạo object
    # 'self': Tham chiếu đến chính object đang được tạo
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")


# 3. Tạo các đối tượng từ Class (object = ClassName(args...))
dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

# 4. Gọi phương thức
dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!
