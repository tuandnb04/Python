# 6. Algorithms - 2. Sorting: Sắp xếp theo cơ số (Radix Sort)
# Khái niệm thuật toán, cơ số (Radix/Base), tầm quan trọng của tính ổn định (Stable Sort),
# mô phỏng từng bước (Manual Run Through), cài đặt Buckets, tối ưu kết hợp Counting Sort và xử lý số âm

# 1. Khái niệm về Thuật toán Radix Sort
# - Radix Sort là thuật toán sắp xếp KHÔNG SO SÁNH (Non-comparative sort), chuyên dùng cho các số nguyên.
# - Nguyên lý hoạt động: Sắp xếp các phần tử bằng cách duyệt qua từng chữ số của chúng, bắt đầu từ
#   chữ số có trọng số thấp nhất (Least Significant Digit - LSD, hàng đơn vị) cho đến chữ số có trọng số cao nhất (MSD).
# - Khái niệm "Radix" (Cơ số):
#   + Là số lượng ký tự số duy nhất trong một hệ đếm.
#   + Trong hệ thập phân (Base 10) mà chúng ta quen thuộc, cơ số là 10 (gồm 10 chữ số từ 0 đến 9).
#   + Do đó, Radix Sort sử dụng 10 "thùng chứa" (Buckets) được đánh chỉ số từ 0 đến 9 để phân loại các phần tử
#     dựa trên chữ số đang được xét.


# 2. Tầm quan trọng sống còn của Tính Ổn định (Stable Sorting)
# - Định nghĩa: Thuật toán ổn định (Stable Sort) là thuật toán bảo toàn thứ tự xuất hiện ban đầu của các phần tử có cùng giá trị.
# - Tại sao Radix Sort BẮT BUỘC phải ổn định?
#   + Vì Radix Sort sắp xếp số qua từng chữ số độc lập.
#   + Sau khi sắp xếp xong theo hàng đơn vị, khi chuyển sang sắp xếp theo hàng chục, ta KHÔNG ĐƯỢC làm hỏng
#     thứ tự đã đạt được ở hàng đơn vị đối với các số có cùng chữ số hàng chục.
#   + Ví dụ: Xét số 24 và 25. Ở hàng đơn vị, 24 < 25 nên 24 đứng trước 25.
#     Khi sang hàng chục, cả hai số đều có chữ số 2. Nếu thuật toán ổn định, 24 sẽ tiếp tục đứng trước 25.
#     Nếu thuật toán không ổn định và đảo ngược lại thành 25 rồi đến 24, kết quả cuối cùng sẽ sai hoàn toàn!


# 3. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: myArray = [33, 45, 40, 25, 17, 24]
# Tạo 10 thùng rỗng: radixArray = [[], [], [], [], [], [], [], [], [], []]
#
# - VÒNG 1: Xét chữ số hàng đơn vị (exp = 1)
#   + 40 (đơn vị 0) -> bucket 0
#   + 33 (đơn vị 3) -> bucket 3
#   + 24 (đơn vị 4) -> bucket 4
#   + 45 (đơn vị 5) -> bucket 5
#   + 25 (đơn vị 5) -> bucket 5 (đứng sau 45 vì vào sau)
#   + 17 (đơn vị 7) -> bucket 7
#   -> Các bucket: [[40], [], [], [33], [24], [45, 25], [], [17], [], []]
#   -> Đưa lại vào mảng chính: [40, 33, 24, 45, 25, 17]
#
# - VÒNG 2: Xét chữ số hàng chục (exp = 10)
#   + 17 (chục 1) -> bucket 1
#   + 24 (chục 2) -> bucket 2
#   + 25 (chục 2) -> bucket 2 (nhờ tính ổn định, 24 vẫn đứng trước 25!)
#   + 33 (chục 3) -> bucket 3
#   + 40 (chục 4) -> bucket 4
#   + 45 (chục 4) -> bucket 4 (40 đứng trước 45)
#   -> Các bucket: [[], [17], [24, 25], [33], [40, 45], [], [], [], [], []]
#   -> Đưa lại vào mảng chính: [17, 24, 25, 33, 40, 45]
# -> Kết thúc: Mảng được sắp xếp hoàn chỉnh!


# 4. Cài đặt Radix Sort cơ bản bằng 10 Buckets (Intuitive Bucket Approach)
# - Sử dụng phép chia nguyên `// exp` và phép chia lấy dư `% 10` để trích xuất chữ số đang xét:
#   Ví dụ: Số 802 tại hàng chục (exp = 10): (802 // 10) % 10 = 80 % 10 = 0 -> Đặt vào bucket 0.
def radix_sort_buckets(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    # Lặp qua từng hàng chữ số: đơn vị (1), chục (10), trăm (100), ...
    while max_val // exp > 0:
        radix_array = [[] for _ in range(10)]

        # Phân phối các số vào 10 thùng tương ứng
        for num in arr:
            radix_index = (num // exp) % 10
            radix_array[radix_index].append(num)

        # Gom các số từ các thùng trở lại mảng chính (đảm bảo FIFO để duy trì tính ổn định)
        arr_idx = 0
        for bucket in radix_array:
            for num in bucket:
                arr[arr_idx] = num
                arr_idx += 1

        exp *= 10

    return arr


sample_list = [170, 45, 75, 90, 802, 24, 2, 66]
print("Radix Sort using 10 Buckets (Intuitive approach):")
print("Original:", [170, 45, 75, 90, 802, 24, 2, 66])
radix_sort_buckets(sample_list)
print("Sorted:  ", sample_list)


# 5. Cài đặt chuẩn công nghiệp: Radix Sort kết hợp Stable Counting Sort (CLRS Standard)
# Trong khoa học máy tính chuẩn mực, thay vì cấp phát danh sách 2 chiều liên tục ở mỗi vòng,
# người ta dùng Counting Sort ổn định làm chương trình con (Subroutine).
# - Tiết kiệm chi phí cấp phát bộ nhớ mảng phụ và tăng tốc độ xử lý trong RAM.
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 1. Đếm tần suất xuất hiện của chữ số tại vị trí exp
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # 2. Tính tổng cộng dồn (Prefix Sum) để xác định vị trí thực tế
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. Duyệt NGƯỢC từ cuối mảng gốc về đầu để đảm bảo tính ỔN ĐỊNH tuyệt đối
    for i in range(n - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % 10
        output[count[digit] - 1] = num
        count[digit] -= 1

    # 4. Sao chép kết quả đã sắp xếp của chữ số này về mảng gốc
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    # Gọi Counting Sort ổn định cho từng hàng chữ số
    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


sample_clrs = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(sample_clrs)
print("\nRadix Sort using Stable Counting Sort Subroutine (CLRS Standard):")
print("Sorted:  ", sample_clrs)


# 6. Minh họa kết hợp Radix Sort với Bubble Sort (Bất kỳ thuật toán con ổn định nào)
# Radix Sort có thể kết hợp với BẤT KỲ thuật toán sắp xếp nào, miễn là thuật toán con đó ỔN ĐỊNH.
def bubble_sort_stable(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def radix_sort_with_bubble_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        radix_list = [[] for _ in range(10)]
        for num in arr:
            radix_index = (num // exp) % 10
            radix_list[radix_index].append(num)

        for bucket in radix_list:
            bubble_sort_stable(bucket)

        idx = 0
        for bucket in radix_list:
            for num in bucket:
                arr[idx] = num
                idx += 1

        exp *= 10

    return arr


sample_bubble = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort_with_bubble_sort(sample_bubble)
print("\nRadix Sort with Bubble Sort for Buckets (Subroutine demonstration):")
print("Sorted:  ", sample_bubble)


# 7. Mở rộng: Hỗ trợ Số nguyên âm trong Radix Sort (Handling Negative Numbers)
# Vì số âm có quy tắc ngược lại (-10 < -2 dù 10 > 2), cách xử lý chuẩn mực là:
# - Tách mảng thành 2 nhóm: số âm (negatives) và số không âm (positives).
# - Với số âm, lấy trị tuyệt đối rồi chạy Radix Sort, sau đó đảo ngược kết quả và đổi lại dấu trừ.
# - Nối danh sách số âm đã sắp xếp với danh sách số dương đã sắp xếp.
def radix_sort_with_negatives(arr):
    if not arr:
        return arr

    negatives = [-x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    # Sắp xếp trị tuyệt đối của các số âm và số dương
    radix_sort(negatives)
    radix_sort(positives)

    # Đảo ngược số âm và gắn lại dấu trừ (vì |-10| = 10 lớn hơn |-2| = 2, nhưng -10 < -2)
    sorted_negatives = [-x for x in reversed(negatives)]

    return sorted_negatives + positives


mixed_numbers = [170, -45, 75, -90, 802, -24, 2, -66, 0]
print("\nRadix Sort with Negative Integers support:")
print("Original:", mixed_numbers)
print("Sorted:  ", radix_sort_with_negatives(mixed_numbers))


# 8. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tổng quát: O(n * k), trong đó:
#     * n là số lượng phần tử cần sắp xếp.
#     * k là số chữ số của phần tử lớn nhất (k = log10(max_val) + 1).
#   + Trường hợp tốt nhất: Khi k là một hằng số nhỏ (ví dụ 1,000,000 số có giá trị tối đa 999, k = 3).
#     Khi đó O(n * k) tương đương O(n) tuyến tính, nhanh hơn rất nhiều so với O(n log n) của Quicksort!
#   + Trường hợp xấu nhất: Khi số chữ số k tỷ lệ thuận với n (k = n), thời gian thành O(n^2).
#   + Trường hợp thông thường: Khi k = log(n), độ phức tạp là O(n log n).
# - Độ phức tạp không gian (Space Complexity):
#   + O(n + b) trong đó b là cơ số (b = 10 trong hệ thập phân), n là bộ nhớ mảng kết quả tạm thời.
# - Điểm mạnh & Điểm yếu:
#   + Điểm mạnh: Không có phép so sánh trực tiếp, cực kỳ nhanh với số nguyên có giới hạn độ dài chữ số.
#   + Điểm yếu: Không áp dụng trực tiếp cho số thực (float), chuỗi có độ dài biến thiên lớn hoặc cấu trúc dữ liệu phức tạp.
