# Thuật toán Counting Sort (Sắp xếp đếm phân phối)
# - Thuật toán sắp xếp KHÔNG dựa trên phép so sánh (Non-comparison based sort)
# - Ý tưởng: Đếm số lần xuất hiện của từng phần tử bằng một mảng đếm (frequency array).
# - Độ phức tạp thời gian: O(n + k) tuyến tính (với k là khoảng giá trị của phần tử).
# - Đặc biệt tối ưu khi miền giá trị nhỏ (ví dụ: chữ số 0-9, điểm số 0-100, ký tự ASCII).

def counting_sort_digits(arr):
    # Khởi tạo mảng đếm cố định cho 10 chữ số (0 đến 9)
    counts = [0] * 10

    # Bước 1: Đếm tần suất
    for num in arr:
        counts[num] += 1

    # Bước 2: Tái tạo mảng đã sắp xếp (tự động theo thứ tự tăng dần từ 0 -> 9)
    sorted_arr = []
    for digit in range(10):
        sorted_arr.extend([digit] * counts[digit])

    return sorted_arr

digits_sample = [4, 2, 7, 2, 1, 9, 0, 4, 1]
print("Original:", digits_sample)
print("Counting Sort (O(n + k)):", counting_sort_digits(digits_sample))
