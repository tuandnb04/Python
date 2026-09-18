# Định nghĩa Enum kiểu chuỗi với enum.StrEnum (Python 3.11+ PEP 663)
from enum import StrEnum, auto

# => TẠI SAO STRENUM TỐT HƠN DÙNG CHUỖI TỰ DO (STRINGS) HOẶC ENUM THƯỜNG?
# 1. Type Safety & Auto-complete: Tránh lỗi gõ sai chính tả (typo) tên loại Node / Relation.
# 2. Hoạt động như một chuỗi thực thụ: `NodeType.FILE == "file"` là True mà không cần `.value`.
# 3. Tự động sinh giá trị bằng `auto()` giúp code siêu ngắn gọn và sạch sẽ.

class NodeType(StrEnum):
    REPOSITORY = auto()                # Giá trị là "repository"
    DIRECTORY = auto()                 # Giá trị là "directory"
    FILE = auto()                      # Giá trị là "file"
    MODULE = auto()                    # Giá trị là "module"
    CLASS = auto()                     # Giá trị là "class"
    FUNCTION = auto()                  # Giá trị là "function"
    METHOD = auto()                    # Giá trị là "method"

class RelationType(StrEnum):
    CONTAINS = auto()
    DEFINES = auto()
    IMPORTS = auto()
    CALLS = auto()
    INHERITS = auto()

# Sử dụng StrEnum trong hệ thống Code Graph
print("Node type:", NodeType.CLASS)
print("Relation type:", RelationType.CALLS)
print("Is NodeType.FILE equal to 'file'?:", NodeType.FILE == "file") # True
