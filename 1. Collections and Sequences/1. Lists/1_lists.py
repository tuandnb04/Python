# 0. Tổng quan 4 cấu trúc dữ liệu Collections trong Python:
# - List      : Có thứ tự (Ordered), Thay đổi được (Changeable / Mutable), Cho phép trùng lặp (Allow duplicates).
# - Tuple     : Có thứ tự (Ordered), KHÔNG thay đổi được (Unchangeable / Immutable), Cho phép trùng lặp.
# - Set       : KHÔNG thứ tự (Unordered), KHÔNG đánh chỉ mục (Unindexed), KHÔNG cho phép trùng lặp (No duplicates).
# - Dictionary: Có thứ tự (Ordered từ Python 3.7+), Thay đổi được (Changeable), Khóa KHÔNG trùng lặp.

# 1. Khởi tạo List, Kiểu dữ liệu & list() constructor:
# - List cho phép phần tử trùng lặp và chứa nhiều kiểu dữ liệu hỗn hợp (Mixed Data Types):
fruits_list = ["apple", "banana", "cherry", "apple", "cherry"]
mixed_list = ["abc", 34, True, 40, "male"]
print("List with duplicates:", fruits_list)
print("Mixed data types:   ", mixed_list)
print("Data type of list:  ", type(fruits_list))  # <class 'list'>
print("List length len():  ", len(fruits_list))   # 5

# - Dùng list() constructor (lưu ý cặp ngoặc tròn đôi khi truyền tuple):
from_tuple = list(("apple", "banana", "cherry"))
chars = list('Jessica')
print("list() from tuple:  ", from_tuple)
print("list() from string: ", chars)  # ['J', 'e', 's', 's', 'i', 'c', 'a']

# 2. Truy cập phần tử (Access Items) & Indexing:
# - Chỉ mục dương (Zero-based): Phần tử đầu tiên có index [0], thứ hai có index [1]
# - Chỉ mục âm (Negative indexing): Bắt đầu từ cuối danh sách (-1 là phần tử cuối, -2 là kế cuối)
cities = ['Los Angeles', 'London', 'Tokyo']
print("Index 0 & 1:        ", cities[0], cities[1])    # 'Los Angeles' 'London'
print("Negative -1 & -2:   ", cities[-1], cities[-2])  # 'Tokyo' 'London'
# cities[10] -> Lỗi IndexError: list index out of range

# 3. Cắt lát dải chỉ mục (Range of Indexes / Slicing):
# Cú pháp: [start:stop:step] - Lấy từ index start (bao gồm) đến trước stop (không bao gồm)
sample_fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Slicing [2:5]:      ", sample_fruits[2:5])        # ['cherry', 'orange', 'kiwi']
print("From start [:4]:    ", sample_fruits[:4])         # ['apple', 'banana', 'cherry', 'orange']
print("To the end [2:]:    ", sample_fruits[2:])         # ['cherry', 'orange', 'kiwi', 'melon', 'mango']
print("Negative range [-4:-1]:", sample_fruits[-4:-1])   # ['orange', 'kiwi', 'melon'] (từ -4 đến trước -1)

# Bước nhảy (step) và đảo ngược:
nums = [1, 2, 3, 4, 5, 6]
print("Step 2 [1::2]:      ", nums[1::2])                # [2, 4, 6]
print("Reversed [::-1]:    ", nums[::-1])                # [6, 5, 4, 3, 2, 1]

# 4. Thay đổi giá trị phần tử (Change Item Values & Slice Assignment):
# - Thay đổi 1 phần tử đơn bằng chỉ mục:
fruits_change = ["apple", "banana", "cherry"]
fruits_change[1] = "blackcurrant"
print("Change single item: ", fruits_change)  # ['apple', 'blackcurrant', 'cherry']

# - Thay đổi một dải phần tử bằng gán lát cắt (Slice Assignment):
# 1. Thay thế đúng số lượng phần tử:
fruits_range = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits_range[1:3] = ["blackcurrant", "watermelon"]
print("Replace range [1:3]:", fruits_range)   # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# 2. Chèn nhiều hơn số phần tử bị thay thế (Danh sách giãn ra):
fruits_expand = ["apple", "banana", "cherry"]
fruits_expand[1:2] = ["blackcurrant", "watermelon"]
print("Expand via slice:   ", fruits_expand)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

# 3. Chèn ít hơn số phần tử bị thay thế (Danh sách co lại):
fruits_shrink = ["apple", "banana", "cherry"]
fruits_shrink[1:3] = ["watermelon"]
print("Shrink via slice:   ", fruits_shrink)  # ['apple', 'watermelon']

# - Cập nhật cơ bản, Xóa (del) & Kiểm tra tồn tại (in):
langs = ['Python', 'Java', 'Rust']
langs[0] = 'JavaScript'  # List có tính Mutable (có thể gán lại giá trị)
del langs[1]
print("Updated list:       ", langs)          # ['JavaScript', 'Rust']

# Kiểm tra tồn tại với từ khóa 'in':
if "Rust" in langs:
    print("Check with 'in':    'Rust' is in langs")

# 5. Nested List & Unpacking
dev = ['Alice', 25, ['Python', 'Rust', 'C++']]
print("Nested element:     ", dev[2][1])  # 'Rust' (truy cập phần tử trong list lồng nhau)

# Unpacking cơ bản & Unpacking gom phần còn lại (*)
name, age, skills = dev
print("Unpacked:           ", name, age)  # 'Alice' 25
name, *rest = dev
print("Unpacked with *:    ", name, rest)  # 'Alice' [25, ['Python', 'Rust', 'C++']]

# 6. Thêm phần tử vào List (Add List Items: append, insert, extend):
# - append(x): Thêm 1 phần tử vào cuối danh sách
fruits_add = ["apple", "banana", "cherry"]
fruits_add.append("orange")
print("append('orange'):   ", fruits_add)  # ['apple', 'banana', 'cherry', 'orange']

# - insert(index, x): Chèn 1 phần tử vào vị trí chỉ mục xác định (không thay thế phần tử cũ)
fruits_add.insert(1, "mango")
print("insert(1, 'mango'): ", fruits_add)  # ['apple', 'mango', 'banana', 'cherry', 'orange']

# - extend(iterable): Nối các phần tử của một danh sách khác vào cuối danh sách hiện tại
tropical = ["pineapple", "papaya"]
fruits_add.extend(tropical)
print("extend(tropical):   ", fruits_add)  # ['apple', 'mango', 'banana', 'cherry', 'orange', 'pineapple', 'papaya']

# - extend() chấp nhận BẤT KỲ đối tượng Iterable nào (như Tuple, Set...):
berry_tuple = ("kiwi", "blueberry")
fruits_add.extend(berry_tuple)             # Thêm các phần tử của Tuple vào List
print("extend(berry_tuple):", fruits_add)

# 7. Xóa phần tử trong List (Remove List Items: remove, pop, del, clear):
# - remove(value): Xóa phần tử đầu tiên có giá trị chỉ định (báo lỗi ValueError nếu không tồn tại)
dup_numbers = [10, 20, 30, 40, 50, 50, 50]
dup_numbers.remove(50)  # Chỉ xóa lần xuất hiện đầu tiên của giá trị 50
print("remove(50):        ", dup_numbers)  # [10, 20, 30, 40, 50, 50]
# dup_numbers.remove(99)  # Lỗi ValueError: list.remove(x): x not in list

# - pop(index): Xóa phần tử theo chỉ mục và trả về phần tử đó
#   Nếu không truyền index, mặc định xóa và trả về phần tử cuối cùng (.pop())
pop_nums = [1, 2, 3, 4, 5]
last_item = pop_nums.pop()    # 5 (phần tử cuối)
item_at_1 = pop_nums.pop(1)   # 2 (phần tử tại index 1)
print("pop result:         ", pop_nums, "| Popped items:", last_item, item_at_1)  # [1, 3, 4] | Popped: 5 2

# - del list[index]: Xóa phần tử tại chỉ mục chỉ định
fruits_del = ["apple", "banana", "cherry"]
del fruits_del[0]             # Xóa phần tử đầu tiên ("apple")
print("del fruits_del[0]:  ", fruits_del)  # ['banana', 'cherry']

# - clear(): Làm rỗng danh sách (danh sách vẫn tồn tại nhưng không có phần tử: [])
fruits_del.clear()
print("clear() empty list: ", fruits_del)  # []

# - del list: Xóa hoàn toàn biến danh sách ra khỏi bộ nhớ (namespace)
del fruits_del
# print(fruits_del) -> Báo lỗi NameError: name 'fruits_del' is not defined

# 8. Duyệt qua Danh sách (Loop Through a List - 4 phương pháp phổ biến):
loop_fruits = ["apple", "banana", "cherry"]

# - Cách 1: Duyệt trực tiếp từng phần tử bằng for loop (Pythonic & thông dụng nhất)
print("--- Loop items directly ---")
for fruit in loop_fruits:
    print("Fruit item:", fruit)

# - Cách 2: Duyệt qua chỉ số index bằng for và range(len(...))
print("--- Loop by index range ---")
for i in range(len(loop_fruits)):
    print(f"Index [{i}]:", loop_fruits[i])

# - Cách 3: Duyệt bằng vòng lặp while kết hợp chỉ mục index
print("--- Loop with while loop ---")
idx = 0
while idx < len(loop_fruits):
    print(f"While [{idx}]:", loop_fruits[idx])
    idx += 1

# 9. Sắp xếp & Đảo ngược danh sách (Sort & Reverse Lists):
# - Sắp xếp theo thứ tự chữ cái (Alphabetical) hoặc số (Numerical) mặc định tăng dần:
alpha_fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
alpha_fruits.sort()
print("Alphabetical sort:   ", alpha_fruits)

# - Sắp xếp giảm dần với reverse=True:
alpha_fruits.sort(reverse=True)
print("Sort descending:     ", alpha_fruits)

# - Phân biệt sort() (in-place, sửa trực tiếp) vs sorted() (tạo danh sách MỚI):
raw_numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(raw_numbers)  # Trả về danh sách mới đã sắp xếp
print("sorted() new list:   ", sorted_numbers)
print("sorted(reverse=True):", sorted(raw_numbers, reverse=True))

raw_numbers.sort()  # Sắp xếp in-place, trả về None
print("sort() in-place:     ", raw_numbers)
# Lưu ý: Cả .extend() và .sort() đều là in-place và trả về None -> KHÔNG THỂ chain: a.extend(b).sort() sẽ gây AttributeError

# - Tùy biến tiêu chí sắp xếp với tham số key=function (Customize Sort Function):
def distance_from_50(n):
    return abs(n - 50)  # Số nào có khoảng cách tới 50 nhỏ nhất sẽ đứng đầu

custom_nums = [100, 50, 65, 82, 23]
custom_nums.sort(key=distance_from_50)
print("Custom sort (near 50):", custom_nums)  # [50, 65, 23, 82, 100]

# - Sắp xếp không phân biệt chữ hoa / chữ thường (Case-Insensitive Sort):
# Mặc định sort() phân biệt hoa thường (Case-sensitive), ký tự HOA đứng trước thường theo mã ASCII:
case_fruits = ["banana", "Orange", "Kiwi", "cherry"]
case_fruits.sort()
print("Case-sensitive sort: ", case_fruits)  # ['Kiwi', 'Orange', 'banana', 'cherry'] (chữ HOA lên đầu)

# Dùng key=str.lower để so sánh theo bảng chữ cái tự nhiên:
case_fruits.sort(key=str.lower)
print("Case-insensitive sort:", case_fruits)  # ['banana', 'cherry', 'Kiwi', 'Orange']

# - Đảo ngược danh sách trực tiếp (reverse in-place):
nums_to_reverse = [6, 5, 4, 3, 2, 1]
nums_to_reverse.reverse()  # reverse(): Đảo ngược thứ tự các phần tử hiện tại mà không quan tâm giá trị
print("reverse() in-place:  ", nums_to_reverse)

# Lấy k phần tử nhỏ nhất / lớn nhất sau khi sắp xếp in-place:
# - k số nhỏ nhất: arr[:k]
# - k số lớn nhất: arr[-k:]
sample_nums = [19, 2, 35, 1, 67, 41]
sample_nums.sort()
print("Smallest 2:          ", sample_nums[:2])   # [1, 2]
print("Largest 2:           ", sample_nums[-2:])  # [41, 67]

# 10. Sao chép danh sách (Copy a List):
# - Bẫy gán tham chiếu (Reference Assignment Trap):
original_list = ["apple", "banana", "cherry"]
ref_list = original_list  # Chỉ sao chép tham chiếu trỏ cùng vùng nhớ!
ref_list.append("kiwi")
print("Original changed via reference:", original_list)  # ['apple', 'banana', 'cherry', 'kiwi']

# - Cách 1: Dùng phương thức .copy() (Shallow Copy - chuẩn và tường minh nhất):
copy_method_list = original_list.copy()
copy_method_list.append("watermelon")
print("After .copy():       ", copy_method_list)
print("Original untouched:  ", original_list)  # Vẫn là ['apple', 'banana', 'cherry', 'kiwi']

# - Cách 2: Dùng list() constructor:
copy_constructor_list = list(original_list)
copy_constructor_list.append("mango")
print("After list():        ", copy_constructor_list)

# - Cách 3: Dùng toán tử cắt lát [:] (Slice operator):
copy_slice_list = original_list[:]
copy_slice_list.append("orange")
print("After slice [:]:     ", copy_slice_list)

# 11. Nối danh sách (Join / Concatenate Lists - 4 phương pháp):
list_letters = ["a", "b", "c"]
list_numbers = [1, 2, 3]

# - Cách 1: Dùng toán tử cộng '+' (Tạo danh sách MỚI, giữ nguyên 2 danh sách gốc):
joined_plus = list_letters + list_numbers
print("Join with '+':       ", joined_plus)     # ['a', 'b', 'c', 1, 2, 3]

# - Cách 2: Dùng kỹ thuật Unpacking '*' (Pythonic hiện đại, linh hoạt chèn thêm phần tử lẻ):
joined_unpack = [*list_letters, "mid", *list_numbers]
print("Join with '*':       ", joined_unpack)   # ['a', 'b', 'c', 'mid', 1, 2, 3]

# - Cách 3: Dùng phương thức .extend() (Nối trực tiếp tại chỗ in-place, tiết kiệm RAM):
list_extend_demo = ["a", "b", "c"]
list_extend_demo.extend(list_numbers)
print("Join with extend():  ", list_extend_demo) # ['a', 'b', 'c', 1, 2, 3]

# - Cách 4: Duyệt vòng lặp for kết hợp .append() (Hữu ích khi cần thêm logic kiểm tra điều kiện):
list_append_demo = ["a", "b", "c"]
for item in list_numbers:
    list_append_demo.append(item)
print("Join with for-loop:  ", list_append_demo) # ['a', 'b', 'c', 1, 2, 3]

# 12. Tìm vị trí (index) & Đếm số lần xuất hiện (count)
programming_languages = ['Rust', 'Java', 'Python', 'C++', 'Java']
print("index('Java'):", programming_languages.index('Java'))  # 1
print("count('Java'):", programming_languages.count('Java'))  # 2
# programming_languages.index('JavaScript')                 # Lỗi ValueError: 'JavaScript' is not in list

# 13. Type hints và Pattern Matching:
tags: list[str] = ['backend', 'python', 'ai']

match dev:
    case [dev_name, dev_age, [main_skill, *other_skills]]:
        print(f"Dev: {dev_name}, Main skill: {main_skill}, Other: {other_skills}")
    case _:
        pass

# 14. Bảng tra cứu 11 Built-in List Methods:
# +---------------+------------------------------------------------------+
# | Phương thức   | Mô tả chức năng                                      |
# +---------------+------------------------------------------------------+
# | append(x)     | Thêm phần tử vào cuối danh sách                      |
# | clear()       | Xóa sạch tất cả các phần tử khỏi danh sách           |
# | copy()        | Trả về một bản sao nông (shallow copy) của danh sách |
# | count(x)      | Đếm số lần xuất hiện của phần tử x                   |
# | extend(iter)  | Nối các phần tử của một iterable vào cuối danh sách  |
# | index(x)      | Trả về chỉ mục đầu tiên của phần tử có giá trị x     |
# | insert(i, x)  | Chèn phần tử x vào vị trí chỉ mục i                  |
# | pop([i])      | Xóa và trả về phần tử tại vị trí i (mặc định cuối)   |
# | remove(x)     | Xóa phần tử đầu tiên có giá trị bằng x               |
# | reverse()     | Đảo ngược thứ tự các phần tử tại chỗ (in-place)      |
# | sort()        | Sắp xếp danh sách tại chỗ (in-place)                 |
# +---------------+------------------------------------------------------+
