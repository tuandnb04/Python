"""
CÁC KỸ THUẬT DEBUGGING TRONG PYTHON (TỪ CƠ BẢN ĐẾN HIỆN ĐẠI)

1. print() & f-strings (Debug nhanh, xem biến và luồng thực thi)
2. breakpoint() tích hợp (Python 3.7+ PEP 553 - Thay thế pdb.set_trace())
3. Module pdb (Interactive Debugger)
4. Công cụ IDE Debugger (VS Code / PyCharm: Breakpoints, Step Over/Into/Out)
5. Module logging (Chuẩn công nghiệp thay thế print)
6. Module traceback (Trích xuất & hiển thị chi tiết stack trace)
"""

import sys
import logging
import traceback

# DÙNG PRINT() VÀ F-STRINGS (Kỹ thuật debug nhanh & đơn giản nhất)
def add(a, b):
    result = a + b
    print(f"[DEBUG] Input: a={a}, b={b}, result={result}")
    return result

add(10, 5)


# HÀM breakpoint() CÓ SẴN (Python 3.7+ - Chuẩn hiện đại thay thế pdb)
# - Không cần gõ `import pdb; pdb.set_trace()`.
# - Tự động mở interactive debugger khi chạy đến dòng này.
# - Trong môi trường Production, có thể tắt toàn bộ breakpoint() bằng cách đặt:
#   Environment variable: PYTHONBREAKPOINT=0 python script.py
def process_data(items):
    total = 0
    for item in items:
        # breakpoint()  # Bỏ comment dòng này khi muốn dừng chương trình để debug
        total += item
    return total

print("Total:", process_data([1, 2, 3]))


# DEBUG TRỰC QUAN BẰNG CÔNG CỤ IDE (VS Code / PyCharm Visual Debugger)
# - Breakpoints (F9): Đặt điểm dừng tại dòng cần kiểm tra (chấm đỏ ở lề trái)
# - Start Debugging (F5): Chạy chương trình ở chế độ debug
# - Step Over (F10): Thực thi dòng hiện tại và đi tới dòng kế tiếp
# - Step Into (F11): Đi vào chi tiết bên trong hàm được gọi
# - Step Out (Shift+F11): Chạy hết hàm hiện tại và quay về nơi gọi
# - Variables / Watch Panel: Theo dõi giá trị trực quan của các biến theo thời gian thực


# DÙNG MODULE logging (Giải pháp chuyên nghiệp thay thế print())
# Ưu điểm:
# - Phân cấp độ rõ ràng: DEBUG, INFO, WARNING, ERROR, CRITICAL
# - Dễ dàng bật/tắt theo level cấu hình hoặc ghi log ra file mà không sửa code
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] (%(filename)s:%(lineno)d): %(message)s",
    datefmt="%H:%M:%S"
)

def divide_numbers(a, b):
    logging.debug(f"Calling divide_numbers(a={a}, b={b})")
    try:
        result = a / b
        logging.info(f"Division result: {result}")
        return result
    except ZeroDivisionError:
        # logging.exception() sẽ tự động đính kèm toàn bộ Traceback vào log
        logging.exception("ZeroDivisionError encountered!")
        return None

divide_numbers(10, 2)
divide_numbers(10, 0)


# TRÍCH XUẤT & XỬ LÝ TRACEBACK VỚI MODULE traceback
def buggy_function():
    return 1 / 0

def caller():
    buggy_function()

try:
    caller()
except ZeroDivisionError:
    print("Caught exception, detailed traceback:")
    traceback.print_exc(file=sys.stdout)


# CÁC LỆNH PDB CƠ BẢN KHI VÀO TRÌNH DEBUGGER:
# n (next)     : Thực thi dòng hiện tại và đi đến dòng kế tiếp (không nhảy vào hàm)
# s (step)     : Nhảy vào chi tiết bên trong hàm đang gọi (Step into)
# c (continue) : Tiếp tục chạy chương trình đến breakpoint kế tiếp hoặc khi kết thúc
# p <tên_biến> : In giá trị của biến ra màn hình
# pp <biến>    : In cấu trúc dữ liệu phức tạp dạng đẹp (Pretty Print)
# whatis <tên> : Kiểm tra kiểu dữ liệu của biến hoặc hàm
# l (list)     : Hiển thị 11 dòng code xung quanh vị trí đang dừng
# q (quit)     : Thoát hoàn toàn khỏi debugger và dừng chương trình
