# * [BỔ SUNG NÂNG CAO] Quick Sort & Python Timsort (sort với key=lambda)

from typing import Optional

# Thuật toán Quick Sort (Divide and Conquer - Chia để trị):
# - Chuẩn công nghiệp: Phân hoạch tại chỗ (In-place Partition - Lomuto/Hoare), Space O(log n)
# - Tránh cách viết [x for x in arr] vì tốn O(n) bộ nhớ phụ ở mỗi tầng đệ quy!
def quick_sort_inplace(arr: list[int], low: int = 0, high: Optional[int] = None) -> list[int]:
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Phân hoạch Lomuto
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

nums = [33, 10, 55, 71, 29, 10]
print("Quick Sort (In-place):", quick_sort_inplace(nums)) # [10, 10, 29, 33, 55, 71]


# Python Built-in Sort (Timsort - O(n log n) tối ưu trong thực tế)
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sắp xếp danh sách tuple theo điểm số tăng dần bằng key=lambda
students.sort(key=lambda s: s[1])
print("Sorted by score:", students)
