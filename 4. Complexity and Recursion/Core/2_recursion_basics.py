# 1. Khái niệm Đệ quy (Recursion)
# Đệ quy là kỹ thuật một hàm tự gọi lại chính nó để giải quyết bài toán
# bằng cách chia nhỏ thành các bài toán con cùng cấu trúc cho đến khi chạm điều kiện dừng.
#
# Hai thành phần BẮT BUỘC của một hàm đệ quy:
# 1. Base Case (Điều kiện dừng): Ngăn hàm gọi vô tận và bắt đầu tháo gỡ ngăn xếp (unwind stack).
# 2. Recursive Case (Trường hợp đệ quy): Gọi lại hàm với đối số thu hẹp dần về phía base case.

# 1.1. Ví dụ đệ quy đếm lùi cơ bản:
def recursive_countdown(number: int) -> None:
    if number < 1:  # Base case: Dừng lại khi number < 1
        return
    print(number, end=" ")
    recursive_countdown(number - 1)  # Recursive case: Tiến dần về base case

print("Countdown recursion:")
recursive_countdown(5)
print("\n")

# 2. Cơ chế Ngăn xếp Lời gọi hàm (Call Stack & Stack Frame)
# - Call Stack là cấu trúc dữ liệu LIFO (Last-In, First-Out) ngầm định quản lý các frame hàm đang chạy.
# - Khi gọi đệ quy, hàm cha tạm dừng (pause), đẩy 1 Stack Frame mới lên đỉnh stack.
# - Khi chạm Base Case, các frame lần lượt được hoàn thành và lấy ra (Pop) từ đỉnh xuống đáy.

# Minh họa thứ tự Push -> Pause -> Base Case -> Pop:
def trace_call_stack(number: int) -> None:
    if number < 1:
        print("  -> Base case reached! Unwinding stack...")
        return
    print(f"  Push frame ({number}) & Pause")
    trace_call_stack(number - 1)
    print(f"  Pop frame ({number}) -> Completed: {number}")

print("Call stack visualization:")
trace_call_stack(3)
print()

# 3. Tính toán toán học với Đệ quy: Tính Giai thừa (Factorial)
# Công thức: n! = n * (n - 1)! với 0! = 1 và 1! = 1.
# Cần kiểm tra ngoại lệ n < 0 vì giai thừa không định nghĩa cho số âm.
def find_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):  # Base case: 0! = 1 và 1! = 1
        return 1
    return n * find_factorial(n - 1)  # Recursive case: n * (n - 1)!

print("Factorial of 5 (5!):", find_factorial(5))  # 120

# 4. So sánh Đệ quy (Recursion) vs Vòng lặp (Iteration)
# - Vòng lặp (Iteration):
#   + Tối ưu cho bài toán duyệt tuyến tính tuần tự.
#   + Tiết kiệm bộ nhớ (O(1) auxiliary space), không lo tràn ngăn xếp.
# - Đệ quy (Recursion):
#   + Tự nhiên và trực quan cho cấu trúc phân nhánh, dữ liệu lồng nhau (Cây, Đồ thị, Chia để trị).
#   + Tiêu tốn bộ nhớ Call Stack: O(d) space với d là độ sâu đệ quy.
