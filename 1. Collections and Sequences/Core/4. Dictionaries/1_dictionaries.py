# Từ điển (Dictionary) là cấu trúc dữ liệu lưu trữ các cặp khóa - giá trị (Key - Value)
# Tương tự từ điển giấy: tra Key để tìm Value tương ứng

# Khai báo dictionary (ví dụ tiếng Anh gốc)
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# Khởi tạo bằng dict() constructor với list of tuples
pizza_dict_constructor = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])

# Quy tắc về Key và Value
# - Key phải là duy nhất và bất biến (immutable)
# - Value có thể trùng lặp và nhận bất kỳ kiểu dữ liệu nào

# Truy cập và Cập nhật giá trị
# Truy cập bằng cú pháp ngoặc vuông: dictionary[key]
print(pizza['name'])  # 'Margherita Pizza'

# Cập nhật giá trị (nếu key chưa có thì tự tạo mới)
pizza['name'] = 'Margherita'
print(pizza['name'])  # 'Margherita'

# Các phương thức phổ biến (Methods)
# .get(key, default) - Lấy giá trị an toàn, trả về giá trị mặc định nếu không tìm thấy key
print(pizza.get('toppings', []))  # ['mozzarella', 'basil']
print(pizza.get('discount', 0))   # 0
# Mẹo tối ưu thay thế giá trị (Value Mapping): Dùng dict.get(x, x) trong comprehension để map dữ liệu O(1)
# Nếu x có trong dict thì đổi thành value, không có thì giữ nguyên chính x mà không cần if-else.
VOWELS_MAP = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
mapped_vals = [VOWELS_MAP.get(x, x) for x in [100, 97, 105, 120]] # [100, 'a', 'i', 120]

# .keys(), .values(), .items() - Trả về view object xem nội dung mà không tốn công copy
print(pizza.keys())    # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
print(pizza.values())  # dict_values(['Margherita', 8.9, 250, ['mozzarella', 'basil']])
print(pizza.items())   # dict_items([('name', 'Margherita'), ...])

# Tính chất Dynamic Reflection của View Objects: tự động cập nhật khi dictionary gốc thay đổi
sample = {'a': 1}
view = sample.keys()
sample['b'] = 2
print("Dynamic View:", view)  # dict_keys(['a', 'b']) - tự phản chiếu mà không cần gọi lại .keys()


# .pop(key, default) - Xóa key và trả về value của key đó
print(pizza.pop('price', 10))  # 8.9

# .popitem() - Xóa và trả về phần tử cuối cùng vừa thêm vào (Python 3.7+)
print(pizza.popitem())         # ('toppings', ['mozzarella', 'basil'])

# .setdefault(key, default) - Trả về value nếu key đã có; nếu chưa có thì thêm key với giá trị default
pizza.setdefault('size', 'Large')
print(pizza.get('size'))  # 'Large'

# Gộp / Cập nhật Dictionary: .update() hoặc toán tử |= (Python 3.9+ PEP 584)
# Cách hiện đại chuẩn Pythonic: dùng toán tử |= thay thế cho .update()
pizza |= {'price': 15, 'total_time': 25}
print("Updated pizza (|=):", pizza)


# .clear() - Xóa sạch toàn bộ phần tử
pizza.clear()
print(pizza)  # {}

# Dictionary Unpacking với toán tử **
# Toán tử ** giải nén dict thành các keyword arguments truyền vào hàm
def sum_three(a: int, b: int, c: int) -> int:
    return a + b + c

nums = {'a': 2, 'b': 4, 'c': 1}
print(sum_three(**nums))  # 7 (tương đương: sum_three(a=2, b=4, c=1))

# Trích xuất & Lọc Keys từ Dictionary:
# - Lấy toàn bộ keys: list(d) hoặc [k for k in d]
# - Lọc keys theo điều kiện value: [k for k, v in d.items() if condition]
constraints = {'has_digits': True, 'has_symbols': False, 'min_length': True}
failed_rules = [key for key, passed in constraints.items() if not passed]
print("Failed rules:", failed_rules)  # ['has_symbols']

# collections.Counter: Chuyên dụng đếm tần suất phần tử ở tầng C (nhanh và tiện hơn dict thông thường)
from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = Counter(data)
print("Counter:", counts)                       # Counter({'apple': 3, 'banana': 2, 'orange': 1})
print("Most common element:", counts.most_common(1)) # [('apple', 3)]
print("Least common element:", counts.most_common()[-1]) # ('orange', 1)


