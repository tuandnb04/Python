import sys
from array import array

# 1. So sánh bộ nhớ: Python List vs array.array
# - list: mảng động chứa con trỏ tới các đối tượng, tốn nhiều RAM lưu metadata.
# - array.array: mảng đồng nhất kiểu ở tầng C, lưu trữ trực tiếp dữ liệu nhị phân.
sample_size = 1000
py_list = list(range(sample_size))
c_array = array('i', range(sample_size))

print(f"List memory ({sample_size} ints): {sys.getsizeof(py_list)} bytes")
print(f"array.array memory ({sample_size} ints): {sys.getsizeof(c_array)} bytes")

# 2. Thao tác trên mảng động (Python List):
numbers = [10, 20, 30, 40, 50]

# Truy cập và cập nhật theo chỉ mục: O(1)
val = numbers[2]
numbers[2] = 99
print(f"Access O(1): {val} | Update O(1): {numbers}")

# Thêm vào cuối: O(1) amortized
numbers.append(60)
print("Append O(1):", numbers)

# Chèn vào đầu/giữa: O(n) do phải dịch chuyển các phần tử phía sau
numbers.insert(1, 15)
print("Insert at index 1 O(n):", numbers)

# Xóa phần tử cuối: O(1) vs Xóa đầu/giữa: O(n)
last_item = numbers.pop()
first_item = numbers.pop(0)
print(f"Pop last O(1): {last_item} | Pop first O(n): {first_item}")
print("Remaining numbers:", numbers)

# 3. Bộ đệm nhị phân khả biến (bytearray):
# Lưu dãy byte thô liền kề ở tầng C, cho phép sửa đổi trực tiếp tại chỗ (in-place)
buffer = bytearray(b"Hello World")
buffer[0] = ord("J")  # Thay 'H' thành 'J' tại chỗ
buffer[:5] = b"Peace" # Ghi đè lát cắt
print("Mutated bytearray:", buffer)
print("Length of buffer:", len(buffer))
