# Từ điển (Dictionary) là cấu trúc dữ liệu lưu trữ các cặp khóa - giá trị (Key - Value)
# Tương tự từ điển giấy: tra Key để tìm Value tương ứng

# 1. Khai báo dictionary (ví dụ tiếng Anh gốc)
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

# 2. Quy tắc về Key và Value
# - Key phải là duy nhất và bất biến (immutable)
# - Value có thể trùng lặp và nhận bất kỳ kiểu dữ liệu nào

# 3. Truy cập và Cập nhật giá trị
# Truy cập bằng cú pháp ngoặc vuông: dictionary[key]
print(pizza['name'])  # 'Margherita Pizza'

# Cập nhật giá trị (nếu key chưa có thì tự tạo mới)
pizza['name'] = 'Margherita'
print(pizza['name'])  # 'Margherita'

# 4. Các phương thức phổ biến (Methods)
# .get(key, default) - Lấy giá trị an toàn, trả về giá trị mặc định nếu không tìm thấy key
print(pizza.get('toppings', []))  # ['mozzarella', 'basil']
print(pizza.get('discount', 0))   # 0

# .keys(), .values(), .items() - Trả về view object xem nội dung mà không tốn công copy
print(pizza.keys())    # dict_keys(['name', 'price', 'calories_per_slice', 'toppings'])
print(pizza.values())  # dict_values(['Margherita', 8.9, 250, ['mozzarella', 'basil']])
print(pizza.items())   # dict_items([('name', 'Margherita'), ...])

# .pop(key, default) - Xóa key và trả về value của key đó
print(pizza.pop('price', 10))  # 8.9

# .popitem() - Xóa và trả về phần tử cuối cùng vừa thêm vào (Python 3.7+)
print(pizza.popitem())         # ('toppings', ['mozzarella', 'basil'])

# .setdefault(key, default) - Trả về value nếu key đã có; nếu chưa có thì thêm key với giá trị default
pizza.setdefault('size', 'Large')
print(pizza.get('size'))  # 'Large'

# .update() - Cập nhật/gộp dictionary khác vào (ghi đè key trùng và thêm key mới)
pizza.update({'price': 15, 'total_time': 25})
print(pizza)

# .clear() - Xóa sạch toàn bộ phần tử
pizza.clear()
print(pizza)  # {}

# 5. Dictionary Unpacking với toán tử **
# Toán tử ** giải nén dict thành các keyword arguments truyền vào hàm
def sum_three(a, b, c):
    return a + b + c

nums = {'a': 2, 'b': 4, 'c': 1}
print(sum_three(**nums))  # 7 (tương đương: sum_three(a=2, b=4, c=1))

# 6. Trích xuất & Lọc Keys từ Dictionary:
# - Lấy toàn bộ keys: list(d) hoặc [k for k in d]
# - Lọc keys theo điều kiện value: [k for k, v in d.items() if condition]
constraints = {'has_digits': True, 'has_symbols': False, 'min_length': True}
failed_rules = [key for key, passed in constraints.items() if not passed]
print("Failed rules:", failed_rules)  # ['has_symbols']
