# Thuật toán Quick Sort (Chia để trị - Divide and Conquer)
# - Độ phức tạp: Trung bình O(n log n), xấu nhất O(n^2).


# 1. Cách viết Pythonic (Dễ hiểu, 3-way partition nhưng tốn O(n) bộ nhớ phụ)
def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# 2. Cách viết In-place chuẩn công nghiệp (Lomuto Partition - Tiết kiệm RAM O(log n))
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        pivot_idx = i

        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    return arr


if __name__ == "__main__":
    nums1 = [33, 10, 55, 71, 29, 10]
    nums2 = nums1.copy()

    print("Original:             ", nums1)
    print("Quick Sort (Pythonic):", quick_sort(nums1))

    quick_sort_inplace(nums2)
    print("Quick Sort (In-place):", nums2)
