# 1. Kế thừa cơ bản (Inheritance: Base Class -> Derived Class)
# Lớp con kế thừa toàn bộ phương thức từ lớp cha, đồng thời có thể bổ sung phương thức riêng:
class Vehicle:
    def greet(self):
        print("Hello from Parent")


class Bike(Vehicle):
    def topspeed(self):
        print("60 km/h")


a = Bike()
a.greet()      # Kế thừa từ lớp cha Vehicle
a.topspeed()   # Phương thức riêng của lớp con Bike (lớp cha không có)

# 2. Ghi đè phương thức (Method Overriding)
# Lớp con định nghĩa lại phương thức cùng tên để thay thế hành vi của lớp cha:
class ElectricBike(Vehicle):
    def greet(self):
        print("Hello from Child")


b = ElectricBike()
b.greet()

# 3. Kế thừa và mở rộng logic lớp cha bằng hàm super()
class LoudBike(Vehicle):
    def greet(self):
        super().greet()  # Gọi phương thức của lớp cha Vehicle
        print("Hello from Loud Bike")


c = LoudBike()
c.greet()


# 4. Đa kế thừa (Multiple Inheritance) & Thứ tự phân giải phương thức (MRO)
# Lớp con có thể kế thừa từ nhiều lớp cha bằng cú pháp: class C(A, B):
class A:
    def hello(self):
        print("Dude!")

    def hi(self):
        print("Dude!")


class B:
    def welcome(self):
        print("What's up!")

    def hi(self):
        print("What's up!")


class C(A, B):
    pass


c = C()
c.hello()    # Kế thừa từ A: "Dude!"
c.welcome()  # Kế thừa từ B: "What's up!"
# Khi trùng tên, Python tìm kiếm theo thứ tự: Lớp con (C) -> Lớp cha từ trái sang phải (A rồi B):
c.hi()       # Gọi A.hi() vì A đứng trước B: "Dude!"

# Kiểm tra thứ tự tìm kiếm phương thức (Method Resolution Order):
print("MRO for class C:", [cls.__name__ for cls in C.mro()])
# Thứ tự: C -> A -> B -> object


# 5. Nguyên lý thiết kế: Composition over Inheritance (Bao hàm thay vì kế thừa)
# - Inheritance (Is-A): An ElectricCar IS A Vehicle.
# - Composition (Has-A): A Car HAS AN Engine and HAS A GPS.
#
# LƯU Ý QUAN TRỌNG VỀ QUAN HỆ KẾ THỪA (IS-A) TRONG OOP:
# Quan hệ Is-A trong OOP phải dựa trên "HÀNH VI" (Behavior), không chỉ dựa vào phân loại đời thực.
# Ví dụ kinh điển (Cạm bẫy Square - Rectangle):
# - Toán học: Hình vuông IS-A Hình chữ nhật.
# - Lập trình OOP: Nếu Square kế thừa Rectangle, khi người dùng gọi set_width(w) trên Rectangle
#   họ kỳ vọng height không đổi. Nhưng Square lại buộc phải đổi cả height -> phá vỡ kỳ vọng hành vi
#   (Vi phạm nguyên lý Liskov Substitution Principle - LSP).
# => Khi đó giải pháp tốt hơn là cả hai cùng kế thừa lớp cha trừu tượng Shape, hoặc dùng Composition.

class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine with {self.horsepower}HP started: Vroooom!"


class GPS:
    def locate(self) -> str:
        return "Coordinates: 37.7749 N, 122.4194 W (San Francisco)"


class Car:
    # Car không kế thừa Engine hay GPS, mà BAO HÀM chúng
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.engine = Engine(horsepower)  # Composition
        self.gps = GPS()  # Composition

    def drive(self) -> None:
        print(f"Starting {self.brand}:")
        print(" -", self.engine.start())
        print(" -", self.gps.locate())


car = Car("Tesla Model S", 670)
car.drive()
