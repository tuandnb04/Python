import itertools

# 1. Khái niệm Iterable vs Iterator
# - Iterable: Đối tượng có thể duyệt qua (list, str, tuple, dict...)
# - Iterator: Con trỏ duyệt từng phần tử một qua hàm next()
numbers = [10, 20, 30]
iterator = iter(numbers)
print("Iterator next():", next(iterator))  # 10
print("Iterator next():", next(iterator))  # 20

# 2. Generator Function với từ khóa 'yield'
# - Không gom toàn bộ dữ liệu vào RAM mà sinh từng giá trị khi có yêu cầu
def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count                        # Tạm dừng hàm và trả về giá trị
        count += 1

gen = count_up_to(3)
for val in gen:
    print("Generated value:", val)         # 1, 2, 3

# 3. Generator Expression (Dùng ngoặc tròn, tương tự List Comprehension nhưng là Generator)
squares_gen = (x ** 2 for x in range(1, 4))
print("Generator expression as list:", list(squares_gen)) # [1, 4, 9]

# 4. [TÍNH NĂNG PYTHON 3.12+ PEP 654]: itertools.batched
# Tự động chia luồng dữ liệu thành từng lô (batch) n phần tử ở cấp độ C
code_files = [f"src/flask/file_{i}.py" for i in range(1, 11)]

print("--- Batch Processing with itertools.batched ---")
for batch_no, batch in enumerate(itertools.batched(code_files, 3), start=1):
    print(f"Batch {batch_no} ({len(batch)} files): {batch}")
