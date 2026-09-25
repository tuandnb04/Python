# INHERITANCE, MULTIPLE INHERITANCE, MRO & COMPOSITION

# PHẦN 1: ĐƠN KẾ THỪA (SINGLE INHERITANCE) VÀ super()

class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def sound(self) -> str:
        return f'{self.name} makes a sound'


# 1. Kế thừa và tái sử dụng trực tiếp thuộc tính & phương thức lớp cha
class SimpleDog(Animal):
    bark = 'woof! woof!! woof!!!'

jack = SimpleDog('Jack')
print(jack.sound())  # Jack makes a sound
print(jack.bark)     # woof! woof!! woof!!!


# 2. Ghi đè phương thức (Method Overriding)
class OverridingDog(Animal):
    bark = 'woof! woof!! woof!!!'

    def sound(self) -> str:
        return f'{self.name} barks {self.bark}'

max_dog = OverridingDog('Max')
print(max_dog.sound())  # Max barks woof! woof!! woof!!!


# 3. Mở rộng logic phương thức lớp cha bằng hàm super()
class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    def sound(self) -> str:
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'

buddy = Dog('Buddy')
print(buddy.sound())  # Buddy makes a sound, then Buddy barks woof! woof!! woof!!!


# PHẦN 2: ĐA KẾ THỪA (MULTIPLE INHERITANCE) VÀ DIAMOND PROBLEM

class Walker:
    def walk(self) -> str:
        return 'I can walk on land'


class Swimmer:
    def swim(self) -> str:
        return 'I can swim in water'


# Amphibian kế thừa từ cả Walker và Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."


frog = Amphibian('Freddy')
print(frog.introduce())


# BÀI TOÁN KIM CƯƠNG (DIAMOND PROBLEM) VÀ MRO (Method Resolution Order):
# Sơ đồ:
#        A
#       / \
#      B   C
#       \ /
#        D

class A:
    def greet(self) -> str:
        return "Greeting from A"

class B(A):
    def greet(self) -> str:
        return "Greeting from B"

class C(A):
    def greet(self) -> str:
        return "Greeting from C"

class D(B, C):
    pass

d = D()
print("d.greet() output:", d.greet())  # Kết quả: "Greeting from B" (vì B đứng trước C)

# Xem thứ tự tìm kiếm phương thức qua MRO:
print("MRO for class D:", [cls.__name__ for cls in D.mro()])
# Thứ tự: D -> B -> C -> A -> object


# PHẦN 3: NGUYÊN LÝ THIẾT KẾ: COMPOSITION OVER INHERITANCE
# "Favor composition over inheritance" (Ưu tiên bao hàm hơn là kế thừa)
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
        self.gps = GPS()                  # Composition

    def drive(self) -> None:
        print(f"Starting {self.brand}:")
        print(" -", self.engine.start())
        print(" -", self.gps.locate())


car = Car("Tesla Model S", 670)
car.drive()
