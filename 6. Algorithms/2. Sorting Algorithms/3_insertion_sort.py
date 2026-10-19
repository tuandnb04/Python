# 6. Algorithms - 2. Sorting: Sắp xếp chèn (Insertion Sort)
# Khái niệm thuật toán, mô phỏng từng bước (xếp bài), vấn đề dịch chuyển ô nhớ (Shifting Problem),
# giải pháp dịch chuyển tại chỗ (In-place Shifting), tối ưu Binary Insertion Sort và phân tích độ phức tạp

# 1. Khái niệm về Sắp xếp chèn (Insertion Sort)
# - Ý tưởng hoạt động: Chia mảng thành 2 phần:
#   + Phần bên trái: Đã được sắp xếp (ban đầu chỉ gồm 1 phần tử đầu tiên arr[0], 1 phần tử thì luôn có thứ tự).
#   + Phần bên phải: Chưa được sắp xếp (các phần tử từ arr[1] đến cuối).
# - Tương tự như cách sắp xếp các lá bài tây trên tay:
#   + Bạn cầm các lá bài đã xếp gọn ở tay trái.
#   + Lần lượt rút từng lá bài từ phần chưa xếp, tìm đúng vị trí phù hợp trong các lá đã xếp và "chèn" vào.
# - Nguyên lý hoạt động:
#   + Lấy phần tử đầu tiên của phần chưa sắp xếp.
#   + Duyệt ngược từ cuối phần đã sắp xếp về đầu để tìm vị trí thích hợp cho phần tử đó.
#   + Đặt phần tử vào đúng vị trí trong phần đã sắp xếp.
#   + Lặp lại cho đến khi toàn bộ mảng được sắp xếp hoàn chỉnh.


# 2. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: [7, 12, 9, 11, 3]
# - Bước 1-2: Phần đã sắp xếp ban đầu là [7]. Phần chưa sắp xếp là [12, 9, 11, 3].
#   -> [7 | 12, 9, 11, 3]
# - Bước 3: Xét phần tử 12. So sánh với 7: 12 > 7, nên 12 đã ở đúng vị trí ngay sau 7:
#   -> [7, 12 | 9, 11, 3]
# - Bước 4-5: Xét phần tử 9. 9 nhỏ hơn 12 nhưng lớn hơn 7, chèn 9 vào giữa 7 và 12:
#   -> [7, 9, 12 | 11, 3]
# - Bước 6-7: Xét phần tử 11. 11 nhỏ hơn 12 nhưng lớn hơn 9, chèn 11 vào giữa 9 và 12:
#   -> [7, 9, 11, 12 | 3]
# - Bước 8-9: Xét phần tử 3. 3 nhỏ hơn tất cả các phần tử đã xếp (12, 11, 9, 7), chèn 3 vào đầu mảng:
#   -> [3, 7, 9, 11, 12]
# -> Kết thúc: Toàn bộ mảng đã được sắp xếp tăng dần!


# 3. Cài đặt cơ bản với pop() và insert() - Vấn đề dịch chuyển ô nhớ (Shifting Problem)
# Cách tiếp cận trực quan nhất theo mô phỏng xếp bài:
# - Rút phần tử ra bằng `arr.pop(i)`
# - Tìm vị trí chèn rồi gọi `arr.insert(insert_index, current_value)`
# Vấn đề hiệu năng nghiêm trọng (Hidden Memory Shifts):
# - pop(i): Khi xóa phần tử tại chỉ số i, máy tính phải dồn toàn bộ các phần tử phía sau sang trái 1 ô.
# - insert(insert_index, current_val): Máy tính phải dồn toàn bộ các phần tử từ insert_index sang phải 1 ô.
# -> Trong các ngôn ngữ bậc cao như Python, ta không thấy phép dịch chuyển này trong code,
# nhưng CPU phải thực hiện hàng ngàn phép dịch chuyển ô nhớ ngầm trong RAM, làm giảm hiệu năng nghiêm trọng.
def insertion_sort_with_pop_insert(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(1, n):
        insert_index = i
        current_value = arr_copy.pop(i)
        for j in range(i - 1, -1, -1):
            if arr_copy[j] > current_value:
                insert_index = j
        arr_copy.insert(insert_index, current_value)
    return arr_copy


demo_list = [64, 34, 25, 12, 22, 11, 90, 5]
print("Insertion Sort with pop() and insert() (Naive approach):")
print(insertion_sort_with_pop_insert(demo_list))


# 4. Cải tiến tối ưu: Dịch chuyển tại chỗ và Dừng sớm (In-place Shifting & Early Break)
# Giải pháp tối ưu:
# - Lưu giá trị cần chèn vào biến tạm: current_value = arr[i].
# - Dịch chuyển trực tiếp các phần tử lớn hơn sang phải 1 vị trí: arr[j + 1] = arr[j].
# - Khi gặp phần tử đầu tiên nhỏ hơn hoặc bằng current_value (hoặc chạm mốc đầu mảng),
#   ta dừng ngay lập tức (`break`) vì phần bên trái đã có thứ tự sẵn!
# - Đặt giá trị cần chèn vào vị trí trống đã tạo: arr[insert_index] = current_value.
# -> Giảm số lượng thao tác dịch chuyển bộ nhớ đi rất nhiều lần so với việc pop và insert liên tục.
def insertion_sort_improved(arr):
    arr_copy = arr.copy()
    n = len(arr_copy)
    for i in range(1, n):
        insert_index = i
        current_value = arr_copy[i]
        for j in range(i - 1, -1, -1):
            if arr_copy[j] > current_value:
                arr_copy[j + 1] = arr_copy[j]
                insert_index = j
            else:
                break
        arr_copy[insert_index] = current_value
    return arr_copy


print("\nImproved Insertion Sort (In-place shifting with break):")
print(insertion_sort_improved(demo_list))


# 5. Cài đặt chuẩn công nghiệp (Production-Ready Insertion Sort)
# Sử dụng vòng lặp `while` kinh điển - phương pháp được chuẩn hóa trong khoa học máy tính:
# Hỗ trợ tùy chọn khóa `key` (sắp xếp object/tuple) và thứ tự `reverse`.
def insertion_sort(arr, key=None, reverse=False):
    n = len(arr)
    get_key = key if key else (lambda x: x)

    for i in range(1, n):
        current_val = arr[i]
        current_key = get_key(current_val)
        j = i - 1

        # Điều kiện dịch chuyển sang phải:
        # Khi reverse=False: dịch chuyển nếu phần tử trước lớn hơn phần tử hiện tại.
        # Khi reverse=True: dịch chuyển nếu phần tử trước nhỏ hơn phần tử hiện tại.
        # Lưu ý: Sử dụng dấu so sánh nghiêm ngặt (> hoặc <) để bảo toàn tính ỔN ĐỊNH (Stable Sort).
        if not reverse:
            while j >= 0 and get_key(arr[j]) > current_key:
                arr[j + 1] = arr[j]
                j -= 1
        else:
            while j >= 0 and get_key(arr[j]) < current_key:
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = current_val

    return arr


sample_numbers = [64, 34, 25, 12, 22, 11, 90, 5]
insertion_sort(sample_numbers)
print("\nProduction-Ready Insertion Sort (In-place while-loop):")
print("Ascending: ", sample_numbers)

insertion_sort(sample_numbers, reverse=True)
print("Descending:", sample_numbers)


# 6. Biến thể nâng cao: Binary Insertion Sort (Sắp xếp chèn nhị phân)
# Ý tưởng: Vì đoạn mảng con arr[0:i] đã được sắp xếp sẵn, ta có thể áp dụng Binary Search
# để tìm vị trí chèn chỉ trong O(log n) phép so sánh (thay vì O(n) như duyệt tuyến tính).
# - Tổng số phép so sánh giảm từ O(n^2) xuống O(n log n).
# - Lưu ý: Số phép dịch chuyển phần tử vẫn là O(n^2), nên tổng thời gian vẫn là O(n^2).
# - Ứng dụng thực tế: Đây là nền tảng cốt lõi được Timsort (thuật toán sắp xếp mặc định của Python)
#   sử dụng để sắp xếp các khối dữ liệu con có kích thước nhỏ (run size <= 32 hoặc 64).
def binary_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        val = arr[i]
        # Tìm vị trí chèn bằng Binary Search
        low, high = 0, i
        while low < high:
            mid = (low + high) // 2
            if val < arr[mid]:
                high = mid
            else:
                low = mid + 1
        pos = low

        # Dịch chuyển các phần tử từ pos đến i - 1 sang phải một nấc
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = val

    return arr


binary_sort_demo = [37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54]
binary_insertion_sort(binary_sort_demo)
print("\nBinary Insertion Sort result:")
print(binary_sort_demo)


# 7. Minh họa tính ỔN ĐỊNH (Stable Sort)
# - Định nghĩa: Thuật toán sắp xếp được gọi là ỔN ĐỊNH nếu nó giữ nguyên thứ tự xuất hiện ban đầu
#   của các phần tử có cùng giá trị khóa.
# - Insertion Sort là Stable Sort vì khi gặp phần tử có giá trị bằng nhau, vòng lặp dừng lại
#   và không thực hiện dịch chuyển, do đó phần tử đứng sau ban đầu vẫn đứng sau phần tử đứng trước.
students = [
    ("David", 92),
    ("Alice", 85),
    ("Bob", 78),
    ("Charlie", 85)
]

insertion_sort(students, key=lambda s: s[1])
print("\nStable Sort demonstration with student grades:")
for name, grade in students:
    print(f"  {name}: {grade}")
# Kết quả: Alice (85) vẫn đứng trước Charlie (85) đúng theo thứ tự nhập liệu ban đầu!


# 8. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tốt nhất (Best Case): O(n) khi mảng đã sắp xếp sẵn.
#     Ở mỗi bước, phần tử mới chỉ cần so sánh đúng 1 lần với phần tử trước đó và dừng ngay (break).
#     Tổng số phép so sánh chỉ là n - 1. Đây là ưu điểm vượt trội của Insertion Sort so với Selection Sort!
#   + Trung bình (Average Case): O(n^2). Trung bình mỗi phần tử phải so sánh và dịch chuyển qua n/2 vị trí.
#   + Xấu nhất (Worst Case): O(n^2) khi mảng bị đảo ngược hoàn toàn.
# - Độ phức tạp không gian (Space Complexity):
#   + O(1) phụ trợ (In-place sort): Chỉ cần một biến tạm lưu giá trị phần tử đang chèn.
# - Khi nào nên dùng Insertion Sort:
#   + Khi kích thước mảng nhỏ (n <= 32 hoặc 64).
#   + Khi dữ liệu đã gần như có thứ tự sẵn (Nearly sorted data).
#   + Online Sorting: Khi dữ liệu đến dạng luồng (streaming) theo thời gian thực và cần chèn từng giá trị một
#     vào một danh sách đã có thứ tự từ trước.
