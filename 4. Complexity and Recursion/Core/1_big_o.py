# 1. Tổng quan Thuật toán (Algorithms) & Ký hiệu Big O (Big O Notation)
# - Thuật toán (Algorithm): Chuỗi chỉ dẫn hữu hạn, rõ ràng để giải quyết bài toán (Input -> Các bước -> Output).
#   Tiêu chí cốt lõi: Tính đúng đắn (Correctness) và Tính hiệu quả (Efficiency: tiết kiệm Time & Space khi n lớn).
# - Ký hiệu Big O: Đo hiệu năng trường hợp xấu nhất (Worst-Case) dựa trên số phép toán khi kích thước n tăng lên.
#   Quy tắc Dominant Term (Bỏ hằng số và hệ số nhân, giữ bậc cao nhất):
#     + 7n + 20          -> O(n) (bỏ hằng số 20 và hệ số 7)
#     + 20n^2 + 15n + 7  -> O(n^2) (hạng tử n^2 chi phối khi n rất lớn)

# 2. Độ phức tạp thời gian (Time Complexity)

# 2.1. O(1) - Constant Time (Thời gian không đổi):
# Số phép toán độc lập hoàn toàn với kích thước dữ liệu n:
def check_even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"

print("O(1) Constant Time:", check_even_or_odd(42))

# 2.2. O(n) - Linear Time (Thời gian tuyến tính):
# Thời gian chạy tăng tỉ lệ thuận với kích thước n.
# Ví dụ: Thuật toán tìm giá trị nhỏ nhất (Lowest value) trong mảng.
# Vòng lặp phải duyệt qua n phần tử đúng 1 lần: n = 6 chạy 6 lần, n = 1000 chạy 1000 lần.
def find_lowest_value(items: list[int]) -> int:
    min_val = items[0]
    for item in items:
        if item < min_val:
            min_val = item
    return min_val

print("O(n) Lowest value: ", find_lowest_value([7, 12, 9, 4, 11, 8]))  # 4

# 2.3. O(n^2) - Quadratic Time (Thời gian bậc hai):
# Xuất hiện khi có 2 vòng lặp lồng nhau duyệt qua dữ liệu:
def count_pairs(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

print("O(n^2) for n=3:    ", count_pairs(3))  # 9 operations

# 2.4. O(2^n) - Exponential Time (Thời gian hàm mũ):
# Số phép toán tăng gấp đôi mỗi khi n tăng thêm 1 đơn vị.
# Ví dụ: Thuật toán Fibonacci đệ quy ngây thơ (Naive Recursion):
def fibonacci_naive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

print("O(2^n) Fibonacci:   ", fibonacci_naive(6))  # 8

# 3. Bảng tóm tắt các cấp độ Big O (từ nhanh nhất đến chậm nhất)
# - O(1)       : Constant Time (Truy cập phần tử, so sánh cơ bản)
# - O(log n)   : Logarithmic Time (Tăng rất chậm vì loại bỏ 1/2 không gian bài toán mỗi bước - VD: Binary Search)
# - O(n)       : Linear Time (Duyệt mảng 1 lần, tìm kiếm tuyến tính)
# - O(n log n) : Log-Linear Time (Các thuật toán sắp xếp tối ưu: Merge Sort, Quick Sort, Timsort)
# - O(n^2)     : Quadratic Time (2 vòng lặp lồng nhau, kém hiệu quả khi n lớn)
# - O(2^n)     : Exponential Time (Đệ quy phân nhánh nhị phân, giải pháp vét cạn)
# - O(n!)      : Factorial Time (Sinh hoán vị, không khả thi khi n lớn)

# 4. Trực quan hóa đồ thị độ phức tạp (Complexity Graph Intuition)
# - Trục hoành (X-axis): Kích thước đầu vào (Input Size - n).
# - Trục tung (Y-axis): Thời gian thực thi / Số phép toán (Running Time / Operations).
# - O(1) là đường nằm ngang phẳng; O(log n) và O(n) tăng từ từ;
#   trong khi O(n^2), O(2^n), O(n!) bùng nổ theo phương thẳng đứng khi n tăng.

# 5. Độ phức tạp không gian (Space Complexity)
# Đo lường lượng bộ nhớ bổ sung (memory) mà thuật toán cần sử dụng khi n tăng lên:
# - O(1) Space (Constant): Chỉ dùng vài biến tạm độc lập với kích thước n (VD: biến đếm, min_val).
# - O(n) Space (Linear): Cần cấp phát bộ nhớ phụ tỉ lệ thuận với n (VD: tạo bản sao danh sách n phần tử).
# - O(n^2) Space (Quadratic): Cần cấp phát bảng/ma trận 2 chiều kích thước n x n.
