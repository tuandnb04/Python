# 1. Khái niệm bytearray & Bộ đệm C liên tục (Contiguous C Buffer)
# Khác biệt cơ bản giữa Python List thông thường và bytearray:
# - Python list: Là một mảng động chứa các con trỏ (pointers), mỗi con trỏ trỏ tới một PyObject
#   riêng lẻ nằm rải rác trên vùng nhớ Heap (tiêu tốn ~28 bytes cho mỗi số nguyên nhỏ).
# - bytearray: Là cấu trúc dữ liệu lưu trữ trực tiếp dãy các byte thô (giá trị từ 0 đến 255)
#   trong một khối bộ nhớ liền kề (Contiguous Memory) ở tầng ngôn ngữ C.
#   -> Tối ưu hóa tuyệt đối bộ nhớ RAM và tận dụng tối đa CPU Cache Locality.

# Khởi tạo bytearray từ bytes chuỗi:
raw_buffer = bytearray(b"Hello World")
print("Initial bytearray:  ", raw_buffer)
print("Length of buffer:   ", len(raw_buffer))  # 11 bytes

# 2. Tính chất Mutable (Có thể thay đổi tại chỗ - In-place)
# Không giống như kiểu 'bytes' vốn là bất biến (immutable), bytearray cho phép sửa đổi trực tiếp:
raw_buffer[0] = ord('J')  # Thay ký tự 'H' (72) thành 'J' (74)
print("Mutated bytearray:  ", raw_buffer)  # Jello World

# 3. Hoán vị phần tử tại chỗ (In-place Swap) không tốn bộ nhớ phụ:
# Ví dụ: sửa lỗi thứ tự chữ số b"1243" thành b"1234"
b = bytearray(b"1243")
print("\nBefore swap:        ", b)

# Đổi chỗ byte tại index 2 ('4') và index 3 ('3') trực tiếp trên RAM C:
b[2], b[3] = b[3], b[2]
print("After swap:         ", b)  # bytearray(b'1234')

# 4. Ép kiểu trực tiếp (Direct Parsing) sang số nguyên:
# Chuyển đổi trực tiếp từ buffer số mà không cần thông qua bước trung gian chuỗi str:
parsed_int = int(b)
print("Parse directly to int:", parsed_int)  # 1234

# 5. Cắt lát và Ghi đè bộ nhớ (Slice Assignment O(k)):
# Thay thế một đoạn byte trực tiếp bằng memcpy ở tầng C:
data = bytearray(b"IMAGE_HEADER_DATA")
data[:5] = b"FRAME"
print("\nReplaced header:    ", data)  # FRAME_HEADER_DATA
