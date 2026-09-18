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
