# 2 Điều kiện cốt lõi của Dynamic Programming (DP):
# Overlapping Subproblems (Các bài toán con gối nhau/trùng lặp)
# Optimal Substructure (Cấu trúc con tối ưu)

# Bài toán: Climbing Stairs (Có n bậc, mỗi lần bước 1 hoặc 2 bậc. Tìm số cách lên đỉnh?)

# Top-Down Approach (Memoization - Đệ quy có nhớ): O(n) thời gian, O(n) không gian
def climb_stairs_memo(n: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]                 # O(1) tra cứu từ bộ nhớ đệm
    if n <= 2:
        return n
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]

# Bottom-Up Approach (Tabulation - Lập bảng từ dưới lên): O(n) thời gian, O(n) không gian
def climb_stairs_tabulation(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Tối ưu không gian (Space-Optimized Tabulation): O(n) thời gian, O(1) không gian
def climb_stairs_optimized(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1

print("Memoization (n=5):", climb_stairs_memo(5))          # 8
print("Tabulation (n=5):", climb_stairs_tabulation(5))      # 8
print("Space-Optimized (n=5):", climb_stairs_optimized(5))# 8
