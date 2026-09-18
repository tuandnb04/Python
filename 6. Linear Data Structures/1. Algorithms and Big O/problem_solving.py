# Quy trình giải quyết bài toán thuật toán:
# 1. Hiểu đề bài: Xác định rõ Input, Output và Constraints (Ràng buộc)
# 2. Viết mã giả (Pseudocode): Mô tả logic dạng văn bản dễ hiểu, độc lập ngôn ngữ
# 3. Xét các trường hợp biên (Edge Cases): Ví dụ chuỗi rỗng "", mảng 1 phần tử
# 4. Cài đặt, so sánh độ phức tạp và tối ưu (Refactoring)

# Ví dụ bài toán: Đảo ngược chuỗi (Reverse a String)
test_str = "hello"
empty_str = ""  # Edge case

# Cách 1: Sử dụng Slicing [::-1] (Ngắn gọn, tối ưu trong Python - O(n))
def reverse_slice(s):
    return s[::-1]

# Cách 2: Vòng lặp duyệt tuần tự (Mô phỏng theo pseudocode)
def reverse_loop(s):
    res = ""
    for char in s:
        res = char + res
    return res

# Cách 3: Sử dụng reversed() và join()
def reverse_builtin(s):
    return "".join(reversed(s))

print("Slice [::-1]:", reverse_slice(test_str))        # olleh
print("Looping:", reverse_loop(test_str))              # olleh
print("Builtin:", reverse_builtin(test_str))          # olleh
print("Edge case (empty):", repr(reverse_slice(empty_str))) # ''
