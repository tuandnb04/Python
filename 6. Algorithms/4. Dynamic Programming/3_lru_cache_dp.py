# Dynamic Programming (Memoization) với @functools.cache:
from functools import cache


# Climbing Stairs với @cache (Top-Down Memoization O(n))
@cache
def climb_stairs_cached(n: int) -> int:
    if n <= 2:
        return n
    return climb_stairs_cached(n - 1) + climb_stairs_cached(n - 2)


# Min Coins (Coin Change) với @cache
@cache
def min_coins_cached(amount: int, coins: tuple[int, ...]) -> float:
    if amount == 0:
        return 0
    min_val = float('inf')
    for coin in coins:
        if coin <= amount:
            min_val = min(min_val, min_coins_cached(amount - coin, coins) + 1)
    return min_val


print("Climb stairs (n=10) with @cache:", climb_stairs_cached(10))  # 89
print("Min coins for 6 with (1, 3, 4):", min_coins_cached(6, (1, 3, 4)))  # 2
