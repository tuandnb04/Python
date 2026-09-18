# Các kiểu dữ liệu phổ biến trong Python (Dynamically-typed)

# 1. Số, Chuỗi, Boolean & None
num_int = 10                       # int (Số nguyên)
num_float = 4.5                    # float (Số thực)
text = 'hello'                     # str (Chuỗi)
is_valid = True                    # bool (True / False)
empty_val = None                   # NoneType (Không có giá trị)

# 2. Tập hợp (Collections) & Trình tự (Sequences)
items_list = [22, 'hello', True]   # list (Có thứ tự, mutable)
items_tuple = (7, 'hello', 8.5)    # tuple (Có thứ tự, immutable)
items_set = {7, 'hello', 8.5}      # set (Tập hợp không trùng lặp)
user_dict = {'name': 'Alice', 'age': 25} # dict (Cặp key-value)
num_range = range(5)               # range (Dãy số 0 -> 4)

print(num_int, num_float, text, is_valid, empty_val)
print(items_list, items_tuple, items_set, user_dict, list(num_range))