# Định nghĩa Enum kiểu chuỗi với StrEnum:
from enum import StrEnum, auto

# So sánh trực tiếp với chuỗi mà không cần .value:

class UserRole(StrEnum):
    ADMIN = auto()  # Giá trị là "admin"
    MODERATOR = auto()  # Giá trị là "moderator"
    MEMBER = auto()  # Giá trị là "member"
    GUEST = auto()  # Giá trị là "guest"


class OrderStatus(StrEnum):
    PENDING = auto()  # Giá trị là "pending"
    PROCESSING = auto()  # Giá trị là "processing"
    SHIPPED = auto()  # Giá trị là "shipped"
    DELIVERED = auto()  # Giá trị là "delivered"
    CANCELLED = auto()  # Giá trị là "cancelled"


# Sử dụng StrEnum trong ứng dụng thông thường
print("User role:", UserRole.ADMIN)
print("Order status:", OrderStatus.DELIVERED)
print("Is UserRole.ADMIN equal to 'admin'?:", UserRole.ADMIN == "admin")  # True
