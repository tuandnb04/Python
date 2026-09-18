class Animal:
    def speak(self) -> str:
        return 'Some generic sound'


class Dog(Animal):
    def speak(self) -> str:
        return 'A dog barks woof woof'


class Cat(Animal):
    def speak(self) -> str:
        return 'A cat meows'


animals: list[Animal] = [Animal(), Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Kết quả:
# Some generic sound
# A dog barks woof woof
# A cat meows

class SocialMedia:
    def post(self) -> str:
        raise NotImplementedError


class Twitter(SocialMedia):
    def __init__(self, content: str):
        self.content = content

    def post(self) -> str:
        return f"Tweet: '{self.content}' (280 chars max)"


class Instagram(SocialMedia):
    def __init__(self, content: str):
        self.content = content

    def post(self) -> str:
        return f"Instagram Post: '{self.content}' + filters"


def start(social_media: SocialMedia):
    print(social_media.post())  # Gọi .post() trên bất kỳ đối tượng nào


# Lời gọi đa hình - cùng một hàm, các kết quả đầu ra khác nhau
start(Twitter('Just learned Python polymorphism!'))  # Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(Instagram('Sunset vibes'))  # Instagram Post: 'Sunset vibes' + filters
