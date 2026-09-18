import sys
from dataclasses import dataclass


# BẢN CHẤT CỦA HAI DẤU GẠCH DƯỚI (__) - CƠ CHẾ NAME MANGLING
# Trong Python, tiền tố __ KHÔNG thực sự biến thuộc tính thành private hoàn toàn.
# Python tự động đổi tên __attribute thành: _ClassName__attribute
# Mục đích chính: Tránh việc class con vô tình ghi đè (accidental overriding)
# thuộc tính của class cha khi kế thừa.

class Parent:
    def __init__(self) -> None:
        self.__data: str = "Dữ liệu lớp cha"

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.__data: str = "Dữ liệu lớp con"

print("--- 1. CƠ CHẾ NAME MANGLING & KẾ THỪA ---")
c = Child()
print("Các thuộc tính thực tế trong object con (qua __dict__):")
print(c.__dict__)
# Cả dữ liệu của cha và con đều được lưu độc lập, không bị đè:
# {'_Parent__data': 'Dữ liệu lớp cha', '_Child__data': 'Dữ liệu lớp con'}


# TỐI ƯU BỘ NHỚ VÀ KHÓA THUỘC TÍNH VỚI __slots__
# - Mặc định, mỗi instance class trong Python đều có 1 cuốn từ điển ngầm `__dict__`
#   để chứa thuộc tính -> tốn RAM và cho phép bên ngoài gán thuộc tính lung tung.
# - Dùng __slots__ để:
#   Tiết kiệm 40% - 60% RAM khi tạo hàng triệu object.
#   Ngăn chặn việc tùy tiện thêm thuộc tính rác ngoài danh sách khai báo.

print("\n--- 2. TỐI ƯU BỘ NHỚ VỚI __slots__ ---")
class StrictWallet:
    __slots__ = ("_balance", "_tag")

    def __init__(self, balance: float) -> None:
        self._balance: float = balance
        self._tag: str = "Personal"

    @property
    def balance(self) -> float:
        return self._balance


wallet = StrictWallet(100.0)
print("Số dư StrictWallet:", wallet.balance)

# Thử gán thêm thuộc tính lạ không có trong __slots__:
try:
    wallet.hack_attr = "Unauthorized"
except AttributeError as e:
    print("Lỗi Slots khi gán thuộc tính lạ:", e)


# ĐÓNG BĂNG DỮ LIỆU BẤT BIẾN VỚI @dataclass(frozen=True)
# - Mutable (Có thể thay đổi): Dễ bị sửa đổi dữ liệu ngoài ý muốn.
# - Immutable (Bất biến / Read-Only): Sinh ra để chỉ đọc, không thể thay đổi.
# - @dataclass(frozen=True, slots=True): Cung cấp một model bất biến hoàn hảo,
#   vừa nhẹ RAM vừa an toàn tuyệt đối, rất hay dùng cho Config, Value Object, DTO.

print("\n--- 3. ĐÓNG GÓI BẤT BIẾN VỚI @dataclass(frozen=True, slots=True) ---")
@dataclass(frozen=True, slots=True)
class ReadOnlyAccount:
    account_id: str
    owner: str
    balance: float


account = ReadOnlyAccount(account_id="ACC-8899", owner="Alice", balance=500.0)
print("Thông tin tài khoản:", account)
print("Chủ sở hữu:", account.owner)

# Thử thay đổi số dư -> BỊ CHẶN
try:
    account.balance = 9999.0
except Exception as e:
    print("Lỗi khi cố sửa giá trị (frozen):", type(e).__name__, "-", e)

# Thử thêm thuộc tính mới -> BỊ CHẶN
try:
    account.note = "VIP"
except Exception as e:
    print("Lỗi khi cố thêm thuộc tính mới (slots):", type(e).__name__, "-", e)

# Vì là bất biến (Immutable), đối tượng có thể dùng làm Key trong Dict hoặc Set:
accounts_map = {
    account: "Hoạt động tốt"
}
print("Dùng làm Key Dict:", accounts_map[account])
