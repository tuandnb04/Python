# Module typing trong Thư viện chuẩn Python (Standard Library)
from typing import Literal, Final, TypedDict, Self

# Hằng số (Final) - Báo hiệu giá trị không được gán lại
API_VERSION: Final[str] = "v1"

# Literal & Type Statement (Python 3.12+ PEP 695)
# Thay vì 'Status = Literal[...]' cũ, dùng từ khóa 'type' chuẩn hiện đại
type Status = Literal["pending", "completed", "failed"]
current_status: Status = "completed"

# TypedDict - Định nghĩa kiểu tĩnh cho cấu trúc Dictionary
class UserProfile(TypedDict):
    username: str
    age: int
    is_active: bool

user: UserProfile = {"username": "alice", "age": 25, "is_active": True}

# [PYTHON 3.11+ PEP 673]: typing.Self cho Fluent Interface / Method Chaining
# Tự động suy luận kiểu trả về là chính class hiện tại (không cần gõ chuỗi hoặc TypeVar)
class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, fields: str) -> Self:
        self.query += f"SELECT {fields} "
        return self

    def from_table(self, table: str) -> Self:
        self.query += f"FROM {table}"
        return self

qb = QueryBuilder().select("name, age").from_table("users")
print("Constructed Query (Self chaining):", qb.query)

print("API Version (Final):", API_VERSION)
print("Status (Literal):", current_status)
print("User profile (TypedDict):", user)
