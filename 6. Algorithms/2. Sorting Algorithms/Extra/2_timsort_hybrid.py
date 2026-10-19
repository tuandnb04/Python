# 6. Algorithms - 2. Sorting - Extra: Thuật toán lai Timsort (Timsort Hybrid)
# Kiến trúc thuật toán sắp xếp mặc định của Python (list.sort & sorted) do Tim Peters thiết kế,
# kết hợp giữa Binary Insertion Sort (cho khối con nhỏ) và Merge Sort (để trộn các run)

# 1. Khái niệm và Lịch sử của Timsort
# - Timsort được Tim Peters phát minh vào năm 2002 để trở thành thuật toán sắp xếp mặc định của ngôn ngữ Python.
# - Sau đó, Timsort đã được áp dụng rộng rãi trong Java SE 7 (cho Arrays.sort trên Object), Android OS, và V8 Engine của Google Chrome.
# - Tư tưởng cốt lõi của Timsort:
#   + Dữ liệu trong thế giới thực hiếm khi hoàn toàn ngẫu nhiên mà thường có sẵn các đoạn con đã có thứ tự tự nhiên (gọi là "Run").
#   + Với các mảng nhỏ (kích thước <= 32 hoặc 64), Insertion Sort chạy nhanh hơn bất kỳ thuật toán O(n log n) nào
#     do có hằng số ẩn (Hidden Constant) cực nhỏ và tận dụng bộ nhớ đệm CPU (L1/L2 Cache) tối ưu.
#   + Do đó, Timsort chia mảng thành các "Run" có độ dài tối thiểu (MIN_RUN = 32), dùng Binary Insertion Sort
#     để sắp xếp từng Run, sau đó dùng Merge Sort để trộn các Run lại với nhau.


MIN_RUN = 32


# 2. Tính toán độ dài run tối ưu (Calculate Minrun)
# Mục tiêu: Chọn giá trị min_run trong khoảng [32, 64] sao cho số lượng run N / min_run xấp xỉ bằng một lũy thừa của 2,
# giúp cây trộn của Merge Sort luôn cân bằng hoàn hảo nhất.
def calculate_min_run(n):
    r = 0
    while n >= MIN_RUN:
        r |= (n & 1)
        n >>= 1
    return n + r


# 3. Thuật toán con 1: Binary Insertion Sort cho từng Run
# Dùng Binary Search để tìm vị trí chèn trong O(log k) phép so sánh, sau đó dịch chuyển mảng tại chỗ.
def binary_insertion_sort_run(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        # Tìm vị trí chèn bằng Binary Search
        low, high = left, i
        while low < high:
            mid = (low + high) // 2
            if key < arr[mid]:
                high = mid
            else:
                low = mid + 1
        pos = low

        # Dời các phần tử sang phải 1 nấc
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key


# 4. Thuật toán con 2: Merge 2 Run kề nhau (In-place buffer merge)
# Trộn 2 đoạn con đã sắp xếp arr[left..mid] và arr[mid+1..right]
def merge_runs(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    # Trộn với điều kiện '<=' để đảm bảo tính ỔN ĐỊNH (Stable Sort)
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# 5. Cài đặt thuật toán Timsort hoàn chỉnh
def timsort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    min_run = calculate_min_run(n)

    # Bước 1: Sắp xếp từng khối con có kích thước min_run bằng Binary Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        binary_insertion_sort_run(arr, start, end)

    # Bước 2: Trộn các Run bằng Merge Sort với kích thước tăng dần gấp đôi: min_run, 2*min_run, 4*min_run, ...
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            # Chỉ trộn khi mảng con bên phải thực sự tồn tại
            if mid < right:
                merge_runs(arr, left, mid, right)

        size *= 2

    return arr


# 6. Thử nghiệm thực tế với tập dữ liệu lớn
large_sample = [
    54, 26, 93, 17, 77, 31, 44, 55, 20, 2, 85, 99, 12, 45, 63, 71,
    38, 5, 47, 15, 36, 28, 65, 10, 84, 19, 73, 50, 91, 8, 60, 3,
    95, 41, 79, 16, 58, 25, 67, 33, 88, 7, 52, 22, 81, 14, 69, 30,
    97, 43, 75, 11, 57, 24, 64, 32, 86, 6, 49, 21, 83, 13, 68, 29
]

sample_copy = large_sample.copy()
print("Timsort Hybrid demonstration on 64 elements:")
print("Original first 10 elements:", large_sample[:10])
timsort(sample_copy)
print("Sorted first 10 elements:  ", sample_copy[:10])
print("Is properly sorted:        ", sample_copy == sorted(large_sample))


# 7. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tốt nhất (Best Case): O(n) khi dữ liệu đã sắp xếp sẵn hoặc gần như sắp xếp (Nearly sorted).
#     Timsort nhận diện các Run tự nhiên và chỉ tốn 1 lượt duyệt kiểm tra mà không tốn phép trộn nào!
#   + Trung bình (Average Case): O(n log n).
#   + Xấu nhất (Worst Case): O(n log n). Không bao giờ bị suy biến thành O(n^2) như Quicksort.
# - Độ phức tạp không gian (Space Complexity):
#   + O(n) bộ nhớ phụ để trộn các mảng con.
# - Tính ổn định: STABLE (Ổn định 100%), bảo toàn thứ tự ban đầu của các phần tử bằng nhau.
