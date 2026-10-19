# 6. Algorithms - 2. Sorting - Extra: Sắp xếp vun đống (Heap Sort)
# Khái niệm thuật toán, cấu trúc Max-Heap (liên kết với Chương 5 Heap), hàm Heapify,
# quy trình sắp xếp tại chỗ in-place O(1) bộ nhớ phụ và phân tích độ phức tạp O(n log n)

# 1. Khái niệm về Thuật toán Heap Sort
# - Heap Sort là thuật toán sắp xếp dựa trên cấu trúc dữ liệu Cây nhị phân hoàn chỉnh (Binary Heap).
# - Liên kết kiến thức: Áp dụng trực tiếp cấu trúc Max-Heap đã học tại [5_heaps.py](file:///c:/Users/ASUS/Desktop/python-projects/5.%20Data%20Structures/Core/5_heaps.py):
#   + Trong Max-Heap, phần tử lớn nhất luôn nằm tại đỉnh (gốc cây, chỉ số 0).
#   + Nút cha tại chỉ số i có con trái tại 2*i + 1 và con phải tại 2*i + 2.
# - Nguyên lý hoạt động:
#   + Bước 1 (Build Max-Heap): Biến đổi mảng ban đầu thành một Max-Heap trong thời gian O(n).
#   + Bước 2 (Extract Max & Swap):
#     * Đổi chỗ phần tử lớn nhất tại đỉnh arr[0] với phần tử cuối cùng của Heap arr[i].
#     * Giảm kích thước Heap đi 1 (phần tử lớn nhất vừa hoán đổi đã nằm đúng vị trí cuối mảng).
#     * Gọi hàm `heapify` để khôi phục tính chất Max-Heap cho đỉnh arr[0].
#   + Lặp lại bước 2 cho đến khi kích thước Heap giảm về 1.


# 2. Hàm vun đống (Heapify)
# Điều chỉnh cây con có gốc tại chỉ số i sao cho thỏa mãn tính chất Max-Heap trong phạm vi n phần tử:
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Kiểm tra nếu con trái tồn tại và lớn hơn nút gốc
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Kiểm tra nếu con phải tồn tại và lớn hơn nút lớn nhất hiện tại
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Nếu nút lớn nhất không phải là nút gốc ban đầu, hoán đổi và tiếp tục vun đống đệ quy
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# 3. Cài đặt Heap Sort tại chỗ (In-place Heap Sort)
def heap_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # Bước 1: Xây dựng Max-Heap từ mảng ban đầu
    # Duyệt từ nút không phải lá cuối cùng (n // 2 - 1) ngược về nút gốc (0)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Bước 2: Lần lượt trích xuất từng phần tử lớn nhất ra cuối mảng
    for i in range(n - 1, 0, -1):
        # Đưa phần tử lớn nhất arr[0] về cuối đoạn chưa sắp xếp arr[i]
        arr[0], arr[i] = arr[i], arr[0]

        # Khôi phục tính chất Max-Heap cho đoạn mảng còn lại có kích thước i
        heapify(arr, i, 0)

    return arr


# 4. Thử nghiệm thực tế
numbers_sample = [64, 34, 25, 12, 22, 11, 90, 5, 80, 45]
print("Heap Sort In-Place demonstration:")
print("Original:", [64, 34, 25, 12, 22, 11, 90, 5, 80, 45])
heap_sort(numbers_sample)
print("Sorted:  ", numbers_sample)


# 5. Minh họa tính KHÔNG ỔN ĐỊNH (Unstable Sort)
# Heap Sort là thuật toán KHÔNG ỔN ĐỊNH vì các phép hoán đổi từ đỉnh heap về cuối mảng
# và thao tác sàng lọc trong Heapify làm thay đổi thứ tự ban đầu của các phần tử bằng nhau.
items = [
    ("Book A", 20),
    ("Book B", 50),
    ("Book C", 20),
    ("Book D", 10)
]

# Tùy biến heap_sort theo khóa:
def heap_sort_by_key(arr, key_func):
    n = len(arr)

    def heapify_custom(size, root_idx):
        largest_idx = root_idx
        l = 2 * root_idx + 1
        r = 2 * root_idx + 2

        if l < size and key_func(arr[l]) > key_func(arr[largest_idx]):
            largest_idx = l
        if r < size and key_func(arr[r]) > key_func(arr[largest_idx]):
            largest_idx = r
        if largest_idx != root_idx:
            arr[root_idx], arr[largest_idx] = arr[largest_idx], arr[root_idx]
            heapify_custom(size, largest_idx)

    for i in range(n // 2 - 1, -1, -1):
        heapify_custom(n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_custom(i, 0)
    return arr


heap_sort_by_key(items, key_func=lambda x: x[1])
print("\nUnstable demonstration with duplicate prices:")
for title, price in items:
    print(f"  {title}: {price}")


# 6. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Xây dựng Max-Heap: O(n).
#   + n - 1 lần trích xuất và heapify: (n - 1) * O(log n) = O(n log n).
#   + Tổng thời gian: LUÔN LÀ O(n log n) trong mọi trường hợp (Best, Average, Worst).
# - Độ phức tạp không gian (Space Complexity):
#   + O(1) bộ nhớ phụ tuyệt đối vì toàn bộ quá trình biến đổi và hoán đổi diễn ra trực tiếp trên mảng gốc (In-place).
# - So sánh ba thuật toán O(n log n) kinh điển:
#   + Quicksort: Nhanh nhất trên thực tế, nhưng tốn O(log n) stack đệ quy và có nguy cơ suy biến O(n^2).
#   + Merge Sort: Thời gian O(n log n) bảo đảm và ổn định (Stable), nhưng tốn O(n) bộ nhớ phụ.
#   + Heap Sort: Thời gian O(n log n) bảo đảm VÀ bộ nhớ phụ chỉ O(1), rất phù hợp cho hệ thống nhúng (Embedded Systems) bị giới hạn RAM nghiêm ngặt.
