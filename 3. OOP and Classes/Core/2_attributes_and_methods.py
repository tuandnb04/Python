# CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES & METHOD TYPES
# 1. Instance Method (self): Thao tác trên thuộc tính của từng đối tượng cụ thể.
# 2. Class Method (@classmethod, cls): Thao tác trên cấp độ Class, thường dùng làm Alternative Constructors.
# 3. Static Method (@staticmethod): Hàm tiện ích độc lập được gom chung vào namespace của class.
# 4. Class Variable vs Instance Variable: Biến chia sẻ chung cho mọi instance vs Biến riêng của từng instance.

from datetime import date


class User:
    # CLASS VARIABLE: Chia sẻ chung cho TOÀN BỘ các instances tạo từ User
    total_users: int = 0
    minimum_age: int = 18

    def __init__(self, name: str, age: int) -> None:
        # INSTANCE VARIABLES: Riêng biệt cho từng cá thể đối tượng
        self.name: str = name
        self.age: int = age
        User.total_users += 1

    # 1. Instance Method: Nhận `self`
    def introduce(self) -> str:
        return f"Hello, I am {self.name}, {self.age} years old."

    def is_adult(self) -> bool:
        return self.age >= User.minimum_age

    # 2. Class Method: Nhận `cls`, dùng làm Alternative Constructor
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> "User":
        current_year = date.today().year
        calculated_age = current_year - birth_year
        return cls(name, calculated_age)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(name=data["name"], age=data["age"])

    # 3. Static Method: Tiện ích độc lập, không nhận self hay cls
    @staticmethod
    def is_valid_name(name: str) -> bool:
        return len(name.strip()) >= 2 and not any(char.isdigit() for char in name)


u1 = User("Alice", 20)
u2 = User("Bob", 16)
print(u1.introduce())
print(f"Is Alice an adult ({User.minimum_age}+)? ->", u1.is_adult())
print("Total registered users:", User.total_users)  # 2

# Tạo đối tượng qua alternative constructor:
u3 = User.from_birth_year("Charlie", 2000)
print(u3.introduce())
print("Total registered users now:", User.total_users)  # 3

# Kiểm tra static method:
print("Is 'John123' valid?", User.is_valid_name("John123"))  # False
print("Is 'Emily' valid?", User.is_valid_name("Emily"))      # True
