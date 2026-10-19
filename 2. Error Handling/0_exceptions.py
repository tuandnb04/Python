# 1. Cơ chế try - except cơ bản (Tránh sập chương trình)
# Khi mã trong khối try gặp lỗi, Python lập tức chuyển sang khối except thay vì dừng chương trình:
try:
    print(hello)  # type: ignore
except:
    print("hello is not a variable")

# 2. Các loại lỗi phổ biến (Built-in Exceptions)
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

# 3. Khối else (Chỉ chạy khi khối try KHÔNG có lỗi)
try:
    x = 10
except:
    print("Error")
else:
    print("No error")


# Phong cách EAFP (Easier to Ask for Forgiveness) vs LBYL:
# Thực hiện thao tác trong khối try và bắt ngoại lệ thay vì if-else kiểm tra trước:
def find_average(numbers: list[int | float]) -> float:
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0


print("Average [10, 20, 30]:", find_average([10, 20, 30]))  # 20.0
print("Average empty list:", find_average([]))  # 0 (ZeroDivisionError an toàn)

# 4. Khối finally (Luôn luôn chạy dù có lỗi hay không)
# Đặt sau tất cả các khối try - except - else:
try:
    f = open("demofile.txt", encoding="utf-8")
except:
    print("Cannot open")
    lines_added = 0
else:
    f.close()
    lines_added = 1
finally:
    print("Done")
    print(lines_added, "lines added")

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
# Câu lệnh 'with' tự động đảm bảo dọn dẹp tài nguyên (tệp tin, kết nối...) ngay cả khi có lỗi xảy ra:
# with open("data.txt", "w") as file:
#     file.write("Hello")

# Tự kích hoạt ngoại lệ thủ công với từ khóa 'raise':
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print("Caught manual raise:", e)

# Tự định nghĩa ngoại lệ riêng (Custom Exception - kế thừa từ Exception):
class InsufficientFundsError(Exception):
    """Ngoại lệ khi tài khoản không đủ số dư để thực hiện giao dịch."""
    pass

try:
    raise InsufficientFundsError("Balance is too low for this transaction!")
except InsufficientFundsError as e:
    print("Caught custom exception:", e)

# 5. Ghi log chuyên nghiệp với module logging & trích xuất Traceback:
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")


def calculate_discount(price: float, discount: float) -> float | None:
    logging.info(f"Calculating discount: price={price}, discount={discount}")
    try:
        if discount > 1.0 or discount < 0.0:
            raise ValueError("Discount must be between 0 and 1")
        return price * (1 - discount)
    except ValueError:
        # logging.exception tự động ghi log lỗi kèm theo Traceback chi tiết:
        logging.exception("Failed to calculate discount!")
        return None


calculate_discount(100, 0.2)
calculate_discount(100, 1.5)

