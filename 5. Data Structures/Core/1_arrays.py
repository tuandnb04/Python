# 1. Danh sách (Lists) dưới góc độ Cấu trúc Dữ liệu (DSA)
# Trong Python, List là cấu trúc dữ liệu tích hợp sẵn đóng vai trò là một Mảng động (Dynamic Array).
# Các đặc tính quan trọng của List:
# - Có thứ tự (Ordered): Các phần tử duy trì đúng vị trí chỉ mục (index) từ 0 đến len - 1.
# - Có thể thay đổi (Mutable): Cho phép thêm, sửa, xóa phần tử linh hoạt sau khi khởi tạo.
# - Chứa kiểu dữ liệu hỗn hợp (Heterogeneous): Có thể lưu trữ các phần tử thuộc nhiều kiểu dữ liệu khác nhau.
# - Phục vụ nền tảng cho nhiều cấu trúc dữ liệu và thuật toán trong DSA.

# 1.1. Khởi tạo danh sách (Creating Lists):
empty_list = []  # Danh sách rỗng
initial_values = [1, 2, 3, 4, 5]  # Danh sách có giá trị ban đầu
mixed_types = [1, "hello", 3.14, True]  # Danh sách chứa nhiều kiểu dữ liệu

print("Empty list:        ", empty_list)
print("Initial values list:", initial_values)
print("Mixed types list:   ", mixed_types)

# 2. Thuật toán tích hợp sẵn qua các phương thức của List (List Methods / Built-in Algorithms)
# Python List đi kèm các thuật toán dựng sẵn ở tầng C để thực hiện các thao tác thường gặp:
x = [9, 12, 7, 4, 11]
print("\nOriginal list x:    ", x)

# Thêm phần tử vào cuối mảng (.append): O(1) amortized
x.append(8)
print("After append(8):    ", x)

# Sắp xếp danh sách theo thứ tự tăng dần (.sort): Timsort O(n log n)
x.sort()
print("After sort():       ", x)  # [4, 7, 8, 9, 11, 12]

# 3. Tự xây dựng thuật toán (Create Custom Algorithms)
# Khi cần giải quyết những bài toán đặc thù mà ngôn ngữ không có sẵn hàm, ta tự thiết kế thuật toán.
# Ví dụ: Thuật toán tìm giá trị nhỏ nhất (Lowest Value) trong mảng:
my_array = [7, 12, 9, 4, 11, 8]
min_val = my_array[0]  # Giả định phần tử đầu tiên là nhỏ nhất

for item in my_array:
    if item < min_val:
        min_val = item

print("\nCustom Algorithm - Finding lowest value:")
print("Array:       ", my_array)
print("Lowest value:", min_val)  # 4

# 4. Phân tích độ phức tạp thời gian & Tối ưu hóa (Time Complexity & Optimization)
# - Khái niệm: Độ phức tạp thời gian đo lường sự thay đổi của thời gian chạy khi kích thước dữ liệu (n) tăng lên.
# - Phân tích thuật toán tìm giá trị nhỏ nhất ở trên:
#   + Vòng lặp phải duyệt qua từng phần tử đúng 1 lần để so sánh với min_val.
#   + Mảng có 6 phần tử -> vòng lặp chạy 6 lần.
#   + Nếu mảng có 1,000 phần tử -> vòng lặp chạy 1,000 lần.
#   -> Thời gian chạy tỉ lệ thuận trực tiếp với kích thước dữ liệu n.
#   -> Độ phức tạp là O(n) - Tuyến tính (Linear Time).
# - Vai trò của Tối ưu hóa (Optimization):
#   Thuật toán đơn giản chạy rất nhanh trên tập dữ liệu nhỏ (n < 100), nhưng khi dữ liệu lớn
#   (hàng triệu phần tử), sự khác biệt giữa O(n), O(n log n) và O(n^2) quyết định chương trình
#   chạy trong vài phần trăm giây hay chạy mất nhiều giờ.

# 5. Cơ chế bên dưới: Static Array vs Dynamic Array
# - Static Array (Mảng tĩnh): Kích thước cố định (fixed size), cấp phát vùng nhớ liền kề (contiguous).
#   Truy cập O(1) qua công thức địa chỉ ô nhớ: Address = Base_Address + Index * Element_Size.
# - Dynamic Array (Mảng động - Bản chất của Python List):
#   Khi mảng đầy, Python tự động cấp phát vùng nhớ mới lớn hơn (thường gấp đôi - Doubling Strategy)
#   và sao chép toàn bộ phần tử cũ sang vùng nhớ mới.

numbers = [3, 4, 5, 6]

# Truy cập & Cập nhật theo index: O(1) - Constant Time
print("\nAccess index 0 (O(1)):", numbers[0])  # 3
numbers[2] = 16                               # Cập nhật O(1)

# Thêm vào cuối (.append): O(1) amortized
numbers.append(7)

# Chèn vào giữa (.insert): O(n) vì phải dịch chuyển toàn bộ phần tử phía sau sang phải 1 bước
numbers.insert(2, 99)

# Xóa phần tử (.pop):
# - Xóa cuối: O(1) vì không phải dịch chuyển phần tử nào
# - Xóa đầu/giữa: O(n) vì phải dồn các phần tử phía sau sang trái
last_val = numbers.pop()  # O(1) - Xóa phần tử cuối (7)
mid_val = numbers.pop(2)  # O(n) - Xóa phần tử tại index 2 (99)

print("Final array numbers: ", numbers)  # [3, 4, 16, 6]

