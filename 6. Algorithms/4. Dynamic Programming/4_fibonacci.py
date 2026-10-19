# BÀI TOÁN DÃY SỐ FIBONACCI (FIBONACCI SEQUENCE):
# - Dãy số: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# - Công thức truy hồi: F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) với n >= 2.
#
# Bài toán này là ví dụ kinh điển để thấy rõ sự tiến hóa từ thuật toán ngây thơ
# đến Quy hoạch động (Dynamic Programming) và tối ưu hóa không gian (Space Optimization).


# 1. Naive Recursive Approach (Đệ quy thuần túy):
# - Độ phức tạp thời gian: O(2^n) - Cây đệ quy phân nhánh nhị phân bùng nổ theo cấp số nhân.
# - Độ phức tạp không gian: O(n) - Độ sâu tối đa của Call Stack.
# - Nhược điểm: Bị Overlapping Subproblems (bài toán con lặp lại cực kỳ nhiều lần).
def fibonacci_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# 2. Top-Down Approach (Memoization - Đệ quy có nhớ):
# - Độ phức tạp thời gian: O(n) - Mỗi bài toán con từ 0 đến n chỉ giải đúng 1 lần.
# - Độ phức tạp không gian: O(n) - Tốn bộ nhớ cho hash map/dict lưu đệm và Call Stack.
def fibonacci_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# 3. Bottom-Up Approach (Tabulation - Lập bảng từ dưới lên):
# - Độ phức tạp thời gian: O(n) - Vòng lặp đơn tính tuần tự từ F(2) đến F(n).
# - Độ phức tạp không gian: O(n) - Cấp phát mảng dp kích thước n + 1.
# - Ưu điểm: Không dùng đệ quy -> Không sợ RecursionError (tràn Call Stack).
def fibonacci_tabulation(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 4. Space-Optimized Iterative Approach (Tối ưu không gian bằng Tuple Unpacking):
# - Độ phức tạp thời gian: O(n) - Duyệt qua 1 vòng lặp n bước.
# - Độ phức tạp không gian: O(1) - Chỉ dùng đúng 2 biến con trỏ trạng thái (a, b).
#
# Cơ chế hoạt động của 'a, b = b, a + b':
# - Python tính toán toàn bộ vế phải trước (b, a + b) thành một tuple tạm thời trong bộ nhớ.
# - Sau đó mở gói (unpack) đồng thời vào hai biến vế trái:
#     + a mới nhận giá trị của b cũ (tương đương F(k) -> F(k+1))
#     + b mới nhận giá trị của a + b cũ (tương đương F(k+1) -> F(k+2))
# - Kỹ thuật này giúp dịch chuyển "cửa sổ trượt" (sliding window) 2 phần tử mà không cần biến tạm 'temp'.
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) Naive Recursive :", fibonacci_recursive(n))  # 55
    print(f"Fibonacci({n}) Memoization      :", fibonacci_memo(n))       # 55
    print(f"Fibonacci({n}) Tabulation       :", fibonacci_tabulation(n)) # 55
    print(f"Fibonacci({n}) Space-Optimized  :", fibonacci(n))            # 55

    # In ra 10 so dau tien trong day Fibonacci bang ham toi uu:
    first_10 = [fibonacci(i) for i in range(10)]
    print("\nFirst 10 Fibonacci numbers:", first_10)
    # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
