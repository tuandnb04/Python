# 6. Algorithms - 2. Sorting - Extra: Sắp xếp theo thùng (Bucket Sort)
# Khái niệm thuật toán, phân phối đều cho số thực trong [0, 1), phân loại vào thùng,
# sắp xếp cục bộ từng thùng (Insertion Sort), ghép nối và phân tích độ phức tạp O(n)

# 1. Khái niệm về Thuật toán Bucket Sort
# - Bucket Sort (Sắp xếp theo thùng) là thuật toán sắp xếp dựa trên kỹ thuật phân phối (Scatter-Gather approach).
# - Điều kiện lý tưởng: Dữ liệu đầu vào là các số thực được phân phối đều (Uniformly distributed) trong khoảng [0, 1).
# - Nguyên lý hoạt động:
#   + Phân tán (Scatter): Tạo k thùng rỗng (thường chọn k = n, với n là số phần tử).
#     Mỗi giá trị x được đưa vào thùng thứ index = int(k * x).
#   + Sắp xếp cục bộ: Sắp xếp từng thùng độc lập (thường dùng Insertion Sort vì mỗi thùng chứa rất ít phần tử).
#   + Gom tụ (Gather): Duyệt tuần tự qua các thùng từ 0 đến k - 1 và ghép các phần tử lại thành mảng kết quả có thứ tự.


# 2. Cài đặt thuật toán chèn nội bộ (Insertion Sort Subroutine)
def insertion_sort_bucket(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
    return bucket


# 3. Cài đặt Bucket Sort chuẩn mực cho mảng số thực [0, 1)
def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr

    # 1. Tạo n thùng rỗng
    buckets = [[] for _ in range(n)]

    # 2. Phân phối các phần tử vào các thùng tương ứng: index = int(n * val)
    for val in arr:
        # Giới hạn chỉ số để giá trị 1.0 (nếu có) không bị tràn chỉ số n
        bucket_idx = min(int(n * val), n - 1)
        buckets[bucket_idx].append(val)

    # 3. Sắp xếp từng thùng và gom lại vào mảng kết quả
    sorted_arr = []
    for bucket in buckets:
        insertion_sort_bucket(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr


# 4. Mở rộng Bucket Sort cho dải số thực bất kỳ [min_val, max_val]
def bucket_sort_arbitrary_range(arr, bucket_count=10):
    if len(arr) <= 1:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    # Nếu tất cả các phần tử đều bằng nhau
    if min_val == max_val:
        return arr.copy()

    val_range = max_val - min_val
    buckets = [[] for _ in range(bucket_count)]

    # Chuẩn hóa giá trị về tỷ lệ [0, 1) để tìm chỉ số thùng
    for val in arr:
        normalized = (val - min_val) / val_range
        idx = min(int(normalized * bucket_count), bucket_count - 1)
        buckets[idx].append(val)

    result = []
    for bucket in buckets:
        insertion_sort_bucket(bucket)
        result.extend(bucket)

    return result


# 5. Thử nghiệm thực tế
floats_sample = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Bucket Sort on Uniform Floats [0, 1):")
print("Original:", floats_sample)
print("Sorted:  ", bucket_sort(floats_sample))

arbitrary_sample = [42.5, 12.1, 89.9, 3.4, 55.6, 21.0, 77.3, 10.5]
print("\nBucket Sort on Arbitrary Range:")
print("Original:", arbitrary_sample)
print("Sorted:  ", bucket_sort_arbitrary_range(arbitrary_sample, bucket_count=5))


# 6. Phân tích độ phức tạp thời gian và không gian (Time and Space Complexity)
# - Độ phức tạp thời gian (Time Complexity):
#   + Trường hợp tốt nhất / Trung bình (Best & Average Case): O(n + k), tuyến tính O(n) khi k = n.
#     Nếu dữ liệu phân phối đều, mỗi thùng chỉ chứa trung bình O(1) phần tử, việc sắp xếp mỗi thùng tốn O(1).
#   + Trường hợp xấu nhất (Worst Case): O(n^2). Xảy ra khi toàn bộ dữ liệu bị lệch và rơi vào duy nhất 1 thùng,
#     thuật toán thoái hóa thành Insertion Sort O(n^2).
# - Độ phức tạp không gian (Space Complexity):
#   + O(n + k) để lưu trữ danh sách các thùng chứa.
# - Điểm khác biệt giữa Bucket Sort và Counting Sort:
#   + Counting Sort đếm tần suất số nguyên cụ thể theo giá trị rời rạc.
#   + Bucket Sort gom các giá trị liên tục (số thực, float) vào các khoảng phân vùng con.
