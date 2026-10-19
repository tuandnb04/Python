import itertools

# 1. enumerate(): Duyệt kèm chỉ mục (index)
languages = ["Python", "JavaScript", "Go", "Rust"]
for index, lang in enumerate(languages, start=1):
    print(f"Top {index}: {lang}")

# 2. zip(): Ghép song song nhiều iterable
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Giải nén (unzip) bằng toán tử *:
zipped = list(zip(names, scores))
unzipped_names, unzipped_scores = zip(*zipped)
print("Unzipped names:", list(unzipped_names))

# 3. Iterator: iter() tạo iterator, next() lấy từng phần tử
numbers = [10, 20, 30]
iterator = iter(numbers)
print("First next():", next(iterator))
print("Second next():", next(iterator))

# 4. Generator function (yield): sinh dữ liệu lười, tiết kiệm bộ nhớ
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print("Countdown:", list(countdown(3)))

# yield from: ủy quyền duyệt cho generator con hoặc iterable
def combined():
    yield from countdown(2)
    yield from ["Go!"]

print("Combined:", list(combined()))

# 5. itertools hữu dụng:
# chain: nối nhiều iterable không tốn RAM tạo list mới
chained = list(itertools.chain([1, 2], [3, 4]))
print("itertools.chain:", chained)

# islice: cắt lát trực tiếp trên luồng lặp
count_stream = itertools.count(start=1)  # Vô hạn
first_three = list(itertools.islice(count_stream, 3))
print("itertools.islice:", first_three)

# batched (Python 3.12+): chia luồng dữ liệu thành từng lô
items = ["a", "b", "c", "d", "e"]
batches = list(itertools.batched(items, 2))
print("itertools.batched:", batches)
