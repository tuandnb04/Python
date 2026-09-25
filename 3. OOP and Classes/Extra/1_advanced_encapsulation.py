import sys
from dataclasses import dataclass


# 1. BẢN CHẤT CỦA HAI DẤU GẠCH DƯỚI (__) - CƠ CHẾ NAME MANGLING
# Trong Python, tiền tố __ KHÔNG thực sự biến thuộc tính thành private tuyệt đối.
# Python tự động đổi tên __attribute thành: _ClassName__attribute
# Mục đích chính: Tránh việc class con vô tình ghi đè (accidental overriding) thuộc tính của class cha.

class Example:
    def __init__(self, internal: str, private: str) -> None:
        self._internal = internal
        self.__private = private

example = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example._internal)
# Truy cập trực tiếp qua tên mới sau khi mangled:
print(example._Example__private) # type: ignore
print("Attributes dictionary:", example.__dict__)


# 2. NAME MANGLING TRONG KẾ THỪA: TRÁNH GHI ĐÈ NHẦM DỮ LIỆU
class Parent:
    def __init__(self) -> None:
        self.__data: str = "Parent data"

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.__data: str = "Child data"

c = Child()
print("Attributes with name mangling:", c.__dict__)
# Cả dữ liệu của cha và con đều được lưu độc lập, không bị đè:
# {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}


# Nếu KHÔNG dùng double underscore (__), thuộc tính cha sẽ bị class con ghi đè mất:
class UnsafeParent:
    def __init__(self) -> None:
        self.data: str = "Parent data"

class UnsafeChild(UnsafeParent):
    def __init__(self) -> None:
        super().__init__()
        self.data: str = "Child data"

unsafe_c = UnsafeChild()
print("Without name mangling (parent data overwritten):", unsafe_c.__dict__)  # {'data': 'Child data'}


# TỐI ƯU BỘ NHỚ VÀ KHÓA THUỘC TÍNH VỚI __slots__
# - Mặc định, mỗi instance class trong Python đều có 1 cuốn từ điển ngầm `__dict__`
#   để chứa thuộc tính -> tốn RAM và cho phép bên ngoài gán thuộc tính lung tung.
# - Dùng __slots__ để:
#   Tiết kiệm 40% - 60% RAM khi tạo hàng triệu object.
#   Ngăn chặn việc tùy tiện thêm thuộc tính rác ngoài danh sách khai báo.

class StrictWallet:
    __slots__ = ("_balance", "_tag")

    def __init__(self, balance: float) -> None:
        self._balance: float = balance
        self._tag: str = "Personal"

    @property
    def balance(self) -> float:
        return self._balance


wallet = StrictWallet(100.0)
print("StrictWallet balance:", wallet.balance)

# Thử gán thêm thuộc tính lạ không có trong __slots__:
try:
    wallet.hack_attr = "Unauthorized" # type: ignore
except AttributeError as e:
    print("Slots error when assigning unauthorized attribute:", e)


# ĐÓNG BĂNG DỮ LIỆU BẤT BIẾN VỚI @dataclass(frozen=True)
# - Mutable (Có thể thay đổi): Dễ bị sửa đổi dữ liệu ngoài ý muốn.
# - Immutable (Bất biến / Read-Only): Sinh ra để chỉ đọc, không thể thay đổi.
# - @dataclass(frozen=True, slots=True): Cung cấp một model bất biến hoàn hảo,
#   vừa nhẹ RAM vừa an toàn tuyệt đối, rất hay dùng cho Config, Value Object, DTO.

@dataclass(frozen=True, slots=True)
class ReadOnlyAccount:
    account_id: str
    owner: str
    balance: float


account = ReadOnlyAccount(account_id="ACC-8899", owner="Alice", balance=500.0)
print("Account info:", account)
print("Account owner:", account.owner)

# Thử thay đổi số dư -> BỊ CHẶN
try:
    account.balance = 9999.0 # type: ignore
except Exception as e:
    print("Error when mutating frozen object:", type(e).__name__, "-", e)

# Thử thêm thuộc tính mới -> BỊ CHẶN
try:
    account.note = "VIP" # type: ignore
except Exception as e:
    print("Error when adding new attribute to slotted object:", type(e).__name__, "-", e)

# Vì là bất biến (Immutable), đối tượng có thể dùng làm Key trong Dict hoặc Set:
accounts_map = {
    account: "Active"
}
print("Used as Dict key:", accounts_map[account])
