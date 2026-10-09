# Thuật toán Insertion Sort (Sắp xếp chèn)
# - Ý tưởng: Tương tự như cách ta xếp các lá bài trên tay.
#   Duyệt từ phần tử thứ 2, chèn phần tử hiện tại vào đúng vị trí trong dãy con đã sắp xếp phía trước.
# - Độ phức tạp thời gian:
#   + Best case: O(n) khi mảng đã sắp xếp hoặc gần như sắp xếp (Nearly sorted).
#   + Average / Worst case: O(n^2) khi mảng ngẫu nhiên hoặc đảo ngược.
# - Độ phức tạp không gian: O(1) phụ trợ (In-place).
# - Tính ổn định: STABLE (Ổn định - bảo toàn thứ tự ban đầu của các phần tử bằng nhau).
# - Ứng dụng thực tế:
#   + Cực kỳ nhanh với dữ liệu kích thước nhỏ (n <= 32 hoặc 64).
#   + Là thành phần cốt lõi của Timsort (thuật toán sắp xếp mặc định của Python và Java).
#   + Thích hợp cho Online Sorting (dữ liệu đến dạng streaming theo thời gian thực).

from bisect import bisect_right


def insertion_sort(arr, key=None):
    """
    Sắp xếp chèn in-place, hỗ trợ tham số key.
    """
    n = len(arr)
    get_key = key if key else (lambda x: x)

    for i in range(1, n):
        current_val = arr[i]
        current_key = get_key(current_val)
        j = i - 1

        # Dời các phần tử lớn hơn về sau 1 vị trí
        # Dùng '>' thay vì '>=' để đảm bảo tính ổn định (Stable)
        while j >= 0 and get_key(arr[j]) > current_key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_val

    return arr


def binary_insertion_sort(arr):
    """
    Biến thể dùng Binary Search để giảm số phép so sánh từ O(n^2) xuống O(n log n).
    (Số phép dịch chuyển phần tử vẫn là O(n^2)).
    Đây chính là kỹ thuật được Timsort áp dụng cho các mảng con nhỏ!
    """
    for i in range(1, len(arr)):
        val = arr[i]
        # Tìm vị trí chèn trong mảng con đã sắp xếp arr[0:i] bằng Binary Search
        pos = bisect_right(arr, val, 0, i)
        
        # Dời các phần tử từ pos đến i - 1 sang phải một nấc
        arr[pos + 1 : i + 1] = arr[pos:i]
        arr[pos] = val

    return arr


if __name__ == "__main__":
    # 1. Thử nghiệm cơ bản
    nums = [12, 11, 13, 5, 6]
    print("Original:                         ", nums)
    insertion_sort(nums)
    print("Sorted (Insertion Sort):          ", nums)

    # 2. Thử nghiệm Binary Insertion Sort
    nums2 = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
    binary_insertion_sort(nums2)
    print("Sorted (Binary Insertion Sort):   ", nums2)

    # 3. Minh họa tính ỔN ĐỊNH (Stable Sort)
    students = [("David", 92), ("Alice", 85), ("Bob", 78), ("Charlie", 85)]
    insertion_sort(students, key=lambda s: s[1])
    print("\nStable Sort demonstration:")
    print("Sorted students:                  ", students)
    print("-> Alice (85) preserves position before Charlie (85)")

