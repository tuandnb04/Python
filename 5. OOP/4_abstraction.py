from abc import ABC, abstractmethod

# Abstract Class cơ bản: Interface chung, không có thuộc tính khởi tạo
class Animal(ABC):  # Kế thừa từ Abstract Base Class (ABC)
    @abstractmethod # Decorator đánh dấu phương thức trừu tượng
    def make_sound(self) -> None: # Lớp con bắt buộc phải override phương thức này
        pass

# Lớp con cụ thể (Concrete class) override phương thức trừu tượng
class Dog(Animal):
    def make_sound(self) -> None:
        print('Woof!')

# Một lớp con cụ thể khác
class Cat(Animal):
    def make_sound(self) -> None:
        print('Meow!')

# Một lớp con cụ thể khác
class Monkey(Animal):
    def make_sound(self) -> None:
        print('Ooh ooh aah aah!')

# Tạo danh sách các đối tượng từ lớp con
animals: list[Animal] = [Dog(), Cat(), Monkey()]

# Duyệt qua từng đối tượng và gọi phương thức make_sound
for animal in animals:
    animal.make_sound()

# Kết quả:
# Woof!
# Meow!
# Ooh ooh aah aah!

# dog = Animal() 
# TypeError: Can't instantiate abstract class Animal 
# without an implementation for abstract method 'make_sound'

class Bird(Animal):
    pass

# bird = Bird()
# TypeError: Can't instantiate abstract class Bird 
# without an implementation for abstract method 'make_sound'


# Abstract Class có __init__ và chia sẻ thuộc tính chung
class TalkingToy(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def speak(self) -> None:
        pass

class RobotToy(TalkingToy):
    def speak(self) -> None:
        print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
    def speak(self) -> None:
        print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
    def speak(self) -> None:
        print(f'{self.name} says ROOOOAR!')

# Tạo các đồ chơi
rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys: list[TalkingToy] = [rusty, fluffy, rex]
for toy in toys:
    toy.speak()

# Kết quả:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!


