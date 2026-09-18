class Animal:
    # Thuộc tính và phương thức của lớp cha
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'


class Dog(Animal):
    # Lớp con kế thừa, mở rộng và/hoặc ghi đè khi cần thiết
    bark = 'woof! woof!! woof!!!'

    # Ghi đè phương thức sound() để dùng biến lớp bark
    # Gọi Animal.sound(), sau đó nối thêm tiếng sủa bark
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'


jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!

class Walker:
    # Thuộc tính và phương thức cho lớp cha
    def walk(self):
        return 'I can walk on land'


class Swimmer:
    # Thuộc tính và phương thức cho lớp con
    def swim(self):
        return 'I can swim in water'


# Amphibian kế thừa từ cả Walker và Swimmer
class Amphibian(Walker, Swimmer):
    # Lớp cháu kế thừa từ cả lớp cha và lớp con
    # Lớp cháu có thể kết hợp hoặc ghi đè hành vi từ mỗi lớp
    def __init__(self, name: str):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."


frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.
