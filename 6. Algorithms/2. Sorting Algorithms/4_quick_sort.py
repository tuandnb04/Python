# 6. Algorithms - 2. Sorting: Sắp xếp nhanh (Quicksort)
# Khái niệm thuật toán, phương pháp chia để trị (Divide and Conquer), phần tử chốt (Pivot),
# mô phỏng từng bước (Manual Run Through), phân hoạch Lomuto, 3-way partition, Median-of-Three và phân tích độ phức tạp

# 1. Khái niệm về Thuật toán Quicksort
# - Quicksort là một trong những thuật toán sắp xếp nhanh nhất và phổ biến nhất trong thực tế.
# - Thuật toán áp dụng tư tưởng "Chia để trị" (Divide and Conquer) kết hợp với Đệ quy (Recursion):
#   + Chọn một phần tử trong mảng làm "phần tử chốt" (Pivot). Có thể chọn phần tử cuối, đầu, giữa hoặc ngẫu nhiên.
#   + Phân hoạch (Partitioning): Sắp xếp lại mảng sao cho tất cả các phần tử nhỏ hơn Pivot nằm về bên trái,
#     và tất cả các phần tử lớn hơn Pivot nằm về bên phải. Phần tử Pivot sẽ nằm ở đúng vị trí cuối cùng của nó.
#   + Đệ quy: Gọi lại chính hàm Quicksort cho mảng con bên trái Pivot và mảng con bên phải Pivot.
#   + Điều kiện dừng (Base case): Khi mảng con chỉ còn 0 hoặc 1 phần tử (đã tự có thứ tự).


# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: [11, 9, 12, 7, 3]
# - Bước 1-3: Chọn phần tử cuối cùng là 3 làm Pivot.
#   Tất cả các số còn lại [11, 9, 12, 7] đều lớn hơn 3 nên phải nằm bên phải 3.
#   Hoán đổi 3 với 11:
#   -> [3 | 9, 12, 7, 11]
#   Số 3 đã ở đúng vị trí tuyệt đối đầu tiên của nó!
# - Bước 4-6: Xét mảng con bên phải [9, 12, 7, 11].
#   Chọn phần tử cuối cùng là 11 làm Pivot mới.
#   Số 7 và 9 nhỏ hơn 11 nên nằm bên trái, 12 lớn hơn 11 nên nằm bên phải.
#   Dịch chuyển và hoán đổi 11 với 12:
#   -> [3 | 9, 7, 11, 12]
#   Số 11 và 12 đã ở đúng vị trí tuyệt đối!
# - Bước 7-8: Xét mảng con [9, 7] bên trái 11.
#   Chọn 7 làm Pivot. Hoán đổi 9 với 7:
#   -> [3, 7, 9, 11, 12]
# -> Kết thúc: Toàn bộ mảng đã được sắp xếp tăng dần!


# 3. Cài đặt Quicksort cơ bản (Lomuto Partition Scheme)
# Thuật toán phân hoạch Lomuto:
# - Biến con trỏ `i` bắt đầu từ `low - 1`, đánh dấu ranh giới của các phần tử nhỏ hơn hoặc bằng Pivot.
# - Vòng lặp `j` quét từ `low` đến `high - 1`. Khi gặp `arr[j] <= pivot`, ta tăng `i` và hoán đổi `arr[i]` với `arr[j]`.
# - Cuối cùng, hoán đổi Pivot tại `arr[high]` với `arr[i + 1]` để đưa Pivot vào đúng vị trí giữa hai mảng con.
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    # Đưa pivot về đúng vị trí phân cách giữa nhóm nhỏ hơn và nhóm lớn hơn
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        # Tìm vị trí chỉ số của pivot sau khi phân hoạch
        pivot_index = partition(array, low, high)

        # Đệ quy gọi quicksort cho mảng con bên trái và bên phải của pivot
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

    return array


demo_list = [64, 34, 25, 5, 22, 11, 90, 12]
print("Quicksort with Lomuto Partition (In-place implementation):")
quicksort(demo_list)
print(demo_list)


# 4. Phiên bản trực quan bằng List Comprehension (3-Way Partition)
# Ưu điểm: Cực kỳ dễ hiểu, phân tách rõ ràng 3 danh sách: nhỏ hơn, bằng, và lớn hơn Pivot.
# Nhược điểm: Tốn thêm O(n) bộ nhớ phụ cho các danh sách con mới tạo (không phải in-place).
def quicksort_comprehension(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort_comprehension(left) + middle + quicksort_comprehension(right)


comp_demo = [11, 9, 12, 7, 3]
print("\nQuicksort with 3-Way List Comprehension:")
print("Original:", comp_demo)
print("Sorted:  ", quicksort_comprehension(comp_demo))


# 5. Cải tiến tối ưu: Chiến lược chọn Pivot (Median-of-Three)
# Vấn đề của cách chọn phần tử cuối cùng làm Pivot:
# - Nếu mảng đã sắp xếp sẵn (hoặc ngược lại), Pivot luôn là giá trị cực trị (nhỏ nhất hoặc lớn nhất).
# - Cây đệ quy bị lệch hoàn toàn về một phía, dẫn đến độ sâu đệ quy là n, độ phức tạp biến thành O(n^2).
# Giải pháp: Median-of-Three (Lấy trung vị của 3 phần tử: đầu, giữa, cuối).
# - So sánh arr[low], arr[mid], arr[high] và chọn giá trị ở giữa làm pivot, sau đó đổi chỗ nó với arr[high].
# - Giúp Quicksort tránh được trường hợp xấu nhất O(n^2) trên dữ liệu thực tế gần như có thứ tự.
def median_of_three(arr, low, high):
    mid = (low + high) // 2
    # Sắp xếp 3 phần tử arr[low], arr[mid], arr[high]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    # Đổi chỗ trung vị (arr[mid]) với arr[high] để dùng làm pivot
    arr[mid], arr[high] = arr[high], arr[mid]
    return arr[high]


def quicksort_optimized(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Nếu mảng con có từ 3 phần tử trở lên, áp dụng median-of-three
        if high - low >= 2:
            median_of_three(arr, low, high)

        pivot_idx = partition(arr, low, high)
        quicksort_optimized(arr, low, pivot_idx - 1)
        quicksort_optimized(arr, pivot_idx + 1, high)

    return arr


sorted_almost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quicksort_optimized(sorted_almost)
print("\nOptimized Quicksort (Median-of-Three on sorted array):")
print(sorted_almost)


# 6. Minh họa tính KHÔNG ỔN ĐỊNH (Unstable Sort)
# - Quicksort là một thuật toán KHÔNG ỔN ĐỊNH (Unstable) vì các phép hoán đổi khoảng cách xa
#   qua phần tử Pivot có thể làm xáo trộn thứ tự xuất hiện ban đầu của các phần tử bằng nhau.
students = [
    ("Alice", 85),
    ("Bob", 90),
    ("Charlie", 85),
    ("David", 70)
]

# Thực hiện partition trực tiếp dựa trên điểm số
# Chú ý: Việc hoán đổi các phần tử có thể khiến Charlie vượt lên trước Alice dù cùng điểm 85.
print("\nStability note:")
print("Quicksort is NOT stable by default because long-distance swaps can change the relative order of equal keys.")


# 7. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tốt nhất (Best Case): O(n log n). Xảy ra khi mỗi lần chọn Pivot, mảng con được chia đôi hoàn hảo thành 2 nửa bằng nhau.
#   + Trung bình (Average Case): O(n log n). Nhờ cơ chế chia đôi đệ quy, số tầng đệ quy xấp xỉ log2(n), mỗi tầng tốn O(n) duyệt.
#   + Xấu nhất (Worst Case): O(n^2). Xảy ra khi Pivot luôn là phần tử nhỏ nhất hoặc lớn nhất (mảng không được chia đôi mà giảm dần 1 phần tử mỗi lần).
# - Độ phức tạp không gian (Space Complexity):
#   + O(log n) trên Call Stack đệ quy trong trường hợp trung bình.
#   + O(n) Call Stack trong trường hợp xấu nhất nếu không tối ưu đệ quy đuôi (Tail Recursion).
# - So sánh với các thuật toán trước:
#   + Nhanh hơn vượt bậc so với Bubble Sort, Selection Sort, và Insertion Sort (O(n^2)).
#   + Thường nhanh hơn Merge Sort trong thực tế do có hằng số ẩn (Hidden Constant Factor) nhỏ hơn và không cần cấp phát mảng phụ lớn.
