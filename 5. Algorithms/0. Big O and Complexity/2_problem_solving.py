# PHẦN 1: QUY TRÌNH GIẢI TOÁN & MẸO TỐI ƯU HÓA CODE (OPTIMIZATION TRICKS)
# Quy trình cốt lõi:
# 1. Hiểu đề bài: Xác định rõ Input, Output và Constraints (Ràng buộc)
# 2. Viết mã giả (Pseudocode): Mô tả logic dạng văn bản dễ hiểu, độc lập ngôn ngữ
# 3. Chọn cấu trúc dữ liệu & Xét trường hợp biên (Edge Cases: chuỗi rỗng, mảng 1 phần tử...)
# 4. Cài đặt, so sánh độ phức tạp và tối ưu (Refactoring)

# Ví dụ bài toán: Đảo ngược chuỗi (Reverse a String)
test_str = "hello"
empty_str = ""  # Edge case

# Sử dụng Slicing [::-1] (Ngắn gọn, tối ưu trong Python - O(n)):
def reverse_slice(s: str) -> str:
    return s[::-1]

# Vòng lặp duyệt tuần tự (Cài đặt dựa trên Pseudocode):
#   GET original_string
#   SET reversed_string = ""
#   FOR EACH char IN original_string:
#       ADD char TO THE BEGINNING OF reversed_string
def reverse_loop(s: str) -> str:
    res = ""
    for char in s:
        res = char + res
    return res

# Sử dụng reversed() và join():
def reverse_builtin(s: str) -> str:
    return "".join(reversed(s))

print("Slice [::-1]:", reverse_slice(test_str))        # olleh
print("Looping:", reverse_loop(test_str))              # olleh
print("Builtin:", reverse_builtin(test_str))          # olleh
print("Edge case (empty):", repr(reverse_slice(empty_str))) # ''

# Lưu ý tối ưu hiệu năng chuỗi (String Optimization & Big O):
# - Chuỗi (str) là immutable: cộng chuỗi dồn dập trong vòng lặp (res += char) tốn O(n^2) do phải cấp phát và sao chép lại bộ nhớ liên tục.
# - Giải pháp tối ưu O(n): gom các ký tự vào list (list.append) rồi dùng ''.join(list), hoặc dùng generator expression bên trong ''.join().
chars = ['a', 'b', 'c', 'd']
print("Optimized O(n):", ''.join(chars))  # 'abcd'

# Kỹ thuật Hai con trỏ (Two Pointers) & Thao tác tại chỗ (In-place - Space O(1)):
# - Khi bài toán yêu cầu dồn/lọc phần tử trong mảng (VD: Move Zeroes, Remove Duplicates) mà không cấp phát mảng phụ (O(1) Space):
# - Dùng 1 con trỏ (read pointer) để duyệt qua toàn bộ mảng, 1 con trỏ (write pointer) đánh dấu vị trí cần ghi đè tiếp theo.
def move_zeros_inplace(arr: list[int | bool]) -> list[int | bool]:
    write_idx = 0
    for read_idx in range(len(arr)):
        if arr[read_idx] != 0 or arr[read_idx] is False:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    while write_idx < len(arr):
        arr[write_idx] = 0
        write_idx += 1
    return arr

sample_arr: list[int | bool] = [0, 1, 0, 3, 12, False]
print("Two Pointers (In-place O(1) Space):", move_zeros_inplace(sample_arr))

# Kỹ thuật Tích lũy tổng một lần (Prefix Sum / Pivot Index / Equal Sides of Array):
# - Tìm index i sao cho sum(arr[:i]) == sum(arr[i+1:]).
# - Tránh gọi sum() trong vòng lặp (gây O(n^2)).
# - Tối ưu O(n) Time & O(1) Space: Tính trước total_sum = sum(arr), duy trì left_sum và suy ra right_sum.
def find_even_index(arr: list[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i, num in enumerate(arr):
        if left_sum == total_sum - left_sum - num:
            return i
        left_sum += num
    return -1

print("Pivot index (Equal sides):", find_even_index([1, 2, 3, 4, 3, 2, 1]))  # 3

# Kỹ thuật Thoát sớm / Nhận diện mẫu (Early Exit & Pattern Recognition):
# - Thay vì đếm toàn bộ mảng O(n) Space, khai thác tính chất bài toán để dừng sớm và tối ưu Space O(1).
# - Ví dụ: Mảng toàn số giống nhau trừ 1 số khác biệt -> Chỉ cần xét 3 phần tử đầu để tìm số chiếm đa số.
def find_unique_fast(arr: list[int]) -> int | None:
    if len(arr) < 3:
        return None

    common = arr[0] if arr[0] == arr[1] or arr[0] == arr[2] else arr[1]
    for x in arr:
        if x != common:
            return x
    return None

print("Find Unique (Early Exit O(1) Space):", find_unique_fast([1, 1, 1, 2, 1, 1]))  # 2

# Khởi tạo giá trị cực trị an toàn với float('inf') và float('-inf'):
# - Tránh gán số cứng tùy tiện (như 999999 hay 1_000_000_000) vì dữ liệu lớn có thể vượt qua mốc này.
# - float('inf') luôn lớn hơn mọi số hữu hạn; float('-inf') luôn nhỏ hơn mọi số hữu hạn.
def find_min_ratio(limits: list[int | float]) -> int | float:
    min_val: int | float = float('inf')
    for val in limits:
        if val < min_val:
            min_val = val
    return min_val if min_val != float('inf') else 0

print("Safe Min with inf:", find_min_ratio([50, 12, 100, 3]))  # 3
print("inf comparison:", float('inf') > 10**18)               # True

# Kỹ thuật Bánh đà Nguyên tố (Wheel Factorization 6k ± 1) - Tối ưu O(sqrt(n)):
# - Mọi số nguyên tố > 3 đều có dạng 6k - 1 hoặc 6k + 1 (5, 7, 11, 13, 17, 19...).
# - Xử lý riêng 2 và 3, sau đó bắt đầu từ d=5 và luân phiên nhảy bước +2, +4 bằng công thức: diff = 6 - diff.
# - Loại bỏ được 66.7% các hợp số, tăng tốc gấp 3 lần so với duyệt tuần tự.
def is_prime_fast(n: int) -> bool:
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    d, diff = 5, 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += diff
        diff = 6 - diff  # Đảo bước nhảy: 2 -> 4 -> 2 -> 4...
    return True

print("is_prime_fast(29):", is_prime_fast(29))  # True
print("is_prime_fast(49):", is_prime_fast(49))  # False

# Kỹ thuật Local Method Caching (Tối ưu vi mô CPython):
# - Trong CPython, gọi `res.append(...)` tốn chi phí tra cứu thuộc tính (LOAD_ATTR) ở mỗi lần lặp.
# - Gán `app = res.append` đưa hàm thành biến cục bộ (LOAD_FAST), giúp tăng tốc đáng kể trong vòng lặp lớn.
items: list[int] = []
app = items.append  # Cache method append thành biến cục bộ
for i in range(5):
    app(i * 10)
print("Cached append:", items)  # [0, 10, 20, 30, 40]

# Thuật toán Hoán vị kế tiếp (Next Permutation / Next Bigger Number) - O(n) Time:
# 1. Quét từ phải sang trái tìm vị trí i đầu tiên mà digits[i] < digits[i + 1] (điểm gãy).
# 2. Quét từ phải sang trái tìm vị trí j đầu tiên mà digits[j] > digits[i], rồi hoán đổi vị trí i và j.
# 3. Đảo ngược đoạn đuôi từ i + 1 đến hết bằng Slice Assignment: digits[i + 1:] = digits[i + 1:][::-1]
def next_permutation(digits: list[int]) -> list[int] | None:
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i < 0:
        return None  # Đã là hoán vị lớn nhất có thể

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = digits[i + 1:][::-1]  # Slice assignment tại chỗ
    return digits

print("Next Permutation [1, 2, 4, 3]:", next_permutation([1, 2, 4, 3]))  # [1, 3, 2, 4]

# Kỹ thuật Đường tắt hiệu năng (Fast-Path Optimization):
# - Nhận diện trường hợp xuất hiện với xác suất cao nhất (common case) và xử lý bằng phép toán siêu nhanh (O(1)) trước.
# - Ví dụ: Trong bài toán số kế tiếp, hoán vị 2 số cuối chiếm ~50% trường hợp ngẫu nhiên.
# - Số học: Đổi chỗ chữ số hàng chục (d1) và đơn vị (d0) chỉ tốn phép tính: n + 9 * (d0 - d1)
def next_bigger_fast_path(n: int) -> int | None:
    d0 = n % 10
    d1 = (n // 10) % 10
    diff = d0 - d1
    if diff > 0:
        return n + 9 * diff  # Fast-path xử lý trong ~15 nanoseconds, không tốn loop hay array
    # Logic tổng quát phía sau cho trường hợp phức tạp...
    return None

print("Fast-Path (5917 -> 5971):", next_bigger_fast_path(5917))  # 5971

# Kỹ thuật Tách ghép chuỗi (String Slicing Decomposition):
# - Ghép hoán vị kế tiếp trực tiếp trên chuỗi chỉ bằng 1 lần cấp phát bộ nhớ (Zero Array Allocation):
# - Cấu trúc: s[:i] + s[j] + s[L-1:j:-1] + pivot + s[j-1:i:-1]
def next_bigger_sliced(n: int) -> int:
    s = str(n)
    L = len(s)
    i = L - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i < 0:
        return -1

    pivot = s[i]
    j = L - 1
    while s[j] <= pivot:
        j -= 1

    # Tái tạo chuỗi kết quả gồm 5 phần ghép lại:
    # 1. s[:i]           : Phần đầu giữ nguyên
    # 2. s[j]            : Ký tự nhỏ nhất lớn hơn pivot đưa lên đầu đoạn hoán vị
    # 3. s[L-1 : j : -1] : Đoạn sau j đảo ngược
    # 4. pivot           : Ký tự s[i] cũ đưa vào giữa
    # 5. s[j-1 : i : -1] : Đoạn trước j đảo ngược
    return int(s[:i] + s[j] + s[L - 1 : j : -1] + pivot + s[j - 1 : i : -1])

print("String Slicing Decomposition (2017):", next_bigger_sliced(2017))  # 2071


# Hoán vị kế tiếp nhỏ hơn (Next Smaller Permutation) & Bẫy số 0 đứng đầu (Leading Zero):
# - Tìm số nhỏ hơn lớn nhất có cùng các chữ số, nhưng KHÔNG được phép có số 0 ở đầu (ví dụ: 1027 -> -1).
def next_smaller(n: int) -> int:
    if n < 21:
        return -1

    # Fast-path 2 chữ số cuối
    d0 = n % 10
    n1 = n // 10
    d1 = n1 % 10
    diff = d1 - d0
    if diff > 0:
        if d0 or n1 > 9:
            return n - 9 * diff
        return -1

    s = str(n)
    L = len(s)
    i = L - 3
    while i >= 0 and s[i] <= s[i + 1]:
        i -= 1
    if i < 0:
        return -1

    pivot = s[i]
    j = L - 1
    while s[j] >= pivot:
        j -= 1

    # Chặn số 0 đứng đầu
    if i == 0 and s[j] == '0':
        return -1

    return int(s[:i] + s[j] + s[L - 1 : j : -1] + pivot + s[j - 1 : i : -1])

print("Next Smaller (2071):", next_smaller(2071))  # 2017
print("Next Smaller with Leading Zero (1027):", next_smaller(1027))  # -1


# PHẦN 2: CÁC MẪU GIẢI THUẬT KINH ĐIỂN (CLASSIC ALGORITHMIC PATTERNS)

# 1. KỸ THUẬT CỬA SỔ TRƯỢT (SLIDING WINDOW)
# Ý tưởng: Dùng một "khung cửa sổ" kích thước k hoặc co giãn trên mảng/chuỗi.
# Khi trượt sang phải: thêm phần tử mới vào bên phải, bớt phần tử cũ ở bên trái.
# Giảm độ phức tạp từ O(n * k) hoặc O(n^2) xuống O(n).

# Bài toán: Tìm tổng lớn nhất của dãy con liên tiếp độ dài k
def max_sum_subarray(arr: list[int], k: int) -> int | None:
    if len(arr) < k:
        return None

    # Tính tổng cửa sổ đầu tiên độ dài k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Trượt cửa sổ từ vị trí k đến hết mảng: thêm arr[i], bớt arr[i - k]
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

nums: list[int] = [2, 1, 5, 1, 3, 2]
print("Sliding Window Max Sum (k=3):", max_sum_subarray(nums, 3))  # 5 + 1 + 3 = 9


# 2. KỸ THUẬT MẢNG TIỀN TỐ (PREFIX SUM)
# Ý tưởng: Tiền xử lý tính mảng cộng dồn P trong O(n):
#   P[i] = arr[0] + arr[1] + ... + arr[i]
# Sau đó, truy vấn tổng bất kỳ đoạn [left, right] chỉ mất O(1):
#   Sum(left, right) = P[right] - (P[left - 1] if left > 0 else 0)

class PrefixSum:
    def __init__(self, arr: list[int]) -> None:
        self.prefix: list[int] = []
        current_sum = 0
        for x in arr:
            current_sum += x
            self.prefix.append(current_sum)

    def query(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]

ps = PrefixSum([1, 2, 3, 4, 5, 6])
# Truy vấn tổng từ index 1 đến 4 ([2, 3, 4, 5]):
print("Prefix Sum Query [1, 4]:", ps.query(1, 4))  # 14


# 3. KỸ THUẬT HASH MAP LOOKUP (MẪU TWO SUM - ĐỔI SPACE LẤY TIME)
# Ý tưởng: Thay vì dùng 2 vòng lặp O(n^2) để tìm cặp thỏa mãn điều kiện target,
# ta dùng dict để ghi nhớ các phần tử và index đã duyệt qua.
# Tại mỗi phần tử x, tra cứu bù trừ (target - x) trong dict với chi phí O(1).
# Kết quả: Giảm thời gian từ O(n^2) -> O(n), đánh đổi thêm O(n) bộ nhớ.

def two_sum(nums: list[int], target: int) -> list[int] | None:
    seen: dict[int, int] = {}  # Lưu {giá trị: index}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], idx]
        seen[num] = idx
    return None

sample_nums = [2, 7, 11, 15]
target_val = 9
print("Two Sum Indices:", two_sum(sample_nums, target_val))  # [0, 1] (vì 2 + 7 = 9)
