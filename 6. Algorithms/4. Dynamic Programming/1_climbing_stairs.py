# LÝ THUYẾT CỐT LÕI VỀ DYNAMIC PROGRAMMING (DP - QUY HOẠCH ĐỘNG):
# 1. Hai điều kiện tiên quyết để áp dụng DP:
#    - Overlapping Subproblems (Bài toán con trùng lặp): Các bài toán con bị lặp lại nhiều lần.
#      * Lưu ý: Nếu các bài toán con độc lập, KHÔNG trùng lặp -> KHÔNG DÙNG DP (dùng Divide & Conquer).
#    - Optimal Substructure (Cấu trúc con tối ưu): Lời giải tối ưu của bài toán lớn được xây dựng
#      từ lời giải tối ưu của các bài toán con.
# 2. Bản chất chuyển đổi độ phức tạp & Đánh đổi (Trade-off):
#    - Chuyển độ phức tạp thời gian từ hàm mũ (Exponential - O(2^n)) sang đa thức (Polynomial - O(n)).
#    - Trade-off: Đánh đổi thêm bộ nhớ (Space) để lưu kết quả trung gian đổi lấy tốc độ (Time).
# 3. Hai hướng tiếp cận:
#    - Memoization (Top-Down): Đệ quy có nhớ, gặp kết quả đã lưu trong cache sẽ trả về ngay (O(1)).
#    - Tabulation (Bottom-Up): Vòng lặp từ dưới lên. Khởi tạo Base cases trước làm giá trị nền tảng
#      (foundational values). Ưu điểm: Tránh overhead đệ quy (không lo tràn Call Stack) và chạy tuần tự.

# Bài toán: Climbing Stairs (Có n bậc, mỗi lần bước 1 hoặc 2 bậc. Tìm số cách lên đỉnh?)

# 1. Naive Recursive Approach (Đệ quy thuần túy): O(2^n) thời gian, O(n) Call Stack
# Kém hiệu quả vì tính toán lặp đi lặp lại cùng một bài toán con nhiều lần (Overlapping Subproblems)
def climb_stairs_recursive(n: int) -> int:
    if n <= 2:
        return n
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


# 2. Top-Down Approach (Memoization - Đệ quy có nhớ): O(n) thời gian, O(n) không gian
def climb_stairs_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]  # O(1) tra cứu từ bộ nhớ đệm
    if n <= 2:
        return n
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


# 3. Bottom-Up Approach (Tabulation - Lập bảng từ dưới lên): O(n) thời gian, O(n) không gian
def climb_stairs_tabulation(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 4. Tối ưu không gian (Space-Optimized Tabulation): O(n) thời gian, O(1) không gian
def climb_stairs_optimized(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


print("Naive Recursive (n=5):", climb_stairs_recursive(5))  # 8
print("Memoization (n=5):", climb_stairs_memo(5))  # 8
print("Tabulation (n=5):", climb_stairs_tabulation(5))  # 8
print("Space-Optimized (n=5):", climb_stairs_optimized(5))  # 8
