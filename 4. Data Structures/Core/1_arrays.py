# Khái niệm Static Array vs Dynamic Array:
# - Static Array: Kích thước cố định (fixed size). Truy cập O(1). Khi đầy phải tạo mảng mới và copy sang.
# - Dynamic Array: Tự động co giãn (resize) trong runtime. Trong Python, kiểu 'list' là Dynamic Array.

# Các thao tác và độ phức tạp trên Dynamic Array (Python list):
numbers = [3, 4, 5, 6]

# Truy cập & Cập nhật theo index: O(1) - Constant Time
print("Access index 0 (O(1)):", numbers[0])    # 3
numbers[2] = 16                                # O(1)

# Thêm vào cuối (.append): O(1) amortized (O(n) khi mảng đầy cần cấp phát lại)
numbers.append(7)

# Chèn vào giữa (.insert): O(n) vì phải dịch chuyển các phần tử phía sau
numbers.insert(2, 99)

# Xóa phần tử (.pop): O(1) nếu xóa cuối, O(n) nếu xóa ở giữa/đầu
last_val = numbers.pop()                       # O(1) - Xóa phần tử cuối (7)
mid_val = numbers.pop(2)                       # O(n) - Xóa phần tử tại index 2 (99)

print("Final array:", numbers)                 # [3, 4, 16, 6]

# bytearray: Mảng Byte liên tục ở tầng C (Contiguous C Buffer)
# - Khác biệt với list: list là mảng các con trỏ trỏ đến PyObject (tốn ~28 bytes/số nguyên, phân tán bộ nhớ).
# - bytearray lưu trữ trực tiếp các byte nhị phân 0-255 trong vùng nhớ liên tục (tối ưu CPU Cache Locality).
# - Hỗ trợ Mutable (đổi chỗ, gán cắt lát tại chỗ memcpy O(k)) và parse trực tiếp sang số nguyên qua int(b):
b = bytearray(b"1243")
# Hoán vị: b[2] (byte '4') và b[3] (byte '3') đổi chỗ cho nhau
b[2], b[3] = b[3], b[2]           # Đổi chỗ tại chỗ 2 byte trực tiếp trên RAM C
print("bytearray:", b)            # bytearray(b'1234')
print("Parse to int:", int(b))    # 1234 (parse trực tiếp từ buffer mà không cần qua str)


