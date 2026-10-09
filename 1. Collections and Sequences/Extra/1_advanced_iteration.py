import itertools
from collections import deque

# Khái niệm Iterable vs Iterator:
# - Iterable là đối tượng chứa dữ liệu có thể lặp (List, Tuple, Dict, Set, chuỗi...).
# - Iterator là luồng duyệt qua dữ liệu, dùng iter() để tạo và next() để lấy từng phần tử kế tiếp.
numbers = [10, 20, 30]
iterator = iter(numbers)
print("Iterator next():", next(iterator))  # 10
print("Iterator next():", next(iterator))  # 20

# Tự tạo luồng lặp Iterator bằng hàm Generator (yield)
def countdown(start: int):
    current = start
    while current > 0:
        yield current
        current -= 1

print("Custom Countdown iterator:", list(countdown(3)))  # [3, 2, 1]

# Generator Function (yield) & Ủy quyền lặp (yield from)
def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count                        # Tạm dừng hàm và trả về giá trị
        count += 1

gen = count_up_to(3)
for val in gen:
    print("Generated value:", val)         # 1, 2, 3

# Kỹ thuật yield from: Ủy quyền duyệt cho generator con (Làm phẳng cấu trúc lồng nhau)
# Chuẩn Pythonic (Duck Typing): Nhận mọi Iterable (list, tuple, set...), ngoại trừ chuỗi str/bytes
from collections.abc import Iterable

def flatten(nested_iterable):
    for item in nested_iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)       # Ủy quyền cho generator đệ quy
        else:
            yield item

nested_data = [1, (2, [3, {4}]), 5, "hello"]
print("Flatten nested iterable (Duck Typing):", list(flatten(nested_data)))  # [1, 2, 3, 4, 5, 'hello']


# Generator Expression (tương tự List Comprehension nhưng sinh lười, tiết kiệm RAM)
squares_gen = (x ** 2 for x in range(1, 4))
print("Generator expression as list:", list(squares_gen))  # [1, 4, 9]

# itertools nâng cao
# chain: Nối luồng lặp liên tiếp không cần tạo list mới
list_a = [1, 2]
list_b = [3, 4]
chained = list(itertools.chain(list_a, list_b, (5, 6)))
print("itertools.chain():", chained)       # [1, 2, 3, 4, 5, 6]

# islice: Cắt lát trực tiếp trên Iterator / Stream mà không cần ép sang list
stream = count_up_to(1_000_000)
first_three = list(itertools.islice(stream, 3))
print("itertools.islice():", first_three)   # [1, 2, 3]

# batched (Python 3.12+): Chia luồng dữ liệu thành từng lô n phần tử
code_files = [f"src/flask/file_{i}.py" for i in range(1, 8)]
for batch_no, batch in enumerate(itertools.batched(code_files, 3), start=1):
    print(f"Batch {batch_no}: {batch}")

# collections.deque(maxlen=N): Cửa sổ trượt (Sliding Window O(1))
# Tự động đẩy phần tử cũ ra khi vượt quá maxlen
recent_logs = deque(maxlen=3)
for i in range(1, 6):
    recent_logs.append(f"Action_{i}")
print("deque sliding window:", list(recent_logs)) # ['Action_3', 'Action_4', 'Action_5']
