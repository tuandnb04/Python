# LÝ THUYẾT CỐT LÕI VỀ DYNAMIC PROGRAMMING (DP - QUY HOẠCH ĐỘNG)
#
# 1. Hai điều kiện tiên quyết để áp dụng Quy hoạch động:
#    - Overlapping Subproblems (Bài toán con gối nhau / trùng lặp): Các bài toán con
#      bị gọi lại nhiều lần trong quá trình giải. (Nếu các bài toán con độc lập,
#      dùng Chia để trị - Divide and Conquer, không dùng DP).
#    - Optimal Substructure (Cấu trúc con tối ưu): Lời giải tối ưu của bài toán lớn
#      được tổng hợp từ lời giải tối ưu của các bài toán con nhỏ hơn.
#
# 2. Bản chất chuyển đổi độ phức tạp & Đánh đổi (Trade-off):
#    - Giảm độ phức tạp thời gian từ hàm mũ (Exponential - O(2^n)) xuống đa thức (Polynomial - O(n)).
#    - Trade-off: Đánh đổi thêm bộ nhớ RAM (Space) để lưu kết quả trung gian, đổi lấy tốc độ (Time).
#
# 3. Hai phương pháp tiếp cận cốt lõi:
#    - Top-Down (Memoization - Đệ quy có nhớ): Bắt đầu từ bài toán lớn n, phân rã đệ quy
#      xuống các bài con; lưu kết quả vào bảng băm (memo table) để tra cứu O(1).
#    - Bottom-Up (Tabulation - Lập bảng từ dưới lên): Khởi tạo từ các bài toán cơ sở (Base cases)
#      rồi chạy vòng lặp tuần tự tính lên n. Ưu điểm: Không tốn Call Stack, không lo tràn đệ quy.
#
# BÀI TOÁN 1: DÃY SỐ FIBONACCI (FIBONACCI SEQUENCE)
# Dãy: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Công thức: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) với n >= 2.


# Cấp độ 1: Naive Recursive (Đệ quy ngây thơ)
# - Time: O(2^n) - Cây đệ quy phân nhánh nhị phân bùng nổ cấp số nhân.
# - Space: O(n) - Độ sâu tối đa của Call Stack.
def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Cấp độ 2: Top-Down Memoization (Đệ quy có nhớ)
# - Time: O(n) - Mỗi trạng thái từ 0..n chỉ được tính đúng 1 lần.
# - Space: O(n) - Bộ nhớ cho memo dict và Call Stack.
def fibonacci_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# Cấp độ 3: Bottom-Up Tabulation (Lập bảng mảng tuần tự)
# - Time: O(n) - Vòng lặp đơn tính từ F(2) đến F(n).
# - Space: O(n) - Mảng dp kích thước n + 1. Không sợ RecursionError.
def fibonacci_tabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Cấp độ 4: Space-Optimized Iterative (Tối ưu không gian O(1))
# - Time: O(n)
# - Space: O(1) - Chỉ cần 2 biến lưu 2 giá trị liền kề trước đó.
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# BÀI TOÁN 2: BÀI TOÁN LEO BẬC THANG (CLIMBING STAIRS - ỨNG DỤNG ĐỒNG DẠNG)
# Bài toán: Có một cầu thang gồm n bậc. Mỗi lần bạn có thể bước 1 bậc hoặc 2 bậc.
# Hỏi có bao nhiêu cách khác nhau để leo lên đỉnh?
#
# Phân tích ánh xạ sang Fibonacci:
# - Để bước tới bậc n, bạn chỉ có thể xuất phát từ:
#   + Bậc (n - 1) rồi bước 1 bước
#   + Bậc (n - 2) rồi bước 2 bước
# => Số cách lên bậc n: Ways(n) = Ways(n - 1) + Ways(n - 2).
# Cơ sở: Ways(1) = 1 (1 cách: 1), Ways(2) = 2 (2 cách: 1+1 hoặc 2).
# Bản chất bài toán chính là dãy Fibonacci tịnh tiến 1 vị trí!

def climb_stairs(n: int) -> int:
    """
    Tìm số cách leo cầu thang n bậc với Space O(1), Time O(n).
    """
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


if __name__ == "__main__":
    n = 10
    print("--- 1. FIBONACCI BENCHMARK (n=10) ---")
    print(f"Fibonacci({n}) Naive Recursive :", fibonacci_recursive(n))  # 55
    print(f"Fibonacci({n}) Memoization      :", fibonacci_memo(n))       # 55
    print(f"Fibonacci({n}) Tabulation       :", fibonacci_tabulation(n)) # 55
    print(f"Fibonacci({n}) Space-Optimized  :", fibonacci(n))            # 55

    first_10 = [fibonacci(i) for i in range(10)]
    print("First 10 Fibonacci numbers   :", first_10)

    print("\n--- 2. CLIMBING STAIRS (Fibonacci Application) ---")
    for steps in range(1, 6):
        print(f"Ways to climb {steps} steps: {climb_stairs(steps)}")
