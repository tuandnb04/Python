# 1. Thuộc tính riêng tư (Private Attributes) & Getter / Setter
# Đóng gói (Encapsulation) giúp che giấu trạng thái nội bộ. Dùng tiền tố 2 dấu gạch dưới __ để tạo private attribute:
class Person:
    def __init__(self, name: str, user_id: int = 89556) -> None:
        self.name = name
        self.__id = user_id

    # Getter: Cho phép đọc thuộc tính private một cách an toàn
    def get_id(self) -> int:
        return self.__id

    # Setter: Kiểm tra điều kiện dữ liệu trước khi lưu trữ
    def set_id(self, new_id: int) -> None:
        if new_id > 10000:
            self.__id = new_id


p = Person("Tobias")
print(p.name)
print(p.get_id())

# Cập nhật giá trị hợp lệ qua setter
p.set_id(43992)
print(p.get_id())

# Đối tượng không thể truy cập trực tiếp vào thuộc tính private:
try:
    print(p.__id)
except AttributeError as e:
    print("Cannot access private attribute directly:", e)


# 2. Getter, Setter và Deleter chuẩn Pythonic với @property
# Thứ tự: @property (Getter) phải đứng trước @<name>.setter và @<name>.deleter:
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Getter: Đọc giá trị thuộc tính
    @property
    def radius(self) -> float:
        return self._radius

    # Setter: Xác thực dữ liệu khi gán
    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    # Deleter: Dọn dẹp thuộc tính khi dùng lệnh del
    @radius.deleter
    def radius(self) -> None:
        print("Deleting radius...")
        del self._radius

    # Thuộc tính chỉ đọc (Read-only property, không có setter)
    @property
    def area(self) -> float:
        return 3.14 * (self._radius ** 2)


my_circle = Circle(5)
print("Initial radius:", my_circle.radius)
print("Initial area:", my_circle.area)

my_circle.radius = 8
print("After modifying radius:", my_circle.radius)
print("After modifying area:", my_circle.area)

del my_circle.radius
try:
    print(my_circle.radius)
except AttributeError as e:
    print("Error:", e)
