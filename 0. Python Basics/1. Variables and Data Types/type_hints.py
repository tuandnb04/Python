# Ghi chú kiểu dữ liệu cho Biến (Type Annotations for Variables)

# Khai báo kiểu dữ liệu cho các kiểu nguyên thủy
name: str = "Alice"
age: int = 25
rating: float = 4.8
is_active: bool = True

# Khai báo biến với kiểu dữ liệu trước khi gán giá trị
user_id: int
user_id = 101

# Kiểu kết hợp nhiều kiểu nguyên thủy (Union với toán tử '|')
score: int | float = 95.5
score = 100

print("Name:", name)
print("Age:", age)
print("Rating:", rating)
print("Active:", is_active)
print("User ID:", user_id)
print("Score:", score)
