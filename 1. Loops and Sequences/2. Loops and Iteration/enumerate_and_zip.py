from itertools import zip_longest

# Hàm enumerate(iterable, start=0)
# - Theo dõi index của từng phần tử trong iterable mà không cần tạo biến đếm thủ công.
# - Trả về enumerate object, khi ép sang list() sẽ là danh sách các tuple: (index, value)
languages = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Duyệt trực tiếp bằng vòng lặp for (mặc định start=0):
for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

# Tùy chỉnh giá trị index bắt đầu với tham số start:
for index, language in enumerate(languages, start=1):
    print(f'Index {index} and language {language}')

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

# Cách A (Python 3.10+): strict=True -> Bắt buộc bằng nhau, nếu lệch ném lỗi ValueError
try:
    for name, dev_id in zip(developers, extra_ids, strict=True):
        pass
except ValueError as error:
    print("zip(strict=True) bắt lỗi lệch độ dài:", error)

# Cách B (itertools.zip_longest): Không bỏ sót phần tử thừa, tự điền fillvalue
print("zip_longest:", list(zip_longest(developers, extra_ids, fillvalue='N/A')))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4), ('N/A', 5)]
