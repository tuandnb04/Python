import bisect

# 6. Algorithms - 1. Searching: Tìm kiếm nhị phân (Binary Search)
# Toàn diện kiến thức về Tìm kiếm nhị phân: Nguyên lý chia đôi, mô phỏng từng bước,
# cài đặt vòng lặp, đệ quy, các biến thể tìm biên và ứng dụng thực tế
#
# 1. Khái niệm về Tìm kiếm nhị phân (Binary Search)
# - Là thuật toán tìm kiếm phần tử trên một mảng ĐÃ ĐƯỢC SẮP XẾP (Sorted Array).
# - Cơ chế hoạt động:
#   + So sánh giá trị cần tìm (target) với phần tử ở chính giữa (middle) của mảng.
#   + Nếu target bằng phần tử ở giữa: trả về chỉ số index và kết thúc.
#   + Nếu target nhỏ hơn phần tử ở giữa: tiếp tục tìm kiếm ở nửa bên trái của mảng.
#   + Nếu target lớn hơn phần tử ở giữa: tiếp tục tìm kiếm ở nửa bên phải của mảng.
#   + Quá trình chia đôi không gian tìm kiếm lặp lại cho đến khi tìm thấy hoặc không gian tìm kiếm rỗng (trả về -1).
# - Độ phức tạp thời gian: O(log2 n) - nhanh hơn rất nhiều so với O(n) của Linear Search.

# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: [2, 3, 7, 7, 11, 15, 25], tìm giá trị target = 11
# - Bước 1: left = 0, right = 6.
# - Bước 2: mid = (0 + 6) // 2 = 3. arr[3] = 7.
#   Vì 7 < 11, ta loại bỏ nửa trái (chỉ số 0..3) và rẽ phải: left = mid + 1 = 4.
# - Bước 3: Nửa còn lại có chỉ số 4..6. mid = (4 + 6) // 2 = 5. arr[5] = 15.
#   Vì 15 > 11, ta loại bỏ nửa phải (chỉ số 5..6) và rẽ trái: right = mid - 1 = 4.
# - Bước 4: left = 4, right = 4. mid = (4 + 4) // 2 = 4. arr[4] = 11.
#   arr[4] == 11, tìm thấy phần tử tại index 4!


# 3. Cài đặt Binary Search vòng lặp (Iterative Binary Search)
# Sử dụng 2 con trỏ left và right để theo dõi phạm vi tìm kiếm:
def binary_search(arr, target_val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # mid = left + (right - left) // 2 để tránh tràn số nguyên khi left + right lớn
        mid = left + (right - left) // 2

        if arr[mid] == target_val:
            return mid
        elif arr[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Thử nghiệm với mảng mẫu:
mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11
result = binary_search(mylist, x)

if result != -1:
    print(f"Binary search for {x}: Found at index {result}")
else:
    print(f"Binary search for {x}: Not found")

# Thử nghiệm với mảng mô phỏng:
manual_list = [2, 3, 7, 7, 11, 15, 25]
print("Manual list search for 11:", binary_search(manual_list, 11))  # 4
print("Manual list search for 8 (not found):", binary_search(manual_list, 8))  # -1


# 4. Phân tích độ phức tạp thời gian O(log2 n)
# - Mỗi phép so sánh sẽ loại bỏ một nửa không gian tìm kiếm: n -> n/2 -> n/4 -> ... -> 1.
# - Số phép so sánh tối đa trong trường hợp xấu nhất là log2(n).
# - Ký hiệu O(log2 n) hay O(log n) nhấn mạnh việc cơ số 2 thể hiện bản chất chia đôi không gian.
# - So sánh tốc độ:
#   Với n = 1,000,000 phần tử:
#   + Linear Search tốn tối đa 1,000,000 phép so sánh.
#   + Binary Search chỉ tốn tối đa khoảng 20 phép so sánh (2^20 ≈ 1,048,576).


# 5. Cài đặt Binary Search đệ quy (Recursive Binary Search)
# Lưu ý: Truyền chỉ số left và right qua từng frame đệ quy,
# tuyệt đối không dùng slicing arr[:mid] vì cắt mảng sẽ tốn O(n) thời gian copy.
def binary_search_recursive(arr, target_val, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target_val:
        return mid
    elif arr[mid] < target_val:
        return binary_search_recursive(arr, target_val, mid + 1, right)
    else:
        return binary_search_recursive(arr, target_val, left, mid - 1)


print("\nRecursive binary search for 11:", binary_search_recursive(mylist, 11))  # 5
print("Recursive binary search for 99:", binary_search_recursive(mylist, 99))  # -1


# 6. Tìm vị trí đầu tiên & cuối cùng khi mảng có phần tử trùng lặp (Duplicates)
duplicate_list = [1, 2, 2, 2, 3, 5, 8]


# 6.1. Vị trí đầu tiên (First Occurrence / Lower Bound):
def binary_search_first(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1  # Tiếp tục thu hẹp sang nửa trái để tìm vị trí sớm hơn
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans


# 6.2. Vị trí cuối cùng (Last Occurrence / Upper Bound):
def binary_search_last(arr, target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1  # Tiếp tục thu hẹp sang nửa phải để tìm vị trí muộn hơn
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans


print("\nDuplicates Handling in [1, 2, 2, 2, 3, 5, 8]:")
print("First occurrence of 2:", binary_search_first(duplicate_list, 2))  # 1
print("Last occurrence of 2: ", binary_search_last(duplicate_list, 2))   # 3


# 7. Sử dụng module bisect có sẵn trong thư viện chuẩn Python
# - bisect.bisect_left: Tìm chỉ số chèn bên trái (tương đương First Occurrence).
# - bisect.bisect_right: Tìm chỉ số chèn bên phải (Last Occurrence + 1).
first_idx = bisect.bisect_left(duplicate_list, 2)
last_idx = bisect.bisect_right(duplicate_list, 2) - 1

print("\nPython 'bisect' module:")
print("bisect_left (First 2):", first_idx)  # 1
print("bisect_right (Last 2):", last_idx)   # 3


# 8. Theo dõi lộ trình tìm kiếm (Search Path Tracking)
# Ghi lại vết các phần tử ở vị trí giữa (mid) được xét qua từng bước
def binary_search_trace(arr, target):
    path = []
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        val = arr[mid]
        path.append(val)

        if val == target:
            return path, mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1

    return path, -1


trace_path, trace_idx = binary_search_trace([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 11)
print(f"\nSearch Path for 11: {trace_path} -> Found at index {trace_idx}")


# 9. Binary Search on Answer (Tìm kiếm nhị phân trên không gian nghiệm)
# Ứng dụng: Tìm căn bậc hai nguyên lớn nhất (floor(sqrt(n))) với độ phức tạp O(log n).
def integer_sqrt(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n

    left, right = 1, n
    ans = 1

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans


print("\nBinary Search on Answer:")
print("integer_sqrt(16):", integer_sqrt(16))  # 4
print("integer_sqrt(26):", integer_sqrt(26))  # 5 (5^2 = 25 <= 26 < 6^2)
