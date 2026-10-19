# Dictionary: cấu trúc lưu trữ cặp Khóa - Giá trị (Key-Value), bảo toàn thứ tự chèn, tra cứu O(1)

# 1. Khởi tạo và cấu trúc Key-Value:
# Dictionary lưu trữ theo cặp Khóa - Giá trị, các khóa (keys) bắt buộc phải là duy nhất:
user = {"name": "Emil", "age": 22, "role": "admin"}
print("Initial user:", user)

# Nếu trùng khóa, giá trị khai báo sau sẽ ghi đè giá trị trước:
duplicate_key = {"name": "Emil", "name": "Tobias"}
print("Duplicate key overwritten:", duplicate_key)

# 2. Truy cập dữ liệu (Ngoặc vuông [] vs .get()):
print("Access by key:", user["name"])                 # 'Emil' (KeyError nếu không có)
print("Safe get (missing key):", user.get("city"))    # Trả về None thay vì báo lỗi
print("Safe get with default:", user.get("city", "Oslo"))  # Trả về 'Oslo' nếu không có
print("Check key exists:", "role" in user)            # True (tra cứu O(1))

# 3. Thêm, sửa & gộp từ điển:
# Gán bằng d[key] = value: nếu key có sẵn thì sửa, nếu chưa có thì thêm mới:
user["name"] = "Tobias"           # Key đã có: cập nhật giá trị
user["city"] = "Oslo"             # Key chưa có: tự động thêm mới
print("After assign:", user)

# Phương thức update() cho phép cập nhật hoặc thêm nhiều key cùng lúc:
user.update({"age": 19, "status": "active"})
print("After update():", user)

# Toán tử gộp '|' (Python 3.9+) kết hợp tạo dict mới:
merged = user | {"theme": "dark"}
print("Merged dict (|):", merged)

# 4. Lấy danh sách keys, values, items:
print("Keys:", list(user.keys()))
print("Values:", list(user.values()))
print("Items:", list(user.items()))

# 5. Xóa phần tử (.pop, popitem, del):
# pop(key) xóa phần tử chỉ định và TRẢ VỀ giá trị đã xóa:
removed_role = user.pop("role")
print("Removed value via pop():", removed_role)

# Từ khóa del xóa phần tử nhưng KHÔNG trả về giá trị:
del user["city"]

# popitem() xóa và trả về cặp (key, value) chèn vào cuối cùng (LIFO):
last_item = user.popitem()
print("Popped last item:", last_item)
print("User after removals:", user)

# 6. Sao chép độc lập (.copy() hoặc dict()):
# Phương thức copy() tạo bản sao độc lập (thay đổi trên bản sao không ảnh hưởng bản gốc):
copy_user = user.copy()
copy_user["age"] = 99
print("Copy age:", copy_user["age"], "| Original age:", user["age"])

# Cũng có thể dùng hàm khởi tạo dict() để tạo bản sao:
dict_copy = dict(user)
print("Copy via dict():", dict_copy)

# 7. Các cách duyệt qua Dictionary:
# Mặc định vòng lặp for duyệt qua các khóa (keys):
for key in user:
    print(f"Key: {key} -> Value: {user[key]}")

# Duyệt chỉ lấy các giá trị (values):
for val in user.values():
    print("Value only:", val)

# Duyệt đồng thời cả key và value với .items():
for key, val in user.items():
    print(f"Item: {key} = {val}")

# 8. Dictionary lồng nhau (Nested Dictionaries):
# Giá trị của một key có thể là một dictionary khác:
myfamily = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}
print("Nested family dict:", myfamily)

# Truy cập bằng chuỗi các khóa liên tiếp [key1][key2]:
print("child1 name:", myfamily["child1"]["name"])

# Truy cập sâu an toàn bằng .get() lồng nhau:
print("Missing child name:", myfamily.get("child4", {}).get("name", "Unknown"))

# 9. Đếm tần suất phần tử bằng dict.get():
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Word counts:", counts)
