# Định nghĩa Enum kiểu chuỗi với enum.StrEnum (Python 3.11+ PEP 663)
from enum import StrEnum, auto

# => TẠI SAO STRENUM TỐT HƠN DÙNG CHUỖI TỰ DO (STRINGS) HOẶC ENUM THƯỜNG?
# Type Safety & Auto-complete: Tránh lỗi gõ sai chính tả (typo) các giá trị cố định.
# Hoạt động như một chuỗi thực thụ: `NodeType.FILE == "file"` là True mà không cần `.value`.
# Tự động sinh giá trị bằng `auto()` giúp code siêu ngắn gọn và sạch sẽ.

class UserRole(StrEnum):
    ADMIN = auto()                     # Giá trị là "admin"
    MODERATOR = auto()                 # Giá trị là "moderator"
    MEMBER = auto()                    # Giá trị là "member"
    GUEST = auto()                     # Giá trị là "guest"

class OrderStatus(StrEnum):
    PENDING = auto()                   # Giá trị là "pending"
    PROCESSING = auto()                # Giá trị là "processing"
    SHIPPED = auto()                   # Giá trị là "shipped"
    DELIVERED = auto()                 # Giá trị là "delivered"
    CANCELLED = auto()                 # Giá trị là "cancelled"

# Sử dụng StrEnum trong ứng dụng thông thường
print("User role:", UserRole.ADMIN)
print("Order status:", OrderStatus.DELIVERED)
print("Is UserRole.ADMIN equal to 'admin'?:", UserRole.ADMIN == "admin") # True

