# Thuật toán Selection Sort (Sắp xếp chọn)
# - Ý tưởng: Tại mỗi bước i, tìm phần tử nhỏ nhất trong đoạn [i, n-1] rồi hoán đổi về vị trí i.
# - Độ phức tạp thời gian: O(n^2) trong MỌI trường hợp (Best, Average, Worst).
# - Độ phức tạp không gian: O(1) phụ trợ (In-place).
# - Tính ổn định: UNSTABLE (Không ổn định - do phép hoán đổi tầm xa).
# - Điểm mạnh hiếm hoi: Số lần hoán đổi (swaps/writes) tối đa là O(n) (n - 1 lần),
#   rất tối ưu trên các bộ nhớ có chi phí ghi đắt đỏ (EEPROM, Flash memory).


def selection_sort(arr, key=None, reverse=False):
    """
    Sắp xếp chọn in-place, hỗ trợ tham số key và reverse.
    """
    n = len(arr)
    get_key = key if key else (lambda x: x)

    for i in range(n - 1):
        target_idx = i

        for j in range(i + 1, n):
            val_j = get_key(arr[j])
            val_target = get_key(arr[target_idx])

            if (val_j > val_target) if reverse else (val_j < val_target):
                target_idx = j

        # Chỉ swap khi vị trí thay đổi (tiết kiệm số phép gán)
        if target_idx != i:
            arr[i], arr[target_idx] = arr[target_idx], arr[i]

    return arr


# Biến thể tối ưu: Tìm đồng thời cả Min và Max trong mỗi vòng lặp (Cocktail/Bidirectional Selection Sort)
def bidirectional_selection_sort(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        min_idx = left
        max_idx = left

        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i

        # Đưa phần tử nhỏ nhất về vị trí left
        if min_idx != left:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            # Nếu max_idx từng nằm ở vị trí left, nó vừa bị dời sang min_idx
            if max_idx == left:
                max_idx = min_idx

        # Đưa phần tử lớn nhất về vị trí right
        if max_idx != right:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]

        left += 1
        right -= 1

    return arr


if __name__ == "__main__":
    # 1. Thử nghiệm cơ bản
    nums = [64, 25, 12, 22, 11]
    print("Original:                  ", nums)
    selection_sort(nums)
    print("Sorted (Selection Sort):   ", nums)

    # 2. Thử nghiệm Bidirectional Selection Sort
    nums2 = [29, 10, 14, 37, 13, 25, 8]
    print("\nOriginal 2:                ", nums2)
    bidirectional_selection_sort(nums2)
    print("Sorted (Bidirectional):    ", nums2)

    # 3. Minh họa tính KHÔNG ỔN ĐỊNH (Unstable)
    # Phần tử ('A', 4) ban đầu đứng trước ('B', 4) nhưng bị nhảy ra sau khi swap với ('C', 2)
    items = [("A", 4), ("B", 4), ("C", 2)]
    print("\nBefore sort:               ", items)
    selection_sort(items, key=lambda x: x[1])
    print("After sort:                ", items)
    print("-> ('B', 4) now appears before ('A', 4) => Unstable!")

