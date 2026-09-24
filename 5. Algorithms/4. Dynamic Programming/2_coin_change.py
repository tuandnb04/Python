# Bài toán Coin Change (Đổi tiền xu bằng Quy hoạch động)
# Tìm số lượng đồng xu ít nhất để đổi thành số tiền 'amount'
# - Độ phức tạp thời gian: O(amount * số_loại_tiền)
# - Độ phức tạp không gian: O(amount)

def min_coins(amount, coins):
    # Khởi tạo bảng dp với giá trị vô cùng (infinity)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Cần 0 đồng xu cho số tiền 0

    # Lập bảng tính số xu tối thiểu cho từng mệnh giá từ 1 đến amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 3, 4]
target_amount = 6
print(f"Min coins for amount {target_amount} with coins {coins}:", min_coins(target_amount, coins)) # 2 (3 + 3)
