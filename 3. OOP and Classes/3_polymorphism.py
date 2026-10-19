# 1. DUCK TYPING POLYMORPHISM (Các class độc lập cùng chia sẻ tên phương thức)
class Twitter:
    def __init__(self, content: str) -> None:
        self.content = content

    def post(self) -> str:
        return f"Tweet: '{self.content}' (280 chars max)"


class Instagram:
    def __init__(self, content: str) -> None:
        self.content = content

    def post(self) -> str:
        return f"Instagram Post: '{self.content}' + filters"


class LinkedIn:
    def __init__(self, content: str) -> None:
        self.content = content

    def post(self) -> str:
        return f"LinkedIn Article: '{self.content}' (Professional Mode)"


def start(social_media) -> None:
    print(social_media.post())  # Gọi .post() trên bất kỳ đối tượng nào


tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes')
article = LinkedIn('Why OOP matters in 2024')

start(tweet)
start(photo)
start(article)


# 2. INHERITANCE-BASED POLYMORPHISM (Kế thừa từ lớp cha và ghi đè phương thức)
class Animal:
    def speak(self) -> str:
        return 'Some generic sound'


class Cat(Animal):
    def speak(self) -> str:
        return 'A cat meow'


class Dog(Animal):
    def speak(self) -> str:
        return 'A dog barks woof woof'


class Monkey(Animal):
    def speak(self) -> str:
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'


animals: list[Animal] = [Cat(), Dog(), Monkey()]

for animal in animals:
    print(animal.speak())
