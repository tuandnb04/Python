# Thuật toán Merge Sort (Chia để trị - Divide and Conquer)
# - Thời gian: Luôn là O(n log n) trong mọi trường hợp (Best, Average, Worst).
# - Không gian: O(n) bộ nhớ phụ (slicing và mảng con).
# - Đặc tính: Stable Sort (bảo toàn thứ tự ban đầu của các phần tử bằng nhau).


def merge_sort(arr, key=None):
    """
    Sắp xếp Merge Sort thay đổi trực tiếp mảng gốc (In-place mutation).
    Hỗ trợ tham số key để sắp xếp tùy biến (tương tự list.sort).
    """
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key=key)
    merge_sort(right, key=key)

    i = j = k = 0
    get_key = key if key else (lambda x: x)

    # ĐIỂM MẤU CHỐT CỦA TÍNH ỔN ĐỊNH (STABILITY):
    # Bắt buộc dùng '<=' thay vì '<' để khi 2 phần tử bằng nhau,
    # phần tử bên mảng left (xuất hiện trước) luôn được ưu tiên lấy trước.
    while i < len(left) and j < len(right):
        if get_key(left[i]) <= get_key(right[j]):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    # 1. Sắp xếp số cơ bản (In-place)
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print("Original numbers:", numbers)
    merge_sort(numbers)
    print("Sorted numbers:  ", numbers)

    # 2. Minh họa tính Ổn định (Stable Sort) bằng tham số key
    # Alice (85) đứng trước Charlie (85), sau khi sort Alice vẫn đứng trước Charlie
    students = [("David", 92), ("Alice", 85), ("Bob", 78), ("Charlie", 85)]
    merge_sort(students, key=lambda s: s[1])
    print("Stable sort:     ", students)

    # 3. So sánh chuyên sâu & Python Timsort:
    # - Merge Sort: Luôn O(n log n), Stable, tốn O(n) RAM -> Phù hợp Linked List, External Sorting.
    # - Quick Sort: Trung bình O(n log n), Unstable, In-place O(log n) RAM -> Phù hợp mảng trong bộ nhớ.
    # - Python Timsort (sorted, list.sort): Kết hợp Merge Sort + Insertion Sort.
