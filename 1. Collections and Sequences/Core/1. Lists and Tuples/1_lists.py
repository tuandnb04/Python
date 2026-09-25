# List là cấu trúc dữ liệu tuần tự, có thứ tự, cho phép trùng lặp và CÓ THỂ THAY ĐỔI (Mutable)

# Tạo List & Indexing (Zero-based & Negative)
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0], cities[1])          # 'Los Angeles' 'London' (index 0 là phần tử đầu)
print(cities[-1], cities[-2])        # 'Tokyo' 'London' (index -1 là phần tử cuối)
# cities[10]                         # Lỗi IndexError: list index out of range

# list() constructor & Hàm len()
chars = list('Jessica')
print(chars, len(chars))             # ['J', 'e', 's', 's', 'i', 'c', 'a'] 7

# Cập nhật, Xóa (del) & Kiểm tra tồn tại (in)
langs = ['Python', 'Java', 'Rust']
langs[0] = 'JavaScript'              # List có tính Mutable (có thể gán lại giá trị)
del langs[1]                         # Xóa phần tử tại index 1
print(langs)                         # ['JavaScript', 'Rust']
print('Rust' in langs)               # True (kiểm tra tồn tại)

# Nested List & Unpacking
dev = ['Alice', 25, ['Python', 'Rust', 'C++']]
print(dev[2][1])                     # 'Rust' (truy cập phần tử trong list lồng nhau)

# Unpacking cơ bản & Unpacking gom phần còn lại (*)
name, age, skills = dev              # Gán từng phần tử vào các biến
print(name, age)                     # 'Alice' 25
name, *rest = dev
print(name, rest)                    # 'Alice' [25, ['Python', 'Rust', 'C++']]

# Slicing [start:stop:step] - Lấy từ start đến trước stop
nums = [1, 2, 3, 4, 5, 6]
print(nums[1:4])                     # [2, 3, 4]
print(nums[1::2])                    # [2, 4, 6] (bước nhảy 2)
print(nums[::-1])                    # [6, 5, 4, 3, 2, 1] (mẹo đảo ngược list)

# Thêm phần tử: append, extend, insert
numbers: list[int | float] = [1, 2, 3, 4, 5, 6]
print("append:", numbers)            # [1, 2, 3, 4, 5, 6]

even_numbers = [8, 10]
numbers.extend(even_numbers)         # extend(): Nối các phần tử của list khác vào cuối
print("extend:", numbers)            # [1, 2, 3, 4, 5, 6, 8, 10]

numbers.insert(2, 2.5)               # insert(index, item): Chèn phần tử vào vị trí chỉ định
print("insert:", numbers)            # [1, 2, 2.5, 3, 4, 5, 6, 8, 10]

# Xóa phần tử: remove, pop, clear
dup_numbers = [10, 20, 30, 40, 50, 50, 50]
dup_numbers.remove(50)               # remove(): Chỉ xóa lần xuất hiện đầu tiên của giá trị
print("remove:", dup_numbers)        # [10, 20, 30, 40, 50, 50]
# dup_numbers.remove(99)             # Lỗi ValueError: list.remove(x): x not in list

pop_nums = [1, 2, 3, 4, 5]
last_item = pop_nums.pop()           # pop(): Mặc định xóa và trả về phần tử cuối cùng (5)
item_at_1 = pop_nums.pop(1)          # pop(index): Xóa và trả về phần tử tại index 1 (2)
print("pop:", pop_nums, "| Popped:", last_item, item_at_1) # [1, 3, 4] | Popped: 5 2

pop_nums.clear()                     # clear(): Xóa sạch tất cả phần tử bên trong list
print("clear:", pop_nums)            # []

# Sắp xếp & Đảo ngược: sort, sorted, reverse
raw_numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(raw_numbers) # sorted(): Hàm trả về một danh sách MỚI đã sắp xếp
print("sorted():", sorted_numbers)
print("sorted(reverse=True):", sorted(raw_numbers, reverse=True))

raw_numbers.sort()                   # sort(): Phương thức sắp xếp trực tiếp tại chỗ (in-place)
print("sort():", raw_numbers)
# Lưu ý: Cả .extend() và .sort() đều là in-place và trả về None -> KHÔNG THỂ chain: a.extend(b).sort() sẽ gây AttributeError
# Lấy k phần tử nhỏ nhất / lớn nhất chuẩn thực tế (không cần import, nhanh nhất nhờ sort in-place):
# Sắp xếp in-place rồi cắt lát (slicing) 2 đầu:
# - k số nhỏ nhất: arr[:k]
# - k số lớn nhất: arr[-k:]
sample_nums = [19, 2, 35, 1, 67, 41]
sample_nums.sort()
print("Smallest 2:", sample_nums[:2])  # [1, 2]
print("Largest 2:", sample_nums[-2:])  # [41, 67]

nums_to_reverse = [6, 5, 4, 3, 2, 1]
nums_to_reverse.reverse()            # reverse(): Đảo ngược thứ tự trực tiếp tại chỗ (in-place)
print("reverse():", nums_to_reverse)

# Tìm vị trí (index) & Đếm số lần xuất hiện (count)
programming_languages = ['Rust', 'Java', 'Python', 'C++', 'Java']
print("index('Java'):", programming_languages.index('Java')) # 1 (trả về index đầu tiên tìm thấy)
print("count('Java'):", programming_languages.count('Java')) # 2 (đếm số lần 'Java' xuất hiện)
# programming_languages.index('JavaScript')                 # Lỗi ValueError: 'JavaScript' is not in list

# Python hiện đại (Python 3.9+ / 3.10+)
tags: list[str] = ['backend', 'python', 'ai']                # Type hints chuẩn Python 3.9+

match dev:                                                   # Structural Pattern Matching (Python 3.10+)
    case [dev_name, dev_age, [main_skill, *other_skills]]:
        print(f"Dev: {dev_name}, Main skill: {main_skill}, Other: {other_skills}")
    case _:
        pass

