# TỔNG QUAN THUẬT TOÁN & BIG O NOTATION:
# 1. Thuật toán (Algorithm): Chỉ dẫn hữu hạn, rõ ràng để giải bài toán (như công thức nấu ăn: Input -> Các bước -> Output).
#    - Tiêu chí cốt lõi: Tính đúng đắn (Correctness) và Tính hiệu quả (Efficiency: tiết kiệm Time & Space để scale khi n lớn).
# 2. Big O Notation: Đo hiệu năng trường hợp xấu nhất (Worst-Case) dựa trên số phép toán khi kích thước n tăng lên vô cùng.
#    - Quy tắc Dominant Term (Bỏ hằng số, giữ bậc cao nhất):
#      + 7n + 20 -> O(n) (bỏ hằng số và hệ số nhân)
#      + 20n^2 + 15n + 7 -> O(n^2) (hạng tử n^2 chi phối khi n rất lớn)

# I. ĐỘ PHỨC TẠP THỜI GIAN (TIME COMPLEXITY)

# O(1) - Constant Time: Thời gian thực thi không đổi dù n tăng
def check_even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"

print("O(1) Check:", check_even_or_odd(42))

# O(n) - Linear Time: Thời gian tăng tuyến tính tỉ lệ thuận với kích thước n
def print_elements(items):
    for item in items:
        pass  # Duyệt qua từng phần tử trong danh sách n phần tử

print_elements([1, 2, 3, 4, 5])

# O(n^2) - Quadratic Time: 2 vòng lặp lồng nhau (Nested loops)
def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

print("O(n^2) operations for n=3:", count_pairs(3)) # 9 operations

# Tóm tắt các cấp độ Big O (từ nhanh nhất đến chậm nhất):
# - O(1)       : Constant Time (Truy cập phần tử, so sánh cơ bản)
# - O(log n)   : Logarithmic Time (Tăng rất chậm vì loại bỏ 1/2 không gian bài toán sau mỗi bước - VD: Binary Search)
# - O(n)       : Linear Time (1 vòng lặp duyệt mảng tỉ lệ thuận với n)
# - O(n log n) : Log-Linear Time (Thuật toán sắp xếp hiệu quả: Merge Sort, Quick Sort, Timsort)
# - O(n^2)     : Quadratic Time (2 vòng lặp lồng nhau, kém hiệu quả khi n lớn)
# - O(2^n)     : Exponential Time (Đệ quy nhánh - Fibonacci ngây thơ)
# - O(n!)      : Factorial Time (Sinh hoán vị, không khả thi trong thực tế khi n lớn)
#
# SO SÁNH TRỰC QUAN TRÊN ĐỒ THỊ (COMPLEXITY GRAPH):
# - Trục hoành (X-axis): Kích thước đầu vào (Input Size - n).
# - Trục tung (Y-axis): Thời gian thực thi / Số phép toán (Running Time / Operations).
# - O(1) là đường nằm ngang phẳng; O(log n) và O(n) tăng từ từ; còn O(n^2), O(2^n), O(n!) bùng nổ rất nhanh theo phương thẳng đứng.


# II. ĐỘ PHỨC TẠP KHÔNG GIAN (SPACE COMPLEXITY)
# Đo lường lượng bộ nhớ bổ sung (memory) mà thuật toán cần sử dụng khi n tăng lên:
# - O(1) Space (Constant): Chỉ dùng vài biến tạm độc lập với kích thước n (VD: biến đếm, cờ hiệu).
# - O(n) Space (Linear): Cần cấp phát bộ nhớ phụ tỉ lệ thuận với n (VD: tạo bản sao danh sách n phần tử).
# - O(n^2) Space (Quadratic): Cần cấp phát bảng/ma trận 2 chiều kích thước n x n (VD: lưu trữ ma trận tất cả các cặp).

