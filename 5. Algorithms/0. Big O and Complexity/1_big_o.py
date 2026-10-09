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
    for _ in items:
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

# O(2^n) - Exponential Time: Đệ quy phân nhánh (VD: Bài toán Tháp Hà Nội - Tower of Hanoi)
# Số bước di chuyển tăng gấp đôi mỗi khi n tăng thêm 1 đĩa: T(n) = 2^n - 1 bước
def hanoi_solver(n: int) -> str:
    """
    Giải bài toán Tháp Hà Nội và ghi lại toàn bộ trạng thái của 3 cọc.
    - Time complexity: O(n * 2^n) do mỗi bước chuyển đĩa tốn O(n) để ghi snapshot trạng thái.
      (Nếu chỉ di chuyển đĩa thuần túy: O(2^n) thao tác).
    - Space complexity: O(n * 2^n) để lưu history; độ sâu ngăn xếp đệ quy (Call Stack) là O(n).
    """
    rods: list[list[int]] = [list(range(n, 0, -1)), [], []]
    history: list[str] = []

    def record() -> None:
        history.append(" ".join(str(r) for r in rods))

    def solve(k: int, src: int, dst: int, aux: int) -> None:
        if k > 0:
            solve(k - 1, src, aux, dst)
            rods[dst].append(rods[src].pop())
            record()
            solve(k - 1, aux, dst, src)

    record()
    solve(n, 0, 2, 1)
    return "\n".join(history)

print("O(2^n) Hanoi Solver (n=2):\n" + hanoi_solver(2))

# Tóm tắt các cấp độ Big O (từ nhanh nhất đến chậm nhất):
# - O(1)       : Constant Time (Truy cập phần tử, so sánh cơ bản)
# - O(log n)   : Logarithmic Time (Tăng rất chậm vì loại bỏ 1/2 không gian bài toán sau mỗi bước - VD: Binary Search)
# - O(n)       : Linear Time (1 vòng lặp duyệt mảng tỉ lệ thuận với n)
# - O(n log n) : Log-Linear Time (Thuật toán sắp xếp hiệu quả: Merge Sort, Quick Sort, Timsort)
# - O(n^2)     : Quadratic Time (2 vòng lặp lồng nhau, kém hiệu quả khi n lớn)
# - O(2^n)     : Exponential Time (Đệ quy nhánh - Tower of Hanoi, Fibonacci ngây thơ)
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

