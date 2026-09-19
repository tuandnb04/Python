import itertools
from collections import deque

# Khái niệm Iterable vs Iterator & Giao thức lặp (Iteration Protocol)
# Iterable cung cấp __iter__(), Iterator duyệt qua từng phần tử bằng next() / __next__()
numbers = [10, 20, 30]
iterator = iter(numbers)
print("Iterator next():", next(iterator))  # 10
print("Iterator next():", next(iterator))  # 20

# Tự tạo Custom Iterator bằng __iter__() và __next__()
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("Custom Countdown iterator:", list(Countdown(3)))  # [3, 2, 1]

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
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)       # Ủy quyền cho generator đệ quy
        else:
            yield item

nested_data = [1, [2, [3, 4]], 5]
print("Flatten nested list:", list(flatten(nested_data)))  # [1, 2, 3, 4, 5]

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
