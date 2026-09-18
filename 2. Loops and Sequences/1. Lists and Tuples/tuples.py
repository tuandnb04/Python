# Tuple là kiểu dữ liệu tuần tự có thứ tự và BẤT BIẾN (không thể sửa sau khi tạo)

# 1. Khởi tạo Tuple & Type Hints (Chuẩn Python 3.9+)
developer: tuple[object, ...] = ('Alice', 34, 'Rust Developer')    # Tập hợp kiểu dữ liệu trong tuple
numbers: tuple[int, ...] = (1, 2, 3, 4, 5)                         # Độ dài tùy biến (...)
single_item = (1,)                                                 # BẮT BUỘC có dấu phẩy ở cuối
coords = 10, 20                                                    # Packing (không cần ngoặc đơn)
chars = tuple('Jessica')                                           # ('J', 'e', 's', 's', 'i', 'c', 'a')

# 2. Truy cập phần tử (Indexing) và Cắt lát (Slicing)
print(developer[1])                          # 34 (chỉ số dương)
print(numbers[-2])                           # 4 (chỉ số âm, từ cuối lên)
print(numbers[1:3])                          # (2, 3) lấy từ vị trí 1 đến trước 3
# numbers[7]                                 # Lỗi IndexError: tuple index out of range

# 3. Tính bất biến (Immutable): Không thể sửa hoặc xóa phần tử
# developer[0] = 'Bob'                       # Lỗi TypeError: không cho phép gán lại
# del developer[1]                           # Lỗi TypeError: không cho phép xóa

# 4. Kiểm tra phần tử tồn tại (in)
print('Alice' in developer)                  # True
candidate: object = input('Enter candidate name: ')
print(candidate in developer)                # False if name not in tuple

# 5. Mở gói Tuple (Unpacking)
name, age, job = developer                   # Gán từng phần tử vào các biến
print(name, age, job)                        # Alice 34 Rust Developer

first, *rest = numbers                       # Dùng * để gom các phần tử còn lại thành list
print(first, rest)                           # 1 [2, 3, 4, 5]

a, b = 10, 20
a, b = b, a                                  # Hoán đổi biến không cần biến tạm
print(a, b)                                  # 20 10

# 6. Khớp mẫu với Tuple (Pattern Matching - Python 3.10+)
point = (0, 5)
match point:
    case (0, y):
        print(f"Y-axis at {y}")              # Y-axis at 5 (nằm trên trục Y)

# 7. Các phương thức của Tuple: count() và index()
fruits = ('apple', 'banana', 'apple', 'cherry', 'banana')
print(fruits.count('apple'))                 # 2 (đếm số lần xuất hiện)
print(fruits.count('orange'))                # 0 (trả về 0 nếu không tìm thấy)
print(fruits.index('banana'))                # 1 (tìm vị trí đầu tiên)
print(fruits.index('banana', 2))             # 4 (bắt đầu tìm từ vị trí index 2)
# fruits.index('orange')                     # Lỗi ValueError: x not in tuple

# 8. Hàm toàn cục sorted() (luôn trả về một list mới, không đổi tuple gốc)
print(sorted(fruits))                        # Sắp xếp tăng dần A-Z (trả về list)
print(sorted(fruits, key=len))               # Sắp xếp theo độ dài từ ngắn đến dài
print(sorted(fruits, reverse=True))          # Sắp xếp đảo ngược Z-A

# 9. Phép toán với Tuple: Ghép (+) và Nhân bản (*)
print((1, 2) + (3, 4))                       # (1, 2, 3, 4) tạo tuple mới
print(('a', 'b') * 2)                        # ('a', 'b', 'a', 'b')
