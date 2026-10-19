# BÀI HỌC: BÀI TOÁN CÁI TÚI 0/1 (0/1 KNAPSACK PROBLEM)
#
# BẢN CHẤT & GIA PHẢ:
# - Thuộc nhánh: Quy hoạch động (Dynamic Programming - DP).
# - Tại sao gọi là "0/1"?
#   Với mỗi món đồ, ta chỉ có 2 lựa chọn duy nhất:
#   + Chọn (1): Nhận giá trị (value) của món đồ và mất dung lượng (weight) trong túi.
#   + Bỏ qua (0): Giữ nguyên dung lượng túi.
#   Không được chọn một món đồ nhiều lần (khác Unbounded Knapsack) và không được chia nhỏ món đồ (khác Fractional Knapsack giải bằng Greedy).
#
# CÔNG THỨC TRUY HỒI (RECURRENCE RELATION):
#   Gọi dp[i][w] là giá trị lớn nhất đạt được khi xét i món đồ đầu tiên với sức chứa túi là w:
#   - Nếu weight[i-1] > w:
#       dp[i][w] = dp[i-1][w]  (Không thể chọn món đồ i)
#   - Nếu weight[i-1] <= w:
#       dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
#
# PHÂN TÍCH ĐỘ PHỨC TẠP:
# - Thời gian (Time Complexity): O(N * W) với N là số đồ vật, W là sức chứa túi.
# - Không gian (Space Complexity):
#   + Bảng 2D: O(N * W)
#   + Tối ưu 1D: O(W) (duyệt ngược từ W về weight để tránh dùng lặp một món đồ).


# 1. Giải pháp bảng 2D kết hợp truy vết (Backtracking)
def knapsack_01_2d(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
    """
    Solve 0/1 Knapsack using a 2D DP table and reconstruct selected item indices.
    Returns: (max_value, selected_item_indices)
    """
    n = len(weights)
    # Initialize DP table (n + 1) rows x (capacity + 1) cols
    dp: list[list[int]] = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Bottom-up table filling
    for i in range(1, n + 1):
        w_curr = weights[i - 1]
        v_curr = values[i - 1]
        for w in range(1, capacity + 1):
            if w_curr <= w:
                # Max of excluding item i vs including item i
                dp[i][w] = max(dp[i - 1][w], v_curr + dp[i - 1][w - w_curr])
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    # Backtracking to reconstruct chosen item indices
    selected_items: list[int] = []
    w = capacity
    for i in range(n, 0, -1):
        # If value differs from the previous row, item (i - 1) was picked
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    selected_items.reverse()
    return max_value, selected_items


# 2. Giải pháp tối ưu không gian bộ nhớ về mảng 1D O(W)
def knapsack_01_space_optimized(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Space-optimized 0/1 Knapsack using a 1D array.
    Iterates backward from capacity down to item weight to prevent duplicate item usage.
    """
    dp = [0] * (capacity + 1)

    for w_curr, v_curr in zip(weights, values):
        # Backward iteration guarantees 0/1 constraint
        for w in range(capacity, w_curr - 1, -1):
            dp[w] = max(dp[w], v_curr + dp[w - w_curr])

    return dp[capacity]


# Thực thi & Kiểm chứng
if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 8]
    capacity = 5

    print(f"Weights: {weights}")
    print(f"Values:  {values}")
    print(f"Capacity: {capacity}")

    # Chạy giải pháp bảng 2D với truy vết
    max_val_2d, chosen = knapsack_01_2d(weights, values, capacity)
    print("\n--- 1. 2D DP Solution ---")
    print(f"Max Value: {max_val_2d}")
    print(f"Chosen Item Indices: {chosen}")
    for idx in chosen:
        print(f" -> Item {idx}: Weight = {weights[idx]}, Value = {values[idx]}")

    # Chạy giải pháp tối ưu không gian 1D
    max_val_1d = knapsack_01_space_optimized(weights, values, capacity)
    print("\n--- 2. Space Optimized (1D Array) Solution ---")
    print(f"Max Value (1D): {max_val_1d}")
    assert max_val_2d == max_val_1d, "Both solutions must yield the same result!"
