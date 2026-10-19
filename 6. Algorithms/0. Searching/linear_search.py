# 6. Algorithms - 1. Searching: Tìm kiếm tuyến tính (Linear Search)
# Khái niệm thuật toán tìm kiếm tuần tự, cài đặt cơ bản và phân tích độ phức tạp O(n)
#
# 1. Khái niệm về Tìm kiếm tuyến tính (Linear Search / Sequential Search)
# - Là thuật toán tìm kiếm đơn giản nhất trong khoa học máy tính.
# - Nguyên lý hoạt động:
#   + Duyệt qua từng phần tử của danh sách lần lượt từ đầu đến cuối.
#   + So sánh từng giá trị với giá trị mục tiêu (target value) cần tìm.
#   + Nếu tìm thấy, trả về chỉ số (index) của phần tử đó.
#   + Nếu duyệt hết toàn bộ danh sách mà không tìm thấy, trả về -1 để báo hiệu không tồn tại.
# - Ưu điểm:
#   + Cực kỳ đơn giản, trực quan, dễ cài đặt.
#   + Hoạt động trên mọi loại dữ liệu (mảng chưa sắp xếp, danh sách liên kết).
# - Nhược điểm: Chậm trên tập dữ liệu lớn vì độ phức tạp thời gian là O(n).

# 2. Kiểm tra phần tử tồn tại bằng toán tử 'in' trong Python
# Trong Python, cách nhanh nhất và trực quan nhất để kiểm tra một phần tử có trong danh sách hay không
# là sử dụng toán tử 'in' (bên dưới tầng C của CPython cũng thực hiện duyệt tuyến tính O(n)):
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
    print("Check with 'in' operator: Found!")
else:
    print("Check with 'in' operator: Not found!")


# 3. Cài đặt thuật toán Linear Search để tìm chỉ số (Index Lookup)
# Khi cần biết chính xác vị trí index của phần tử, ta tự cài đặt vòng lặp Linear Search:
def linear_search(arr, target_val):
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1


# Thử nghiệm với mảng mẫu:
search_val = 4
result_idx = linear_search(mylist, search_val)

if result_idx != -1:
    print(f"Linear search for {search_val}: Found at index {result_idx}")
else:
    print(f"Linear search for {search_val}: Not found")

# Thử nghiệm tìm phần tử không tồn tại:
not_found_val = 99
result_not_found = linear_search(mylist, not_found_val)

if result_not_found != -1:
    print(f"Linear search for {not_found_val}: Found at index {result_not_found}")
else:
    print(f"Linear search for {not_found_val}: Not found (returned -1)")


# 4. Biến thể: Tìm tất cả các vị trí xuất hiện (Find All Occurrences)
# Trong thực tế, một giá trị có thể xuất hiện nhiều lần trong mảng.
def linear_search_all(arr, target_val):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target_val:
            indices.append(i)
    return indices


multi_list = [4, 2, 7, 4, 9, 4, 1]
print("\nAll occurrences of 4 in [4, 2, 7, 4, 9, 4, 1]:", linear_search_all(multi_list, 4))  # [0, 3, 5]


# 5. Phân tích độ phức tạp thuật toán (Time & Space Complexity)
# - Thời gian (Time Complexity):
#   + Best Case (Trường hợp tốt nhất): O(1) - Phần tử cần tìm nằm ngay ở vị trí đầu tiên (chỉ cần 1 phép so sánh).
#   + Worst Case (Trường hợp xấu nhất): O(n) - Phần tử nằm ở cuối mảng hoặc không tồn tại (cần đúng n phép so sánh).
#   + Average Case (Trường hợp trung bình): O(n) - Trung bình cần n / 2 phép so sánh.
# - Không gian (Space Complexity): O(1) - Chỉ sử dụng một biến đếm chỉ số i, không tốn thêm bộ nhớ.
#
# 6. Khi nào nên dùng Linear Search vs Binary Search?
# - Dùng Linear Search khi:
#   + Mảng chưa được sắp xếp và kích thước nhỏ.
#   + Chỉ tìm kiếm 1 lần duy nhất (không bõ công sắp xếp mảng tốn O(n log n)).
# - Chuyển sang Binary Search khi:
#   + Mảng đã được sắp xếp tăng dần từ trước.
#   + Khi đó Binary Search đạt tốc độ vượt trội O(log n) so với O(n) của Linear Search.
print("\nComplexity Summary:")
print("- Time: Best O(1), Worst O(n), Average O(n)")
print("- Space: O(1)")
