# Thuật toán Merge Sort theo tư tưởng Divide and Conquer (Chia để trị)
# - Độ phức tạp thời gian: O(n log n)
# - Độ phức tạp không gian: O(n) (không phải in-place, cần bộ nhớ phụ để trộn)

def merge_sort(arr: list[int]) -> list[int]:
    # Base case: Mảng có 0 hoặc 1 phần tử đã được sắp xếp sẵn
    if len(arr) <= 1:
        return arr

    # Divide: Chia mảng thành 2 nửa
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer / Merge: Trộn 2 nửa đã sắp xếp
    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

numbers = [42, 37, 53, 17]
print("Original:", numbers)
print("Merge Sort:", merge_sort(numbers)) # [17, 37, 42, 53]
