import bisect

# BÀI HỌC: CHUỖI CON CHUNG DÀI NHẤT (LCS) & DÃY CON TĂNG DÀI NHẤT (LIS)
#
# BẢN CHẤT & GIA PHẢ:
# - Cả 2 bài toán đều thuộc nhóm Quy hoạch động trên chuỗi và dãy số (Sequence DP).
# - Phân biệt khái niệm:
#   + Substring (Chuỗi con liên tiếp): Các ký tự phải liền kề nhau (ví dụ: "BCD" trong "ABCDE").
#   + Subsequence (Chuỗi con không liên tiếp): Giữ nguyên thứ tự xuất hiện nhưng không cần liền kề
#     (ví dụ: "ACE" là subsequence của "ABCDE").
#
# ỨNG DỤNG THỰC TẾ CỦA LCS:
# - Công cụ Git Diff: So sánh sự khác nhau giữa 2 commit code.
# - Sinh học phân tử (Bioinformatics): So sánh độ tương đồng giữa hai chuỗi gen/ADN.
# - Kiểm tra đạo văn (Plagiarism Detection).


# 1. Longest Common Subsequence (LCS)
# Công thức quy hoạch động:
# Gọi dp[i][j] là độ dài LCS của text1[0..i-1] và text2[0..j-1]:
# - Nếu text1[i-1] == text2[j-1]:
#     dp[i][j] = dp[i-1][j-1] + 1  (Ký tự giống nhau, tăng độ dài)
# - Nếu khác nhau:
#     dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (Chọn hướng có độ dài lớn hơn)

def longest_common_subsequence(text1: str, text2: str) -> tuple[int, str]:
    """
    Compute LCS length and reconstruct the longest common subsequence string.
    - Time complexity: O(m * n)
    - Space complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill 2D DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    # Backtracking to reconstruct subsequence characters
    lcs_chars: list[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs_chars.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_chars.reverse()
    return lcs_length, "".join(lcs_chars)


# 2. Longest Increasing Subsequence (LIS)
# Bài toán: Cho một mảng số nguyên, tìm độ dài của dãy con tăng dần nghiêm ngặt dài nhất.

def lis_dp_quadratic(nums: list[int]) -> int:
    """
    Classic O(n^2) Dynamic Programming solution.
    dp[i] represents the length of LIS ending at index i.
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(nums: list[int]) -> int:
    """
    Optimized O(n log n) Patience Sorting with Binary Search.
    Maintains `tails` array storing smallest tail of all increasing subsequences of various lengths.
    """
    tails: list[int] = []

    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            # Overwrite to keep smallest tail element possible
            tails[idx] = x

    return len(tails)


# Thực thi & Kiểm chứng
if __name__ == "__main__":
    # Demo LCS
    s1 = "ABCBDAB"
    s2 = "BDCABA"
    length, lcs_str = longest_common_subsequence(s1, s2)
    print("--- 1. Longest Common Subsequence (LCS) ---")
    print(f"String 1: '{s1}'")
    print(f"String 2: '{s2}'")
    print(f"LCS Length: {length}")
    print(f"LCS Subsequence: '{lcs_str}'")

    # Demo LIS
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("\n--- 2. Longest Increasing Subsequence (LIS) ---")
    print(f"Array: {nums}")
    print("LIS O(n^2) DP length:         ", lis_dp_quadratic(nums))      # 4 ([2, 3, 7, 101])
    print("LIS O(n log n) Binary Search: ", lis_binary_search(nums))     # 4
