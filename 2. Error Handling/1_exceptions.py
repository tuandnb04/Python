# Các loại lỗi phổ biến (Built-in Exceptions) & Cải tiến Traceback
# - SyntaxError: Lỗi cú pháp
# - NameError: Dùng biến/hàm chưa định nghĩa (Python có 'Did you mean: ...?')
try:
    user_name = "Alice"
    print(usr_name)  # type: ignore # Did you mean: 'user_name'?
except NameError as e:
    print(f"NameError: {e}")

# - TypeError: Phép toán sai kiểu dữ liệu
try:
    result = 5 + "5" # type: ignore
except TypeError as e:
    print(f"TypeError: {e}")

# - IndexError: Vượt quá chỉ mục list/tuple
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

# - KeyError: Key không tồn tại trong dict
try:
    user_profile = {"id": 1}
    print(user_profile["email"])
except KeyError as e:
    print(f"KeyError: {e}")

# - AttributeError: Gọi thuộc tính không tồn tại
try:
    num = 42
    num.append(5) # type: ignore
except AttributeError as e:
    print(f"AttributeError: {e}")

# Cấu trúc đầy đủ: try - except - else - finally
# - try: Chứa đoạn code có khả năng phát sinh lỗi
# - except: Bắt và xử lý lỗi cụ thể
# - else: Chỉ chạy khi khối try không có lỗi
# - finally: Luôn luôn chạy trong mọi trường hợp (dọn dẹp tài nguyên)

# Ví dụ 1: Cơ bản try - except
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Triết lý Pythonic: EAFP vs LBYL & Zero-cost Exception (Python 3.11+)
# - LBYL (Look Before You Leap): Dùng if kiểm tra trước -> Tốn chi phí rẽ nhánh ở MỌI lần gọi.
# - EAFP (Easier to Ask for Forgiveness): Cứ thực hiện trong try, bắt ngoại lệ nếu xảy ra.
# Từ Python 3.11+, khối try là Zero-cost Exception (0 overhead khi chạy đúng).
def find_average(numbers: list[int | float]) -> float:
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0

print("Average [10, 20, 30]:", find_average([10, 20, 30]))  # 20.0
print("Average empty list:", find_average([]))              # 0 (ZeroDivisionError an toàn)

# Ví dụ 2: Đầy đủ try - except - else - finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("Division successful:", x)
finally:
    print("This block always runs.")

# Bắt nhiều ngoại lệ (riêng lẻ hoặc dùng tuple)
# Bắt riêng lẻ từng khối except:
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")

# Sử dụng alias 'as e' để lấy thông báo lỗi:
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# Gom nhiều ngoại lệ vào một tuple:
try:
    number = int("0")
    result = 10 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")

# ExceptionGroup & except* (Python 3.11+ PEP 654)
# Bắt nhiều lỗi đồng thời khi chạy tác vụ song song
def simulate_concurrent_tasks():
    errors = [
        ValueError("Invalid GitHub URL format"),
        FileNotFoundError("Repository config missing"),
        TimeoutError("Connection timed out during git clone")
    ]
    raise ExceptionGroup("Multiple pipeline errors occurred", errors)

try:
    simulate_concurrent_tasks()
except* ValueError as e:
    print("Caught ValueError group:", e.exceptions)
except* (FileNotFoundError, TimeoutError) as e:
    print("Caught File/Network error group:", e.exceptions)



# Context Managers & Cú pháp 'with': Quản lý tài nguyên an toàn (thay thế try...finally)
# Câu lệnh 'with' tự động đảm bảo dọn dẹp tài nguyên (file, socket, timer...) ngay cả khi có lỗi.

# Cách 1: Tạo Context Manager bằng Class (__enter__ và __exit__)
class ManagedResource:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"[Resource] Acquiring: {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[Resource] Releasing: {self.name}")
        # Trả về True nếu muốn triệt tiêu (suppress) ngoại lệ, False để tiếp tục ném lỗi
        return False

with ManagedResource("Database Connection") as res:
    print(f"Working with {res.name}...")

# Cách 2: Tạo Context Manager siêu ngắn gọn bằng @contextmanager từ thư viện contextlib
from contextlib import contextmanager

@contextmanager
def timer_scope(task_name):
    import time
    start = time.perf_counter()
    print(f"\n[Timer] Bat dau task: '{task_name}'")
    try:
        yield
    finally:
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[Timer] Task '{task_name}' hoan thanh trong {elapsed:.2f} ms")

with timer_scope("Processing items"):
    _ = sum(i * i for i in range(100_000))
