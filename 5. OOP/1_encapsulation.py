class Wallet:
    def __init__(self):
        self.__balance = 0  # Thuộc tính private

    @staticmethod
    def __validate(amount: float) -> None:
        if amount <= 0:
            raise ValueError('Amount must be positive')

    def deposit(self, amount: float) -> None:
        self.__validate(amount)
        self.__balance += amount  # Nạp tiền an toàn

    def withdraw(self, amount: float) -> None:
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        self.__balance -= amount  # Rút tiền an toàn

    def get_balance(self) -> float:
        return self.__balance


acct_one = Wallet()
acct_one.deposit(3)
print("Wallet balance:", acct_one.get_balance())  # 3

acct_one.deposit(50)
print("Wallet balance:", acct_one.get_balance())  # 53

# acct_one.deposit(-4)  # ValueError: Amount must be positive
# acct_one.withdraw(-8) # ValueError: Amount must be positive
# acct_one.withdraw(58) # ValueError: Insufficient funds


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius  # Gọi setter để kiểm tra giá trị

    # Getter: Đọc bán kính
    @property
    def radius(self) -> float:
        return self._radius

    # Setter: Gán bán kính có kiểm tra
    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    # Deleter: Xóa bán kính
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

    # Getter: Tính diện tích
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)


# Khởi tạo đối tượng
my_circle = Circle(5)

# Đọc thuộc tính (Getter)
print("Initial radius:", my_circle.radius)  # Initial radius: 5
print("Initial area:", my_circle.area)      # Initial area: 78.5

# Gán giá trị mới (Setter)
my_circle.radius = 8
print("After modifying radius:", my_circle.radius)  # After modifying radius: 8
print("After modifying area:", my_circle.area)      # 200.96

# Xóa thuộc tính (Deleter)
del my_circle.radius  # Deleting radius...

# Kiểm tra lỗi sau khi xóa
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e)  # Error: 'Circle' object has no attribute '_radius'
