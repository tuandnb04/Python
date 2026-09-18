# O(1) - Constant Time: Thời gian thực thi không đổi dù n tăng
def check_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

print("O(1) Check:", check_even_or_odd(42))

# O(n) - Linear Time: Thời gian tăng tuyến tính tỉ lệ thuận với kích thước n
def print_elements(items):
    for item in items:
        pass  # Duyệt qua từng phần tử trong danh sách n phần tử

print_elements([1, 2, 3, 4, 5])

# O(n^2) - Quadratic Time: 2 vòng lặp lồng nhau (Nested loops)
def count_pairs(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

print("O(n^2) operations for n=3:", count_pairs(3)) # 9 operations

# Tóm tắt các cấp độ Big O (từ nhanh nhất đến chậm nhất):
# - O(1)       : Constant Time (Truy cập phần tử, so sánh cơ bản)
# - O(log n)   : Logarithmic Time (Binary Search - chia đôi không gian tìm kiếm)
# - O(n)       : Linear Time (1 vòng lặp duyệt mảng)
# - O(n log n) : Log-Linear Time (Merge Sort, Quick Sort)
# - O(n^2)     : Quadratic Time (2 vòng lặp lồng nhau)
# - O(2^n)     : Exponential Time (Đệ quy nhánh - Fibonacci ngây thơ)
# - O(n!)      : Factorial Time (Sinh hoán vị)
