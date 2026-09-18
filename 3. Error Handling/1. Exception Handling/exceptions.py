# Các loại lỗi phổ biến (Built-in Exceptions) & Cải tiến Traceback
# - SyntaxError: Lỗi cú pháp
# - NameError: Dùng biến/hàm chưa định nghĩa (Python có 'Did you mean: ...?')
try:
    user_name = "Alice"
    print(usr_name)  # Did you mean: 'user_name'?
except NameError as e:
    print(f"NameError: {e}")

# - TypeError: Phép toán sai kiểu dữ liệu
try:
    result = 5 + "5"
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
    num.append(5)
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
# Cách 1: Bắt riêng lẻ từng khối except
try:
    number = int("abc")
    result = 10 / number
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")

# Cách 2: Sử dụng alias 'as e' để lấy thông báo lỗi
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# Cách 3: Gom nhiều ngoại lệ vào một tuple
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
