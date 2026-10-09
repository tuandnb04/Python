# Recursion & Call Stack (Kỹ thuật Đệ quy và Cơ chế Ngăn xếp Lời gọi hàm)
# - Khái niệm Đệ quy (Recursion): Kỹ thuật một hàm tự gọi chính nó để giải quyết bài toán
#   bằng cách chia nhỏ thành các bài toán con cùng cấu trúc cho đến khi chạm điều kiện dừng.
# - Hai thành phần bắt buộc của hàm đệ quy:
#    1. Base Case (Điều kiện dừng): Kết thúc đệ quy và bắt đầu tháo gỡ ngăn xếp (unwind stack).
#    2. Recursive Case (Trường hợp đệ quy): Gọi lại hàm với đối số thu hẹp dần về base case (Tính hội tụ - Convergence).
# - Call Stack & Stack Frame:
#    - Call Stack là cấu trúc dữ liệu LIFO (Last-In, First-Out) ngầm định quản lý các frame hàm đang chạy.
#    - Khi gọi đệ quy, hàm cha tạm dừng (pause), đẩy 1 Stack Frame mới lên đỉnh stack -> Tốn O(độ sâu) bộ nhớ.
# - So sánh Đệ quy (Recursion) vs Vòng lặp (Iteration):
#    + Vòng lặp: Tối ưu cho bài toán tuyến tính, tiết kiệm bộ nhớ (O(1) space).
#    + Đệ quy: Tự nhiên và vượt trội cho dữ liệu phân nhánh, không rõ trước độ sâu (Cây, Đồ thị, JSON/Dict lồng nhau).


# 1. Base Case & Recursive Case cơ bản
# - In trước khi gọi đệ quy: Lệnh print() chạy ngay khi frame được push lên đỉnh stack
def recursive_countdown(number: int) -> None:
    if number < 1:             # Base case: Dừng lại khi number < 1
        return
    print(number)
    recursive_countdown(number - 1)  # Recursive case: Tiến dần về base case

recursive_countdown(5)         # In ra: 5, 4, 3, 2, 1


# 2. Vị trí lời gọi đệ quy & Trực quan hóa Call Stack (LIFO)
# - Đặt print() sau lời gọi đệ quy: Lệnh bị tạm dừng và chỉ chạy khi frame được pop ra khỏi stack.
# - Trace chi tiết quá trình: Push -> Pause -> Base Case -> Pop ngược từ dưới lên (1 -> 2 -> 3)
def trace_countdown_asc(number: int) -> None:
    if number < 1:
        print("-> Base case reached (Stack unwinding starts)")
        return
    print(f"Push frame {number} & Pause")
    trace_countdown_asc(number - 1)
    print(f"Pop frame {number} -> Print value: {number}")

trace_countdown_asc(3)
# Thứ tự in hoàn thành: 1, 2, 3 (do frame 1 nằm trên đỉnh stack nên pop trước 2 và 3)


# 3. Đệ quy thu thập dữ liệu (Returning & Accumulating Data Structures - Bottom-up)
# - Thay vì chỉ print(), hàm tích lũy dữ liệu trả về từ các frame con từ dưới đáy stack trả lên.
# - Base case khởi tạo danh sách [] đúng 1 lần duy nhất, các frame cha gọi .append() in-place -> O(n) thời gian.
# - Lưu ý cạm bẫy: Tránh dùng toán tử '+' (vd: countup(n-1) + [n]) vì sẽ copy lại mảng ở mỗi tầng -> O(n^2).
def countup(number: int) -> list[int]:
    if number < 1:
        return []
    count_list: list[int] = countup(number - 1)
    count_list.append(number)
    return count_list

print("Countup list:", countup(5))     # In ra: [1, 2, 3, 4, 5]


# 4. Kỹ thuật Accumulator (Truyền đối số tích lũy từ trên xuống - Top-down / Tail Recursion)
# - Dữ liệu tích lũy được truyền trực tiếp qua từng frame con thay vì đợi stack tháo gỡ ngược lại.
# - Ứng dụng: Đảo ngược chuỗi (String Reversal)
def reverse_string_acc(text: str, acc: str = "") -> str:
    """Đảo ngược chuỗi bằng tham số tích lũy (Accumulator Pattern)."""
    if not text:
        return acc
    return reverse_string_acc(text[:-1], acc + text[-1])

print("Reversed string:", reverse_string_acc("recursion"))  # In ra: noisrucer


# 5. Tính toán toán học & Xử lý trường hợp biên (Factorial with Edge Cases)
# - Giai thừa n! = n * (n - 1)! với 0! = 1 và 1! = 1.
# - Cần chặn ngoại lệ n < 0 vì giai thừa không định nghĩa cho số âm (tránh rơi vào đệ quy vô hạn).
def find_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):                    # Base case: 0! = 1 và 1! = 1
        return 1
    return n * find_factorial(n - 1)   # Recursive case: n * (n - 1)!

print("Factorial of 5:", find_factorial(5))    # In ra: 120


# 6. Xử lý cấu trúc lồng nhau không rõ độ sâu (Deeply Nested Structures)
# - Đệ quy phát huy sức mạnh tối đa khi duyệt cây thư mục hoặc dữ liệu lồng nhau bất kỳ cấp độ.
def calculate_nested_sum(data: list | int) -> int:
    """Tính tổng mọi số nguyên trong danh sách lồng nhau bất kỳ độ sâu."""
    if isinstance(data, int):          # Base case: Phần tử đơn lẻ là số nguyên
        return data
    total = 0
    for item in data:                  # Recursive case: Lặp qua từng phần tử con
        total += calculate_nested_sum(item)
    return total

nested_data = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]
print("Nested list sum:", calculate_nested_sum(nested_data))  # In ra: 45


# 7. Giới hạn Call Stack & Bắt ngoại lệ RecursionError
# - Python runtime bảo vệ bộ nhớ bằng ngưỡng giới hạn đệ quy (mặc định ~1000 frames).

def trigger_stack_overflow(n: int) -> None:
    trigger_stack_overflow(n + 1)

try:
    trigger_stack_overflow(1)
except RecursionError as e:
    print("Caught RecursionError:", e)

# Ghi chú:
# - Với các bài toán đệ quy tính toán lặp lại, có thể tối ưu bằng cách lưu tạm kết quả đã tính vào từ điển (dict).
