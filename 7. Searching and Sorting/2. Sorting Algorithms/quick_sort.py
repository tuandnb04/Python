# * [BỔ SUNG NÂNG CAO] Quick Sort & Python Timsort (sort với key=lambda)

# 1. Thuật toán Quick Sort (Divide and Conquer - Chia để trị)
# - Chọn 1 phần tử làm Pivot (chốt)
# - Phân hoạch: nhỏ hơn pivot sang trái, lớn hơn pivot sang phải
# - Độ phức tạp: Trung bình O(n log n), Xấu nhất O(n^2) nếu chọn pivot kém
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

nums = [33, 10, 55, 71, 29, 10]
print("Quick Sort:", quick_sort(nums)) # [10, 10, 29, 33, 55, 71]

# 2. Python Built-in Sort (Timsort - O(n log n) tối ưu trong thực tế)
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
# Sắp xếp danh sách tuple theo điểm số tăng dần bằng key=lambda
students.sort(key=lambda s: s[1])
print("Sorted by score:", students)
