# Câu lệnh 'raise': Kích hoạt ngoại lệ thủ công
def check_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Caught ValueError:", e)

# Re-raising: Bắt lỗi để xử lý trung gian rồi ném tiếp
def parse_config_entry(data):
    try:
        return int(data)
    except ValueError:
        print("[Internal Log]: Failed to parse integer, re-raising to caller...")
        raise

try:
    parse_config_entry("invalid_data")
except ValueError as e:
    print("Caller received re-raised error:", e)

# Custom Exception: Ngoại lệ tự định nghĩa
# Dạng tối giản: Chỉ cần kế thừa Exception và dùng 'pass'
class ItemNotFoundError(Exception):
    """Ngoại lệ kế thừa toàn bộ tính năng mặc định của Exception."""
    pass

try:
    raise ItemNotFoundError("Product with ID 404 does not exist")
except ItemNotFoundError as e:
    print("Caught:", e)

# Custom Exception với thông điệp chi tiết:
class InsufficientFundsError(Exception):
    """Ngoại lệ khi tài khoản không đủ số dư để thực hiện giao dịch."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Insufficient funds: Balance is ${balance}, requested ${amount}")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print("Account transaction error:", e)

# Phân cấp nhóm ngoại lệ theo Module/Dự án:
# Giúp caller có thể bắt chung lỗi của cả nhóm (AppBaseError) hoặc bắt chi tiết từng loại lỗi
class AppBaseError(Exception):
    """Ngoại lệ gốc cho toàn bộ module ứng dụng."""
    pass

class DatabaseConnectionError(AppBaseError):
    pass

class DatabaseError(AppBaseError):
    pass

class RecordNotFoundError(DatabaseError):
    pass

try:
    raise DatabaseConnectionError("Failed to connect to primary replica")
except AppBaseError as e:
    print(f"Caught by AppBaseError handler: {type(e).__name__} -> {e}")

# Exception Chaining: Chuỗi ngoại lệ với từ khóa 'from' (PEP 3134)
# Giữ nguyên nguyên nhân gốc (raise ... from err)
try:
    try:
        raw_port = "abc"
        port = int(raw_port)
    except ValueError as err:
        raise RuntimeError("Server configuration failed") from err
except RuntimeError as e:
    print("Caught outer error:", e)
    print("Root cause (__cause__):", e.__cause__)

# Ẩn nguyên nhân gốc (raise ... from None)
try:
    try:
        val = int("xyz")
    except ValueError:
        raise KeyError("Invalid secret key") from None
except KeyError as e:
    print("Clean error:", e)
    print("Cause (__cause__):", e.__cause__)

# Câu lệnh 'assert': Kiểm tra điều kiện nội bộ khi debug/test
try:
    temperature_kelvin = -10
    assert temperature_kelvin >= 0, "Kelvin temperature cannot be negative!"
except AssertionError as e:
    print("AssertionError:", e)

# Gắn ghi chú chẩn đoán với Exception.add_note() (Python 3.11+ PEP 678)
try:
    try:
        raise ValueError("Database connection failed")
    except ValueError as e:
        e.add_note("Context: Connecting to PostgreSQL at 192.168.1.10")
        e.add_note("Timeout limit: 30 seconds")
        raise
except ValueError as err:
    print("Main exception:", err)
    print("Attached notes (__notes__):")
    for note in getattr(err, "__notes__", []):
        print(f"  * {note}")

# Gom nhóm và ném nhiều ngoại lệ cùng lúc với ExceptionGroup (Python 3.11+ PEP 654)
# - Bài toán thực tế (Batch Validation): Thay vì dừng lại ngay ở lỗi đầu tiên,
#   ta thu thập toàn bộ các lỗi vi phạm dữ liệu rồi ném ra cùng một lúc.
def validate_user_registration(username: str, email: str, age: int) -> None:
    errors: list[Exception] = []
    if len(username) < 3:
        errors.append(ValueError(f"Username '{username}' is too short (min 3 chars)"))
    if "@" not in email:
        errors.append(ValueError(f"Email '{email}' is missing '@'"))
    if age < 18:
        errors.append(PermissionError(f"Age {age} is below minimum requirement (18+)"))

    if errors:
        raise ExceptionGroup("User registration validation failed", errors)

try:
    validate_user_registration(username="al", email="invalid-email", age=16)
except ExceptionGroup as eg:
    print(f"Validation failed with {len(eg.exceptions)} errors:")
    for err in eg.exceptions:
        print(f"  - [{type(err).__name__}]: {err}")

# Ghi chú: Để tìm hiểu chi tiết cách BẮT và XỬ LÝ từng loại lỗi song song bằng cú pháp `except*`,
# tham khảo file: 2. Error Handling/1_exceptions.py


