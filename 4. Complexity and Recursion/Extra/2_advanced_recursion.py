import sys

# 1. Kỹ thuật Accumulator (Truyền đối số tích lũy - Top-down Accumulation)
# Thay vì chờ đệ quy chạm đáy rồi mới gỡ stack để tính toán ngược lên (Bottom-up),
# kỹ thuật Accumulator chuyển dần kết quả tính toán vào tham số của lời gọi hàm tiếp theo.
#
# Ví dụ: Đảo ngược chuỗi (String Reversal)
def reverse_string_acc(text: str, acc: str = "") -> str:
    """Đảo ngược chuỗi bằng tham số tích lũy (Accumulator Pattern)."""
    if not text:
        return acc
    return reverse_string_acc(text[:-1], acc + text[-1])

print("Reversed string with Accumulator:", reverse_string_acc("recursion"))  # noisrucer

# 2. Đệ quy thu thập cấu trúc dữ liệu (Accumulating Data Structures)
# Base case tạo danh sách [] duy nhất 1 lần, các frame cha gọi .append() in-place để tránh copy lại mảng:
def countup(number: int) -> list[int]:
    if number < 1:
        return []
    count_list: list[int] = countup(number - 1)
    count_list.append(number)
    return count_list

print("Countup list (in-place append): ", countup(5))  # [1, 2, 3, 4, 5]

# 3. Duyệt cấu trúc lồng nhau không rõ độ sâu (Deeply Nested Structures)
# Đệ quy phát huy ưu thế vượt trội khi xử lý dữ liệu cây, JSON hoặc danh sách lồng nhau bất kỳ cấp:
def calculate_nested_sum(data: list | int) -> int:
    """Tính tổng mọi số nguyên trong danh sách lồng nhau bất kỳ độ sâu."""
    if isinstance(data, int):  # Base case: Gặp phần tử đơn lẻ là số nguyên
        return data
    total = 0
    for item in data:  # Recursive case: Lặp qua từng phần tử con
        total += calculate_nested_sum(item)
    return total

nested_data = [1, [2, [3, 4]], 5, [6, [7, [8, 9]]]]
print("Sum of deeply nested list:      ", calculate_nested_sum(nested_data))  # 45

# 4. Giới hạn Call Stack & Bắt ngoại lệ RecursionError
# Python runtime thiết lập ngưỡng đệ quy mặc định (~1,000 frames) để bảo vệ bộ nhớ tiến trình:
current_limit = sys.getrecursionlimit()
print(f"\nCurrent recursion limit:        {current_limit}")

def trigger_stack_overflow(n: int) -> None:
    trigger_stack_overflow(n + 1)

try:
    trigger_stack_overflow(1)
except RecursionError as e:
    print("Caught RecursionError:          ", e)
