# 1. Class Attribute vs Instance Attribute (Class Dog)
class Dog:
    species = "French Bulldog"  # Class attribute (dùng chung cho cả lớp)

    def __init__(self, name):
        self.name = name        # Instance attribute (riêng cho từng đối tượng)

    def bark(self):
        return f"{self.name} says woof woof!"


# Truy cập Class attribute trực tiếp từ Class
print(Dog.species)  # French Bulldog

# Truy cập Instance attribute qua Object
dog1 = Dog("Jack")
print(dog1.name)     # Jack
print(dog1.species)  # French Bulldog

dog2 = Dog("Tom")
print(dog2.name)     # Tom
print(dog2.species)  # French Bulldog

# Gọi Method
jack = Dog("Jack")
jill = Dog("Jill")
print(jack.bark())  # Jack says woof woof!
print(jill.bark())  # Jill says woof woof!


# 2. Instance Attributes & Method describe (Class Car)
class Car:
    def __init__(self, color, model):
        self.color = color  # Instance attribute
        self.model = model  # Instance attribute

    def describe(self):
        return f"This car is a {self.color} {self.model}"


car_1 = Car("red", "Toyota Corolla")
car_2 = Car("green", "Lamborghini Revuelto")

print(car_1.model)  # Toyota Corolla
print(car_2.model)  # Lamborghini Revuelto
print(car_1.color)  # red
print(car_2.color)  # green

print(car_1.describe())  # This car is a red Toyota Corolla
print(car_2.describe())  # This car is a green Lamborghini Revuelto
