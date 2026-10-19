# 1. Khởi tạo danh sách (List) và truy cập chỉ mục (Indexing)
# Danh sách lưu trữ nhiều giá trị trong cặp ngoặc vuông [].
# Vị trí (index) bắt đầu từ 0. Dùng số âm để đếm ngược từ cuối bảng (-1 là phần tử cuối):
fruits = ["apple", "banana", "cherry"]
print("First item [0]:", fruits[0])    # 'apple'
print("Last item [-1]:", fruits[-1])   # 'cherry'

# 2. Cắt lát danh sách (Slicing: [start : stop : step])
# Cắt lát tạo ra một danh sách mới, không làm thay đổi danh sách gốc:
nums = [10, 20, 30, 40, 50]
print("Slice [1:4]:", nums[1:4])        # [20, 30, 40] (lấy từ index 1 đến trước 4)
print("From start [:3]:", nums[:3])     # [10, 20, 30] (khuyết start: lấy từ đầu)
print("To end [3:]:", nums[3:])         # [40, 50] (khuyết stop: lấy đến hết)
print("Step 2 [::2]:", nums[::2])       # [10, 30, 50] (lấy cách quãng mỗi 2 phần tử)
print("Reversed [::-1]:", nums[::-1])   # [50, 40, 30, 20, 10] (đảo ngược danh sách)

# 3. Giải nén (Unpacking):
first, *rest = [1, 2, 3, 4]
print(f"first: {first}, rest: {rest}")  # 1, [2, 3, 4]

# 4. Thay đổi giá trị phần tử và gán lát cắt (Slice Assignment):
fruits[0] = "mango"                     # Đổi 1 phần tử theo chỉ mục
print("After item change:", fruits)     # ['mango', 'banana', 'cherry']

fruits[1:3] = ["kiwi", "pear"]          # Thay thế đồng thời một dải phần tử
print("After slice change:", fruits)    # ['mango', 'kiwi', 'pear']

# 5. Thêm phần tử (.append, .insert, .extend):
fruits.append("orange")         # Thêm vào cuối danh sách
fruits.insert(1, "berry")       # Chèn vào vị trí chỉ định (index 1)
fruits.extend(["melon", "fig"]) # Nối thêm một danh sách khác vào cuối
print("After adding:", fruits)

# 6. Xóa phần tử (.remove, .pop, del):
fruits.remove("kiwi")         # Xóa theo giá trị đầu tiên trùng khớp
popped_first = fruits.pop(0)  # Xóa theo chỉ mục và trả về giá trị
popped_last = fruits.pop()    # Không truyền tham số: mặc định xóa phần tử cuối
del fruits[0]                 # Xóa theo chỉ mục bằng từ khóa del
print("Popped first:", popped_first)
print("Popped last:", popped_last)
print("Remaining fruits:", fruits)

# 7. Duyệt qua danh sách:
for fruit in fruits:
    print("Fruit:", fruit)

# 8. Sắp xếp (.sort và sort(reverse=True)):
nums = [19, 2, 35, 1, 67]
nums.sort()                                # Sắp xếp tăng dần tại chỗ
print("sort() ascending: ", nums)
nums.sort(reverse=True)                    # Sắp xếp giảm dần với reverse=True
print("sort() descending:", nums)

# 9. Sao chép (bẫy tham chiếu vs .copy()):
original = [1, 2, 3]
copy_list = original.copy()                # Bản sao độc lập, thay đổi không ảnh hưởng original
copy_list.append(99)
print(f"Copy: {copy_list} | Original: {original}")

# 10. Nối (+), nhân bản lặp lại (*) và giải nén (*):
print("Join with '+':", [1, 2] + [3, 4])
print("Repeat with '*':", [1, 2] * 3)                   # [1, 2, 1, 2, 1, 2]
print("Unpack with '*':", [*[1, 2], "mid", *[3, 4]])    # [1, 2, 'mid', 3, 4]

# 11. Tìm vị trí (.index) và Đếm số lần xuất hiện (.count):
langs = ['Python', 'Java', 'Python']
print("Index of 'Java':", langs.index('Java'))          # 1
print("Count of 'Python':", langs.count('Python'))      # 2

# Tóm tắt 11 phương thức tích hợp sẵn của List:
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort


# 12. Tuple: Chuỗi bất biến (immutable sequence)
# Khởi tạo bằng cặp ngoặc tròn (), không thể thay đổi sau khi tạo:
t = ("apple", "banana", "cherry", "orange", "kiwi")

# Truy cập bằng chỉ mục:
print("\nFirst tuple item [0]:", t[0])
print("Last tuple item [-1]:", t[-1])

# Độ dài (len) và kiểm tra tồn tại (in):
print("Tuple length:", len(t))
print("Contains 'apple':", "apple" in t)

# Cắt lát (Slicing tạo ra một tuple mới):
print("Slice [1:4]:", t[1:4])  # Lấy index 1, 2, 3: ('banana', 'cherry', 'orange')
print("From start [:3]:", t[:3])  # 3 phần tử đầu: ('apple', 'banana', 'cherry')
print("To end [2:]:", t[2:])      # Từ index 2 đến hết: ('cherry', 'orange', 'kiwi')

# Tuple có 1 phần tử bắt buộc phải có dấu phẩy ở cuối:
single = ("apple",)

# Cập nhật gián tiếp qua list (khi cần sửa dữ liệu của tuple):
# Chuyển sang list -> sửa phần tử -> chuyển ngược lại tuple:
temp = list(t)
temp[1] = "mango"
t_updated = tuple(temp)
print("Updated via list:", t_updated)

# 3. Đóng gói (Packing) & Giải nén (Unpacking):
# Giải nén cơ bản (số lượng biến phải khớp chính xác số phần tử):
a, b, c = (1, 2, 3)
print("\nUnpacked:", a, b, c)

# Dùng dấu * để gom các phần tử còn lại vào một list:
first, *rest = (1, 2, 3, 4)
print(f"first: {first} | rest (list): {rest}")

# Hoán đổi biến nhanh gọn không cần biến tạm:
x, y = 10, 20
x, y = y, x
print(f"Swapped: x={x}, y={y}")

# 4. Duyệt qua Tuple bằng vòng lặp for (hoạt động tương tự như List):
for item in t:
    print("Tuple item:", item)

# 5. Nối (+), nhân bản (*) & 2 phương thức duy nhất của Tuple (.count, .index):
t1 = (1, 2)
t2 = (3, 4)
print("Join tuples (+):", t1 + t2)
print("Repeat tuple (*):", t1 * 3)

chars = ("a", "b", "c", "b")
print("count('b'):", chars.count("b"))  # Đếm số lần xuất hiện: 2
print("index('b'):", chars.index("b"))  # Vị trí đầu tiên: 1 (Key/ValueError nếu không thấy)

# Các hàm tích hợp sẵn hỗ trợ Tuple: min(), max(), sum():
scores = (7, 9, 5)
print(f"min: {min(scores)}, max: {max(scores)}, sum: {sum(scores)}")

# Tóm tắt 3 khác biệt cốt lõi giữa List và Tuple:
# 1. Khả năng thay đổi: List thay đổi được (mutable), Tuple không thể thay đổi (immutable).
# 2. Phương thức: List có 11 phương thức, Tuple chỉ có đúng 2 phương thức (.count và .index).
# 3. Hiệu năng: Tuple xử lý nhanh hơn và tốn ít bộ nhớ RAM hơn List.
