# 6. Algorithms - 2. Sorting: Sắp xếp chọn (Selection Sort)
# Khái niệm thuật toán, mô phỏng từng bước, vấn đề dịch chuyển ô nhớ (Shifting Problem),
# giải pháp hoán đổi (Swapping) và phân tích độ phức tạp O(n^2)
#
# 1. Khái niệm về Sắp xếp chọn (Selection Sort)
# - Thuật toán hoạt động bằng cách liên tục tìm phần tử nhỏ nhất trong phần chưa sắp xếp
#   và đưa nó về đầu phần chưa sắp xếp đó.
# - Nguyên lý hoạt động:
#   + Duyệt qua mảng để tìm giá trị nhỏ nhất.
#   + Đưa giá trị nhỏ nhất đó về đầu đoạn mảng chưa sắp xếp.
#   + Lặp lại quá trình trên cho các đoạn mảng con tiếp theo cho đến khi toàn bộ mảng có thứ tự.

# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: [7, 12, 9, 11, 3]
# - Bước 1-3: Quét tìm giá trị nhỏ nhất trong toàn bộ mảng -> 3 là nhỏ nhất.
#   Đưa 3 về đầu mảng: [3, 7, 12, 9, 11]
# - Bước 4: Xét đoạn còn lại [7, 12, 9, 11]. 7 là nhỏ nhất và đã ở đúng vị trí đầu đoạn:
#   Giữ nguyên: [3, 7, 12, 9, 11]
# - Bước 5-6: Xét đoạn [12, 9, 11]. 9 là nhỏ nhất.
#   Đưa 9 về đầu đoạn: [3, 7, 9, 12, 11]
# - Bước 7-8: Xét đoạn [12, 11]. 11 là nhỏ nhất.
#   Đưa 11 về đầu đoạn: [3, 7, 9, 11, 12]
# -> Kết thúc: Mảng được sắp xếp hoàn chỉnh!


# 3. Vấn đề dịch chuyển ô nhớ trong cài đặt ngây thơ (The Shifting Problem)
# Cách cài đặt ngây thơ thường dùng: `mylist.pop(min_index)` rồi `mylist.insert(i, min_value)`
# Vấn đề hiệu năng nghiêm trọng:
# - pop(min_index) bắt buộc máy tính phải dịch chuyển toàn bộ các phần tử phía sau sang trái một vị trí: O(n).
# - insert(i, min_value) lại phải dịch chuyển toàn bộ các phần tử từ i trở đi sang phải một vị trí: O(n).
# -> Gây ra chi phí dịch chuyển bộ nhớ ngầm (hidden memory shifting) rất đắt đỏ dù code trông ngắn gọn.
def selection_sort_with_shifting(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        # Thao tác gây dồn mảng tốn kém:
        min_val = arr_copy.pop(min_idx)
        arr_copy.insert(i, min_val)
    return arr_copy


demo_list = [64, 34, 25, 5, 22, 11, 90, 12]
print("Selection Sort with shifting (pop & insert):")
print(selection_sort_with_shifting(demo_list))


# 4. Giải pháp tối ưu: Hoán đổi trực tiếp (Solution: Swap Values!)
# Thay vì xóa và chèn làm xô lệch toàn bộ mảng, ta HOÁN ĐỔI trực tiếp phần tử nhỏ nhất với phần tử ở vị trí i:
# arr[i], arr[min_idx] = arr[min_idx], arr[i]
# - Phép hoán đổi đạt O(1) tức thì, hoàn toàn KHÔNG gây ra bất kỳ thao tác dịch chuyển bộ nhớ nào!
def selection_sort(arr, key=None, reverse=False):
    n = len(arr)
    get_key = key if key else (lambda x: x)

    for i in range(n - 1):
        target_idx = i
        for j in range(i + 1, n):
            val_j = get_key(arr[j])
            val_target = get_key(arr[target_idx])
            if (val_j > val_target) if reverse else (val_j < val_target):
                target_idx = j

        # Chỉ hoán đổi khi tìm thấy vị trí mới khác i
        if target_idx != i:
            arr[i], arr[target_idx] = arr[target_idx], arr[i]

    return arr


# Thử nghiệm với mảng mẫu:
sample_list = [64, 34, 25, 12, 22, 11, 90, 5]
print("\nImproved Selection Sort with Swapping:")
selection_sort(sample_list)
print(sample_list)  # [5, 11, 12, 22, 25, 34, 64, 90]


# 5. Biến thể tối ưu hai chiều (Bidirectional Selection Sort / Min-Max Sort)
# Tìm đồng thời cả phần tử nhỏ nhất (Min) và lớn nhất (Max) trong mỗi vòng quét:
# - Đưa Min về đầu (left), đưa Max về cuối (right), giảm số vòng quét xuống còn n / 2.
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

        # Đưa Min về vị trí left
        if min_idx != left:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            # Nếu vị trí left ban đầu chính là max_idx, nó đã bị tráo sang min_idx
            if max_idx == left:
                max_idx = min_idx

        # Đưa Max về vị trí right
        if max_idx != right:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]

        left += 1
        right -= 1

    return arr


two_way_list = [29, 10, 14, 37, 13, 25, 8]
print("\nBidirectional Selection Sort:")
bidirectional_selection_sort(two_way_list)
print(two_way_list)


# 6. Minh họa tính không ổn định (Unstable Sort)
# Selection Sort là thuật toán KHÔNG ỔN ĐỊNH do phép hoán đổi tầm xa.
# Ví dụ: Phần tử ('A', 4) đứng trước ('B', 4). Khi hoán đổi 4 với 2 ở xa,
# ('A', 4) bị nhảy ra sau ('B', 4), làm thay đổi thứ tự tương đối ban đầu của các phần tử bằng nhau.
items = [("A", 4), ("B", 4), ("C", 2)]
print("\nStability Demonstration:")
print("Before sort:", items)
selection_sort(items, key=lambda x: x[1])
print("After sort: ", items)
print("-> ('B', 4) appears before ('A', 4) => Unstable!")


# 7. Phân tích độ phức tạp thuật toán (Time & Space Complexity)
# - Thời gian (Time Complexity):
#   + Số phép so sánh luôn là: (n - 1) + (n - 2) + ... + 1 = n*(n - 1) / 2 ≈ O(n^2).
#   + Worst Case: O(n^2)
#   + Average Case: O(n^2)
#   + Best Case: O(n^2) (ngay cả khi mảng đã sắp xếp sẵn, thuật toán vẫn phải quét tìm Min ở đoạn sau).
# - Điểm mạnh hiếm hoi: Số lần hoán đổi (swaps/writes) tối đa chỉ là O(n) (chính xác tối đa n - 1 lần).
#   Rất hữu ích khi chi phí ghi dữ liệu lên bộ nhớ đắt đỏ (như Flash memory, EEPROM).
# - Không gian (Space Complexity): O(1) - Sắp xếp tại chỗ (In-place).
print("\nSelection Sort Complexity Summary:")
print("- Time: Worst O(n^2), Average O(n^2), Best O(n^2)")
print("- Swaps: Maximum n - 1 swaps (very few swaps compared to Bubble Sort)")
print("- Space: O(1) (In-place)")
print("- Stability: Unstable")
