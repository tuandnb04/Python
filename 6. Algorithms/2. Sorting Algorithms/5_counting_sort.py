# 6. Algorithms - 2. Sorting: Sắp xếp đếm phân phối (Counting Sort)
# Khái niệm thuật toán, sắp xếp phi so sánh (Non-comparison sort), điều kiện áp dụng,
# mô phỏng từng bước (Manual Run Through), giải quyết vấn đề pop(0), thuật toán ổn định (Stable Counting Sort) và số âm

# 1. Khái niệm về Thuật toán Counting Sort
# - Counting Sort là thuật toán sắp xếp KHÔNG DỰA TRÊN SO SÁNH (Non-comparison based sort).
# - Các thuật toán so sánh (Bubble, Selection, Insertion, Quicksort, Merge) bị giới hạn bởi cận dưới lý thuyết
#   O(n log n). Counting Sort phá vỡ giới hạn này bằng cách sử dụng giá trị của phần tử làm chỉ số (index)
#   để đếm tần suất xuất hiện trực tiếp trong một mảng đếm (Counting Array).
# - Nguyên lý hoạt động:
#   + Tạo một mảng đếm `count` có kích thước đủ để chứa tất cả các giá trị từ 0 đến giá trị lớn nhất (max_val).
#   + Duyệt qua mảng cần sắp xếp, mỗi lần gặp giá trị x thì tăng `count[x]` lên 1.
#   + Sau khi đếm xong, duyệt qua mảng đếm từ đầu đến cuối để tái tạo lại mảng đã sắp xếp theo thứ tự tăng dần.


# 2. Điều kiện và Giới hạn áp dụng của Counting Sort
# - Chỉ áp dụng cho số nguyên (Integer values): Vì các giá trị phải ánh xạ tương ứng vào chỉ số mảng nguyên.
# - Giá trị không âm (Non-negative values): Mặc định mảng bắt đầu từ index 0 (nếu có số âm cần dịch chuyển bằng offset).
# - Miền giá trị k phải tương đương hoặc nhỏ hơn số lượng phần tử n (Limited range of values):
#   + Nếu mảng có n = 5 phần tử nhưng số lớn nhất là 1,000,000, ta phải tạo mảng đếm 1,000,001 ô nhớ.
#   + Điều này gây lãng phí bộ nhớ khủng khiếp và thuật toán mất thời gian duyệt qua hàng triệu ô số 0 vô ích.


# 3. Mô phỏng từng bước thủ công (Manual Run Through)
# Mảng ban đầu: myArray = [2, 3, 0, 2, 3, 2]
# - Bước 1-2: Giá trị lớn nhất là 3 -> Tạo mảng đếm gồm 4 phần tử (từ 0 đến 3):
#   countArray = [0, 0, 0, 0]
# - Bước 3-6: Đếm từng phần tử:
#   + Gặp 2 -> countArray[2] tăng thành 1 -> [0, 0, 1, 0]
#   + Gặp 3 -> countArray[3] tăng thành 1 -> [0, 0, 1, 1]
#   + Gặp 0 -> countArray[0] tăng thành 1 -> [1, 0, 1, 1]
#   + Gặp 2 -> countArray[2] tăng thành 2 -> [1, 0, 2, 1]
#   + Gặp 3 -> countArray[3] tăng thành 2 -> [1, 0, 2, 2]
#   + Gặp 2 -> countArray[2] tăng thành 3 -> [1, 0, 3, 2]
#   -> Kết quả sau khi đếm: countArray = [1, 0, 3, 2]
# - Bước 7-10: Tái tạo mảng theo thứ tự từ nhỏ đến lớn:
#   + countArray[0] = 1 -> Đưa 1 số 0 vào mảng: [0]
#   + countArray[1] = 0 -> Bỏ qua
#   + countArray[2] = 3 -> Đưa 3 số 2 vào mảng: [0, 2, 2, 2]
#   + countArray[3] = 2 -> Đưa 2 số 3 vào mảng: [0, 2, 2, 2, 3, 3]
# -> Kết thúc: Mảng được sắp xếp hoàn chỉnh!


# 4. Cài đặt cơ bản và Phân tích tối ưu
# Lưu ý về pop(0):
# - Trong cách tiếp cận ngây thơ dùng `arr.pop(0)`, Python tốn O(n) do phải dịch chuyển toàn bộ mảng sang trái.
# - Do đó, thay vì `pop(0)`, ta duyệt trực tiếp `for num in arr:` để đạt tốc độ chuẩn O(n + k).
def counting_sort_basic(arr):
    if not arr:
        return []

    max_val = max(arr)
    count = [0] * (max_val + 1)

    # Đếm tần suất xuất hiện không làm biến đổi mảng gốc
    for num in arr:
        count[num] += 1

    # Tái tạo mảng có thứ tự
    sorted_arr = []
    for i in range(len(count)):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


sample_list = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
print("Basic Counting Sort (Frequency counting):")
print("Original:", sample_list)
print("Sorted:  ", counting_sort_basic(sample_list))


# 5. Cài đặt chuẩn công nghiệp: Stable Counting Sort (Cộng dồn Prefix Sum)
# Vấn đề của cách cơ bản trên: Nó chỉ tái tạo lại các con số, không phải là sắp xếp ỔN ĐỊNH (Stable).
# Nếu các phần tử là Object hoặc Tuple mang kèm dữ liệu phụ, cách trên sẽ làm mất đối tượng gốc.
# Giải pháp chuẩn mực (Chuẩn bị làm tiền đề cho thuật toán Radix Sort tiếp theo):
# - Bước 1: Đếm tần suất `count[val]`.
# - Bước 2: Tính tổng cộng dồn (Prefix Sum): `count[i] += count[i - 1]`
#   Lúc này `count[i]` cho biết vị trí (1-based index) cuối cùng của phần tử `i` trong mảng kết quả!
# - Bước 3: Duyệt NGƯỢC từ cuối mảng gốc về đầu (`for i in range(n - 1, -1, -1)`),
#   đặt phần tử vào đúng vị trí `output[count[arr[i]] - 1]` và giảm `count[arr[i]] -= 1`.
#   -> Duyệt ngược giúp bảo toàn 100% thứ tự ban đầu của các phần tử bằng nhau (STABLE SORT).
def counting_sort_stable(arr, key=None):
    if not arr:
        return []

    n = len(arr)
    get_key = key if key else (lambda x: x)

    # Tìm giá trị khóa lớn nhất
    max_val = max(get_key(x) for x in arr)
    count = [0] * (max_val + 1)
    output = [None] * n

    # 1. Đếm số lần xuất hiện của từng khóa
    for item in arr:
        count[get_key(item)] += 1

    # 2. Cộng dồn tần suất (Prefix sum) để xác định vị trí thực tế trong mảng đích
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 3. Duyệt ngược từ cuối mảng gốc về đầu để giữ vững tính ổn định (Stability)
    for i in range(n - 1, -1, -1):
        item = arr[i]
        k = get_key(item)
        output[count[k] - 1] = item
        count[k] -= 1

    return output


# Minh họa tính ỔN ĐỊNH với danh sách học sinh có cùng điểm số
student_records = [
    ("Alice", 3),
    ("Bob", 1),
    ("Charlie", 3),
    ("David", 2),
    ("Eva", 1)
]

sorted_students = counting_sort_stable(student_records, key=lambda s: s[1])
print("\nStable Counting Sort with student tuples (by score):")
for name, score in sorted_students:
    print(f"  {name}: {score}")
# Kết quả: Alice vẫn đứng trước Charlie (cùng điểm 3), Bob vẫn đứng trước Eva (cùng điểm 1).


# 6. Mở rộng: Hỗ trợ Số nguyên âm (Handling Negative Numbers with Offset)
# Nếu mảng chứa số âm (ví dụ: [-5, -2, 0, 3, -1]), ta tìm giá trị nhỏ nhất `min_val = -5`.
# Sử dụng độ lệch `offset = -min_val` để chuyển tất cả các số về chỉ số không âm:
# Giá trị -5 sẽ ứng với chỉ số (-5 + 5) = 0 trong mảng đếm!
def counting_sort_with_negatives(arr):
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Ánh xạ giá trị num thành chỉ số (num - min_val)
    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output


negative_sample = [-5, -10, 0, -3, 8, 5, -1, 10]
print("\nCounting Sort supporting negative integers:")
print("Original:", negative_sample)
print("Sorted:  ", counting_sort_with_negatives(negative_sample))


# 7. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Tổng quát: O(n + k), trong đó n là số phần tử và k là phạm vi miền giá trị (max - min + 1).
#   + Tốt nhất / Trung bình: O(n) khi k <= n (khoảng giá trị nhỏ hoặc tỷ lệ thuận với số phần tử).
#   + Xấu nhất: O(n + k). Nếu k quá lớn (ví dụ k = n^2 hoặc hàng tỷ), thời gian duyệt mảng đếm chiếm ưu thế
#     và thuật toán trở nên kém hiệu quả hơn cả O(n log n).
# - Độ phức tạp không gian (Space Complexity):
#   + O(k) cho mảng đếm `count`.
#   + O(n) cho mảng kết quả `output` (đối với thuật toán ổn định).
# - Nhận xét quan trọng:
#   + Dù mảng có ngẫu nhiên, đã sắp xếp hay đảo ngược, số phép toán của Counting Sort đều không thay đổi.
#   + Counting Sort chính là thuật toán con cốt lõi (Subroutine) để xây dựng thuật toán Radix Sort!
