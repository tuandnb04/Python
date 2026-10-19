# 6. Algorithms - 2. Sorting: Sắp xếp nổi bọt (Bubble Sort)
# Khái niệm thuật toán, mô phỏng từng bước, cài đặt cơ bản, cải tiến dừng sớm và phân tích độ phức tạp
#
# 1. Khái niệm về Sắp xếp nổi bọt (Bubble Sort)
# - Là thuật toán sắp xếp mảng theo thứ tự từ nhỏ đến lớn bằng cách so sánh từng cặp phần tử liền kề.
# - Nguồn gốc tên gọi "Bubble" (Nổi bọt): Sau mỗi lượt duyệt mảng, phần tử lớn nhất trong phạm vi chưa sắp xếp
#   sẽ dần dần "nổi bọt" (chuyển dịch) về vị trí cuối cùng của mảng.
# - Nguyên lý hoạt động:
#   + Đi qua mảng lần lượt từng phần tử.
#   + So sánh phần tử hiện tại với phần tử kế tiếp ngay sau nó.
#   + Nếu phần tử đứng trước lớn hơn phần tử đứng sau, hoán đổi vị trí của chúng.
#   + Lặp lại quá trình trên cho đến khi toàn bộ mảng được sắp xếp hoàn chỉnh.

# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: [7, 12, 9, 11, 3]
# - Lượt duyệt 1 (Pass 1):
#   + So sánh 7 và 12: 7 < 12, không đổi chỗ       -> [7, 12, 9, 11, 3]
#   + So sánh 12 và 9: 12 > 9, đổi chỗ 12 và 9     -> [7, 9, 12, 11, 3]
#   + So sánh 12 và 11: 12 > 11, đổi chỗ 12 và 11 -> [7, 9, 11, 12, 3]
#   + So sánh 12 và 3: 12 > 3, đổi chỗ 12 và 3     -> [7, 9, 11, 3, 12]
#   -> Kết thúc lượt 1: Số lớn nhất là 12 đã nổi về đúng vị trí cuối cùng!
# - Lặp lại các lượt tiếp theo cho đến khi không còn hoán đổi nào.


# 3. Cài đặt Bubble Sort cơ bản (Basic Bubble Sort)
# Mảng mẫu minh họa:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(mylist)

for i in range(n - 1):
    # Mỗi lần lặp ngoài, phần tử lớn nhất đã nằm ở cuối nên vòng lặp trong giảm đi i phần tử
    for j in range(n - i - 1):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]

print("Basic Bubble Sort result:")
print(mylist)  # [5, 11, 12, 22, 25, 34, 64, 90]


# 4. Cải tiến thuật toán với cờ 'swapped' (Bubble Sort Improvement / Early Exit)
# Vấn đề: Với mảng gần như đã sắp xếp sẵn (ví dụ [7, 3, 9, 12, 11]), sau 1 lượt duyệt mảng đã xong.
# Nếu không tối ưu, thuật toán cơ bản vẫn tiếp tục lặp đủ n - 1 lượt không cần thiết.
# Giải pháp: Thêm biến cờ `swapped`. Nếu sau một lượt duyệt vòng trong mà không có hoán đổi nào xảy ra,
# chứng tỏ mảng đã hoàn toàn có thứ tự -> dừng vòng lặp ngay lập tức (`break`).
almost_sorted = [7, 3, 9, 12, 11]
n_opt = len(almost_sorted)

for i in range(n_opt - 1):
    swapped = False
    for j in range(n_opt - i - 1):
        if almost_sorted[j] > almost_sorted[j + 1]:
            almost_sorted[j], almost_sorted[j + 1] = almost_sorted[j + 1], almost_sorted[j]
            swapped = True
    # Nếu không có phép hoán đổi nào xảy ra trong lượt này, dừng thuật toán sớm
    if not swapped:
        print(f"Early exit triggered at pass {i + 1}!")
        break

print("\nImproved Bubble Sort result:")
print(almost_sorted)  # [3, 7, 9, 11, 12]


# 5. Đóng gói hàm tái sử dụng chuẩn hóa (Reusable Function)
def bubble_sort(arr):
    arr_copy = arr.copy()
    n_len = len(arr_copy)
    total_passes = 0
    total_swaps = 0

    for i in range(n_len - 1):
        swapped = False
        total_passes += 1
        for j in range(n_len - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
                total_swaps += 1
        if not swapped:
            break

    return arr_copy, total_passes, total_swaps


test_list = [7, 12, 9, 11, 3]
sorted_res, passes, swaps = bubble_sort(test_list)
print(f"\nSorting {test_list}:")
print(f"Sorted array: {sorted_res}")
print(f"Passes taken: {passes}, Total swaps: {swaps}")


# 6. Phân tích độ phức tạp thuật toán (Time & Space Complexity)
# - Thời gian (Time Complexity):
#   + Worst Case: O(n^2) - Khi mảng ban đầu được sắp xếp ngược chiều hoàn toàn.
#   + Average Case: O(n^2) - Trung bình cần n*(n-1)/2 phép so sánh.
#   + Best Case: O(n) - Khi mảng đã được sắp xếp sẵn từ trước (nhờ cờ `swapped` dừng ngay sau 1 lượt).
# - Không gian (Space Complexity): O(1) - Thuật toán sắp xếp tại chỗ (In-place sort).
# - Tính ổn định (Stability): Là thuật toán ổn định (Stable Sort), vì hai phần tử bằng nhau
#   không bao giờ bị hoán đổi vị trí (chỉ hoán đổi khi arr[j] > arr[j+1]).
print("\nBubble Sort Complexity Summary:")
print("- Time: Worst O(n^2), Average O(n^2), Best O(n)")
print("- Space: O(1) (In-place)")
print("- Stability: Stable")
