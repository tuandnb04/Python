# Tự động hóa Dynamic Programming (Memoization) bằng @functools.cache (Python 3.9+)
from functools import cache

# => TẠI SAO @CACHE TỐT HƠN VIẾT MEMOIZATION THỦ CÔNG (memo={})?
# 1. Loại bỏ hoàn toàn mã lặp (Boilerplate): Không cần tự truyền tham số `memo={}` hoặc tự kiểm tra `if n in memo`.
# 2. Tối ưu hiệu năng ở cấp độ C (C-level implementation): Nhanh hơn việc thao tác dict thủ công trong Python.
# 3. An toàn đa luồng (Thread-safe): Được bảo vệ chống xung đột dữ liệu khi chạy đa luồng.

# 1. Climbing Stairs với @cache (Tương đương Memoization Top-Down O(n))
@cache
def climb_stairs_cached(n: int) -> int:
    if n <= 2:
        return n
    return climb_stairs_cached(n - 1) + climb_stairs_cached(n - 2)

# 2. Min Coins (Coin Change) với @cache
@cache
def min_coins_cached(amount: int, coins: tuple[int, ...]) -> float:
    if amount == 0:
        return 0
    min_val = float('inf')
    for coin in coins:
        if coin <= amount:
            min_val = min(min_val, min_coins_cached(amount - coin, coins) + 1)
    return min_val

print("Climb stairs (n=10) with @cache:", climb_stairs_cached(10)) # 89
print("Min coins for 6 with (1, 3, 4):", min_coins_cached(6, (1, 3, 4))) # 2
