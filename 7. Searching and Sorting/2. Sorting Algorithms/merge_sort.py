# Thuật toán Merge Sort theo tư tưởng Divide and Conquer (Chia để trị)
# - Độ phức tạp thời gian: O(n log n)
# - Độ phức tạp không gian: O(n) (không phải in-place, cần bộ nhớ phụ để trộn)

def merge_sort(arr):
    # Base case: Mảng có 0 hoặc 1 phần tử đã được sắp xếp sẵn
    if len(arr) <= 1:
        return arr

    # 1. Divide: Chia mảng thành 2 nửa
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 2. Conquer / Merge: Trộn 2 nửa đã sắp xếp
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

numbers = [42, 37, 53, 17]
print("Original:", numbers)
print("Merge Sort:", merge_sort(numbers)) # [17, 37, 42, 53]
