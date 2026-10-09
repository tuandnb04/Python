import bisect

# 1. Linear Search (Tìm kiếm tuyến tính) - O(n) thời gian, O(1) không gian
# - Không yêu cầu mảng phải được sắp xếp trước.
# - Duyệt tuần tự từ đầu tới cuối mảng cho đến khi tìm thấy target hoặc hết mảng.
def linear_search(arr: list[int], target: int) -> int:
    # Chuẩn Pythonic: Dùng enumerate thay vì range(len(arr)) khi cần cả chỉ số và giá trị
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

unsorted_list = [13, 4, 7, 9, 10]
print("Linear search (find 9):", linear_search(unsorted_list, 9))   # 3
print("Linear search (find 5):", linear_search(unsorted_list, 5))   # -1


# 2. Binary Search vòng lặp (Iterative Binary Search) - O(log n) thời gian, O(1) không gian
# - ĐIỀU KIỆN BẮT BUỘC: Danh sách phải được sắp xếp tăng dần!
# - Khi nào nên dùng?
#   + Khi mảng đã sắp xếp sẵn từ trước.
#   + Hoặc khi thực hiện nhiều truy vấn (queries) trên cùng một tập dữ liệu tĩnh.
#   (Nếu mảng chưa sắp xếp và chỉ tìm 1 lần: Sort O(n log n) + Search O(log n) chậm hơn Linear Search O(n)).
def binary_search(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1

    while low <= high:
        # mid = low + (high - low) // 2: Tránh tràn số nguyên trong C++/Java khi low + high quá lớn
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1      # Thu hẹp phạm vi sang nửa bên phải
        else:
            high = mid - 1     # Thu hẹp phạm vi sang nửa bên trái

    return -1                  # Trả về -1 nếu target không tồn tại

sorted_list = [4, 7, 9, 10, 13]
print("Binary search iterative (find 9):", binary_search(sorted_list, 9))     # 2
print("Binary search iterative (find 5):", binary_search(sorted_list, 5))     # -1


# 3. Binary Search đệ quy (Recursive Binary Search) - O(log n) thời gian, O(log n) không gian
# - CẠM BẪY CẦN TRÁNH: Không dùng slicing mảng arr[:mid] hay arr[mid+1:]
#   vì mỗi lần cắt mảng sẽ copy mảng con tốn O(n) thời gian & bộ nhớ!
# - Giải pháp chuẩn: Luôn truyền hai con trỏ chỉ số low và high qua từng frame đệ quy.
def binary_search_recursive(arr: list[int], target: int, low: int = 0, high: int | None = None) -> int:
    if high is None:
        high = len(arr) - 1

    if low > high:             # Base case: Không tìm thấy target
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:     # Base case: Tìm thấy target
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

print("Binary search recursive (find 9):", binary_search_recursive(sorted_list, 9))  # 2
print("Binary search recursive (find 5):", binary_search_recursive(sorted_list, 5))  # -1


# 4. Tìm kiếm vị trí đầu tiên & cuối cùng (First & Last Occurrence with Duplicates)
# - Khi mảng có các phần tử trùng lặp, Binary Search cơ bản chỉ tìm thấy một vị trí bất kỳ.
# - Biến thể tìm First Occurrence (Lower Bound) và Last Occurrence (Upper Bound):
duplicate_list = [1, 2, 2, 2, 3, 5, 8]

def binary_search_first(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            high = mid - 1     # Tiếp tục thu hẹp về nửa bên trái để tìm vị trí xuất hiện sớm hơn
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def binary_search_last(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid
            low = mid + 1      # Tiếp tục thu hẹp về nửa bên phải để tìm vị trí xuất hiện muộn hơn
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

print("First occurrence of 2 in [1, 2, 2, 2, 3, 5, 8]:", binary_search_first(duplicate_list, 2))  # 1
print("Last occurrence of 2 in [1, 2, 2, 2, 3, 5, 8]:", binary_search_last(duplicate_list, 2))   # 3


# 5. Chuẩn Pythonic trong thực tế: Module `bisect` (Triển khai ở tầng C)
# - bisect.bisect_left: Tìm index đầu tiên của target (tương đương First Occurrence).
# - bisect.bisect_right: Tìm index sau phần tử trùng cuối cùng (Last Occurrence + 1).
first_idx = bisect.bisect_left(duplicate_list, 2)
last_idx = bisect.bisect_right(duplicate_list, 2) - 1

print("bisect_left (First 2):", first_idx)  # 1
print("bisect_right (Last 2):", last_idx)   # 3


# 6. Binary Search theo dõi tiến trình duyệt (Search Path Tracking)
# - Lưu lại vết các phần tử ở vị trí giữa (mid) được xét qua từng bước
# - Giúp trực quan hóa cách Binary Search thu hẹp không gian tìm kiếm
def binary_search_trace(search_list: list[int], value: int) -> tuple[list[int], int]:
    path_to_target: list[int] = []
    low, high = 0, len(search_list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, mid
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return path_to_target, -1

path1, idx1 = binary_search_trace([1, 2, 3, 4, 5], 3)
path2, idx2 = binary_search_trace([1, 2, 3, 4, 5, 9], 4)
path3, idx3 = binary_search_trace([1, 3, 5, 9, 14, 22], 10)

print(f"Search 3 in [1, 2, 3, 4, 5] -> Path: {path1}, Index: {idx1}")
print(f"Search 4 in [1, 2, 3, 4, 5, 9] -> Path: {path2}, Index: {idx2}")
print(f"Search 10 in [1, 3, 5, 9, 14, 22] -> Path: {path3}, Index: {idx3}")


# 7. Binary Search on Answer (Tìm kiếm nhị phân trên không gian nghiệm)
# - Dùng cho các bài toán tối ưu: tìm nghiệm nhỏ nhất / lớn nhất thỏa mãn một điều kiện.
# - Bài toán ví dụ: Tìm căn bậc hai nguyên lớn nhất của số n (tức floor(sqrt(n))) với O(log n).
def integer_sqrt(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n

    low, high = 1, n
    ans = 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid <= n:
            ans = mid          # mid hợp lệ, thử tìm giá trị lớn hơn ở nửa phải
            low = mid + 1
        else:
            high = mid - 1     # mid * mid > n, thu hẹp về nửa trái

    return ans

print("integer_sqrt(16):", integer_sqrt(16))  # 4
print("integer_sqrt(26):", integer_sqrt(26))  # 5 (vì 5^2 = 25 <= 26 < 6^2)


# Biến thể: Bisection Method trên số thực (Floating-Point Binary Search)
# - Dùng cho tìm nghiệm liên tục với sai số cho phép (tolerance).
# - Cạm bẫy: Khi 0 < number < 1, căn bậc hai lớn hơn chính nó (vd sqrt(0.25) = 0.5),
#   nên cận trên bắt buộc phải là max(1.0, number).
def bisection_sqrt(number: float, tolerance: float = 1e-6, max_iter: int = 100) -> float:
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number in (0.0, 1.0):
        return number

    low = 0.0
    high = max(1.0, number)

    for _ in range(max_iter):
        mid = (low + high) / 2.0
        if high - low <= tolerance:
            return mid

        if mid * mid < number:
            low = mid
        else:
            high = mid

    raise RuntimeError(f"Failed to converge within {max_iter} iterations")


print(f"bisection_sqrt(2):    {bisection_sqrt(2.0):.6f}")    # ~1.414214
print(f"bisection_sqrt(0.25): {bisection_sqrt(0.25):.6f}")   # 0.500000

