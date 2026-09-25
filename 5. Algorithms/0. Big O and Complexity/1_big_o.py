# KHÁI NIỆM VỀ THUẬT TOÁN VÀ ĐỘ PHỨC TẠP BIG O:
# 1. Thuật toán (Algorithm):
#    - Tập hợp các chỉ dẫn rõ ràng, hữu hạn để giải quyết một bài toán hoặc thực hiện một nhiệm vụ.
#    - Ẩn dụ "Công thức nấu ăn" (Recipe):
#      + Nguyên liệu = Input (dữ liệu đầu vào).
#      + Các bước nấu = Thuật toán (chỉ thị từng bước máy tính cần làm).
#      + Món ăn = Output (kết quả đầu ra).
#    - Các đặc tính cốt lõi (Key Characteristics):
#      + Tính hữu hạn (Finiteness): Phải dừng lại sau một số bước hữu hạn, không chạy vô tận.
#      + Tính xác định (Unambiguous / Definiteness): Mỗi bước phải rõ ràng, chính xác, không mập mờ.
#      + Đầu vào & Đầu ra (Input/Output): Có 0 hoặc nhiều input; tạo ra 1 hoặc nhiều output hợp lệ.
#      + Độc lập ngôn ngữ: Bản chất thuật toán không phụ thuộc ngôn ngữ nào, cần cài đặt cụ thể qua Python, C++, v.v. để chạy.
#
# 2. Big O Notation:
#    - Đo lường hiệu năng trường hợp xấu nhất (Worst-Case) và tốc độ tăng trưởng (Growth Rate)
#      khi kích thước đầu vào (n) tăng dần lên vô cùng.
#    - Quy tắc bỏ hằng số và bậc thấp (Dominant Term):
#      + Bỏ hằng số: 7n + 20 -> O(n) (vì 20 không đáng kể khi n rất lớn).
#      + Giữ bậc cao nhất: 20n^2 + 15n + 7 -> O(n^2) (hạng tử n^2 chi phối toàn bộ hành vi).

# I. ĐỘ PHỨC TẠP THỜI GIAN (TIME COMPLEXITY)

# O(1) - Constant Time: Thời gian thực thi không đổi dù n tăng
def check_even_or_odd(number):
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
# - O(log n)   : Logarithmic Time (Binary Search - chia đôi không gian tìm kiếm)
# - O(n)       : Linear Time (1 vòng lặp duyệt mảng)
# - O(n log n) : Log-Linear Time (Merge Sort, Quick Sort)
# - O(n^2)     : Quadratic Time (2 vòng lặp lồng nhau)
# - O(2^n)     : Exponential Time (Đệ quy nhánh - Fibonacci ngây thơ)
# - O(n!)      : Factorial Time (Sinh hoán vị)


# II. ĐỘ PHỨC TẠP KHÔNG GIAN (SPACE COMPLEXITY)
# Đo lường lượng bộ nhớ bổ sung (memory) mà thuật toán cần sử dụng khi n tăng lên:
# - O(1) Space (Constant): Chỉ dùng vài biến tạm độc lập với kích thước n (VD: biến đếm, cờ hiệu).
# - O(n) Space (Linear): Cần cấp phát bộ nhớ phụ tỉ lệ thuận với n (VD: tạo bản sao list, list comprehension).
# - O(n^2) Space (Quadratic): Cần cấp phát bảng/ma trận 2 chiều kích thước n x n (VD: bảng quy hoạch động 2D).
