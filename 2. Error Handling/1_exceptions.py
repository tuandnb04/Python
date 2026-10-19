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
    result = 5 + "5"  # type: ignore
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
    num.append(5)  # type: ignore
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


# Phong cách EAFP (Easier to Ask for Forgiveness) vs LBYL:
# Thực hiện thao tác trong khối try và bắt ngoại lệ thay vì if-else kiểm tra trước:
def find_average(numbers: list[int | float]) -> float:
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


print("Average [10, 20, 30]:", find_average([10, 20, 30]))  # 20.0
print("Average empty list:", find_average([]))  # 0 (ZeroDivisionError an toàn)

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


# ExceptionGroup & except* (bắt nhóm ngoại lệ):
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
# Câu lệnh 'with' tự động đảm bảo dọn dẹp tài nguyên (file, kết nối, timer...) ngay cả khi có lỗi.
# Tự định nghĩa Context Manager thuần bằng class (__enter__ & __exit__) không cần import:
class ManagedResource:
    def __init__(self, name: str) -> None:
        self.name = name

    def __enter__(self):
        print(f"\n[Acquire] Resource '{self.name}' acquired successfully.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        print(f"[Release] Resource '{self.name}' released safely.")
        return False


with ManagedResource("DatabaseConnection"):
    print("  Executing safe operations inside with-block...")
