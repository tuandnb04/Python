# ENCAPSULATION & PROPERTIES (@property, setter, deleter)
# Đóng gói là việc gom nhóm thuộc tính và phương thức vào trong class, đồng thời
# che giấu trạng thái nội bộ bằng các thuộc tính private và kiểm soát truy cập qua public methods/properties.

# PHẦN 1: PRIVATE ATTRIBUTES VÀ BẢO VỆ DỮ LIỆU CƠ BẢN
class Wallet:
    def __init__(self, balance: float = 0.0) -> None:
        self.__balance = balance  # Thuộc tính private với hai dấu gạch dưới `__`

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


# PHẦN 2: GETTER, SETTER VÀ DELETER VỚI @property (PYTHONIC ENCAPSULATION)
# QUY TẮC VỀ GETTER & SETTER TRONG PYTHON (@property):
# 1. Cả Getter và Setter đều KHÔNG bắt buộc phải có.
#    - Chỉ có Getter (không Setter): Thuộc tính chỉ đọc (Read-only), như ví dụ `area` bên dưới.
# 2. THỨ TỰ BẮT BUỘC:
#    - Getter (@property) PHẢI đứng ĐẦU TIÊN để tạo đối tượng property mang tên hàm (`radius`).
#    - Setter (@<name>.setter) và Deleter (@<name>.deleter) PHẢI đứng SAU Getter.
#    - Nếu đặt Setter/Deleter lên trước Getter sẽ bị lỗi: `NameError: name '<name>' is not defined`.

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius  # Gọi setter để kiểm tra giá trị

    # 1. Getter: Đọc bán kính (Bắt buộc đứng đầu)
    @property
    def radius(self) -> float:
        return self._radius

    # 2. Setter: Gán bán kính có kiểm tra hợp lệ
    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value

    # 3. Deleter: Xóa bán kính
    @radius.deleter
    def radius(self) -> None:
        print("Deleting radius...")
        del self._radius

    # Getter: Tính diện tích (Chỉ đọc - Read-only, không có setter)
    @property
    def area(self) -> float:
        return 3.14 * (self._radius ** 2)


my_circle = Circle(5)
print("Initial radius:", my_circle.radius)  # Initial radius: 5
print("Initial area:", my_circle.area)      # Initial area: 78.5

my_circle.radius = 8
print("After modifying radius:", my_circle.radius)  # After modifying radius: 8
print("After modifying area:", my_circle.area)      # 200.96

del my_circle.radius  # Deleting radius...
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e)
