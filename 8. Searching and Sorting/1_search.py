# 1. Linear Search (Tìm kiếm tuyến tính) - O(n) thời gian, O(1) không gian
# - Không yêu cầu mảng phải được sắp xếp
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

unsorted_list = [13, 4, 7, 9, 10]
print("Linear search (find 9):", linear_search(unsorted_list, 9))   # 3
print("Linear search (find 5):", linear_search(unsorted_list, 5))   # -1

# 2. Binary Search (Tìm kiếm nhị phân) - O(log n) thời gian, O(1) không gian
# - ĐIỀU KIỆN BẮT BUỘC: Danh sách phải được sắp xếp tăng dần!
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1      # Tìm tiếp ở nửa bên phải
        else:
            high = mid - 1     # Tìm tiếp ở nửa bên trái

    return -1                  # Trả về -1 nếu không tìm thấy

sorted_list = [4, 7, 9, 10, 13]
print("Binary search (find 9):", binary_search(sorted_list, 9))     # 2
print("Binary search (find 5):", binary_search(sorted_list, 5))     # -1
