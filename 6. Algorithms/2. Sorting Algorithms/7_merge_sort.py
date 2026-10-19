# 6. Algorithms - 2. Sorting: Sắp xếp trộn (Merge Sort)
# Khái niệm thuật toán, phương pháp Chia để trị (Divide and Conquer), mô phỏng từng bước (Manual Run Through),
# cài đặt đệ quy, cài đặt không đệ quy (Iterative Bottom-up), tính ổn định và phân tích độ phức tạp

# 1. Khái niệm về Thuật toán Merge Sort
# - Merge Sort là thuật toán sắp xếp kinh điển theo mô hình "Chia để trị" (Divide and Conquer).
# - Nguyên lý hoạt động gồm 2 pha chính:
#   + Chia (Divide): Chia mảng thành 2 nửa bằng nhau arr[:mid] và arr[mid:].
#     Tiếp tục chia nhỏ các mảng con bằng đệ quy cho đến khi mỗi mảng con chỉ còn duy nhất 1 phần tử
#     (mảng 1 phần tử thì luôn luôn được coi là đã có thứ tự).
#   + Trị / Trộn (Conquer & Merge): Trộn (ghép) hai mảng con đã có thứ tự lại với nhau thành một mảng lớn hơn,
#     bằng cách so sánh lần lượt các phần tử từ đầu mỗi mảng con và lấy phần tử nhỏ hơn đặt vào mảng kết quả.
#   + Quá trình trộn tiếp diễn cho đến khi toàn bộ mảng ban đầu được phục hồi hoàn chỉnh theo thứ tự tăng dần.


# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Dãy ban đầu: [12, 8, 9, 3, 11, 5, 4]
# - Bước 1: Tách đôi thành [12, 8, 9] và [3, 11, 5, 4].
#   Xét nửa bên trái [12, 8, 9]:
#   + Tách tiếp thành [12] và [8, 9] -> [12], [8], [9].
# - Bước 2: Trộn [8] và [9] -> [8, 9].
# - Bước 3: Trộn [12] với [8, 9]:
#   + So sánh 12 với 8 -> lấy 8
#   + So sánh 12 với 9 -> lấy 9
#   + Còn lại 12 -> lấy 12
#   -> Nửa trái đã sắp xếp: [8, 9, 12].
# - Bước 4-6: Xét nửa bên phải [3, 11, 5, 4]:
#   + Tách thành [3, 11] và [5, 4] -> [3], [11], [5], [4].
#   + Trộn [3] và [11] -> [3, 11].
#   + Trộn [5] và [4] -> [4, 5].
# - Bước 7: Trộn [3, 11] với [4, 5]:
#   + So sánh 3 với 4 -> lấy 3
#   + So sánh 11 với 4 -> lấy 4
#   + So sánh 11 với 5 -> lấy 5
#   + Còn lại 11 -> lấy 11
#   -> Nửa phải đã sắp xếp: [3, 4, 5, 11].
# - Bước 8-12: Trộn 2 nửa lớn [8, 9, 12] và [3, 4, 5, 11]:
#   + So sánh 8 với 3 -> lấy 3
#   + So sánh 8 với 4 -> lấy 4
#   + So sánh 8 với 5 -> lấy 5
#   + So sánh 8 với 11 -> lấy 8
#   + So sánh 9 với 11 -> lấy 9
#   + So sánh 12 với 11 -> lấy 11
#   + Còn lại 12 -> lấy 12
#   -> Mảng kết quả cuối cùng: [3, 4, 5, 8, 9, 11, 12]!


# 3. Cài đặt Merge Sort đệ quy kinh điển (Recursive Implementation)
# Hàm merge nhận 2 mảng con đã sắp xếp và trộn lại:
def merge(left, right):
    result = []
    i = j = 0

    # So sánh từng cặp phần tử từ 2 mảng con
    # Lưu ý: Bắt buộc dùng '<=' thay vì '<' để đảm bảo tính ỔN ĐỊNH (Stable Sort)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Nối các phần tử còn dư của mảng con chưa duyệt hết
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    # Điều kiện dừng của đệ quy: mảng có 0 hoặc 1 phần tử
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Đệ quy chia nhỏ và sắp xếp từng nửa
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Trộn 2 nửa đã sắp xếp lại với nhau
    return merge(sorted_left, sorted_right)


sample_array = [3, 7, 6, -10, 15, 23.5, 55, -13]
print("Recursive Merge Sort result:")
print("Original:", [3, 7, 6, -10, 15, 23.5, 55, -13])
print("Sorted:  ", merge_sort(sample_array))


# 4. Cài đặt Merge Sort không đệ quy (Iterative / Bottom-Up Merge Sort)
# Thay vì chia từ trên xuống bằng đệ quy (Top-down), ta bắt đầu từ dưới lên (Bottom-up):
# - Bắt đầu với các mảng con kích thước step = 1 (mỗi phần tử là 1 mảng con đã có thứ tự).
# - Trộn từng cặp kề nhau thành mảng con kích thước 2.
# - Sau đó nhân đôi step *= 2 (trộn các mảng con kích thước 2 thành 4, rồi 4 thành 8, ...).
# - Ưu điểm: Hoàn toàn không tốn bộ nhớ Call Stack đệ quy, tránh được lỗi RecursionError trên dữ liệu lớn.
def merge_sort_iterative(arr):
    step = 1
    n = len(arr)

    while step < n:
        for i in range(0, n, 2 * step):
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]
            merged = merge(left, right)

            # Cập nhật kết quả đã trộn ngược lại vào mảng gốc
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2

    return arr


iterative_demo = [12, 8, 9, 3, 11, 5, 4]
print("\nIterative (Bottom-Up) Merge Sort:")
print("Original:", [12, 8, 9, 3, 11, 5, 4])
merge_sort_iterative(iterative_demo)
print("Sorted:  ", iterative_demo)


# 5. Cài đặt chuẩn công nghiệp: In-place Mutation hỗ trợ tham số key và reverse
# Tương tự như hàm sorted() và list.sort() trong thư viện chuẩn Python.
def merge_sort_custom(arr, key=None, reverse=False):
    if len(arr) <= 1:
        return arr

    get_key = key if key else (lambda x: x)

    def sort_internal(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr

        mid = len(sub_arr) // 2
        left = sort_internal(sub_arr[:mid])
        right = sort_internal(sub_arr[mid:])

        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            key_left = get_key(left[i])
            key_right = get_key(right[j])

            # Khi reverse=False: ưu tiên phần tử nhỏ hơn hoặc bằng
            # Khi reverse=True: ưu tiên phần tử lớn hơn hoặc bằng
            condition = (key_left >= key_right) if reverse else (key_left <= key_right)
            if condition:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return sort_internal(arr)


# 6. Minh họa tính ỔN ĐỊNH (Stable Sort) với dữ liệu thực tế
# Merge Sort là thuật toán sắp xếp ỔN ĐỊNH vì khi 2 phần tử có cùng giá trị khóa,
# điều kiện `<=` đảm bảo phần tử từ mảng con bên trái (xuất hiện trước) luôn được lấy trước.
students = [
    ("David", 92),
    ("Alice", 85),
    ("Bob", 78),
    ("Charlie", 85)
]

sorted_students = merge_sort_custom(students, key=lambda s: s[1])
print("\nStable Sort demonstration with student grades:")
for name, grade in sorted_students:
    print(f"  {name}: {grade}")
# Kết quả: Alice (85) vẫn đứng trước Charlie (85) chuẩn theo thứ tự ban đầu!


# 7. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tất cả các trường hợp (Best, Average, Worst): LUÔN LÀ O(n log n).
#   + Phương trình đệ quy: T(n) = 2 * T(n / 2) + O(n). Theo Định lý thợ (Master Theorem), T(n) = O(n log n).
#   + Dù mảng đã sắp xếp, ngẫu nhiên hay đảo ngược, thuật toán vẫn luôn thực hiện đúng số bước chia và trộn.
# - Độ phức tạp không gian (Space Complexity):
#   + O(n) bộ nhớ phụ để lưu trữ các mảng con trong quá trình trộn.
# - So sánh với Quicksort:
#   + Điểm mạnh của Merge Sort: Hiệu năng cực kỳ ổn định (không bao giờ bị suy biến thành O(n^2) như Quicksort),
#     bảo toàn tính ổn định (Stable Sort), cực kỳ phù hợp cho Linked Lists và sắp xếp dữ liệu ngoài (External Sorting).
#   + Điểm yếu của Merge Sort: Tốn thêm O(n) bộ nhớ RAM phụ (Quicksort chạy in-place chỉ tốn O(log n) Call Stack).
