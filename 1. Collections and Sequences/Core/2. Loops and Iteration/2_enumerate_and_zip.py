from itertools import zip_longest

# Hàm enumerate(iterable, start=0)
# - Theo dõi index của từng phần tử trong iterable mà không cần tạo biến đếm thủ công.
# - Trả về enumerate object, khi ép sang list() sẽ là danh sách các tuple: (index, value)
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# 1. Duyệt cơ bản (mặc định start=0):
for index, language in enumerate(languages):
    print(f"Index {index}: {language}")

# 2. Đánh số thứ tự hiển thị người dùng (tùy biến start=1):
for rank, language in enumerate(languages, start=1):
    print(f"Top {rank}: {language}")

# 3. Ứng dụng thực tế: Tìm vị trí của phần tử đầu tiên thỏa mãn điều kiện
target_lang = "Russian"
for index, language in enumerate(languages):
    if language == target_lang:
        print(f"Found '{target_lang}' at index {index}")
        break

# Hàm zip(*iterables) - Ghép song song nhiều iterables
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

zipped = list(zip(developers, ids))
print("zipped:", zipped)
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# Duyệt song song qua zip() với vòng lặp for:
for name, dev_id in zip(developers, ids):
    print(f'Name: {name}, ID: {dev_id}')

# Kỹ thuật Unzip (Tách ngược lại các list ban đầu từ danh sách cặp tuple)
# Sử dụng toán tử giải nén (*) kết hợp với zip:
names_unzipped, ids_unzipped = zip(*zipped)
print("Unzipped names:", list(names_unzipped))
print("Unzipped ids:", list(ids_unzipped))

# Xử lý khi các iterable lệch độ dài:
extra_ids = [1, 2, 3, 4, 5]

# Mặc định: zip() tự động dừng lại ở iterable ngắn nhất (bỏ qua phần tử thừa)
print("Default zip (stops at shortest):", list(zip(developers, extra_ids)))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# Python 3.10+: strict=True đảm bảo các iterable bắt buộc phải có cùng độ dài (báo lỗi nếu lệch)
print("Strict zip (equal lengths):", list(zip(developers, ids, strict=True)))

# itertools.zip_longest: Không bỏ sót phần tử thừa, tự điền fillvalue
print("zip_longest:", list(zip_longest(developers, extra_ids, fillvalue='N/A')))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4), ('N/A', 5)]

