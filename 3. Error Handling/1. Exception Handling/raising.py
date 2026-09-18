# Câu lệnh 'raise': Kích hoạt ngoại lệ thủ công
def check_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

print("--- 1. Manual raise ---")
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

print("\n--- 2. Re-raising ---")
try:
    parse_config_entry("invalid_data")
except ValueError as e:
    print("Caller received re-raised error:", e)

# Custom Exception: Ngoại lệ tự định nghĩa
# 1. Dạng tối giản: Chỉ cần kế thừa Exception và dùng 'pass'
class ItemNotFoundError(Exception):
    """Ngoại lệ kế thừa toàn bộ tính năng mặc định của Exception."""
    pass

print("\n--- 3.1. Minimal Custom Exception ---")
try:
    raise ItemNotFoundError("Product with ID 404 does not exist")
except ItemNotFoundError as e:
    print("Caught:", e)

# 2. Custom Exception có thuộc tính mở rộng (Attributes & Metadata)
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance is ${balance}, requested ${amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

print("\n--- 3.2. Custom Exception with Attributes ---")
try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print("Account transaction error:", e)
    print(f"Details: Balance = {e.balance}, Requested = {e.amount}")

# 3. Phân cấp ngoại lệ theo Module/Dự án (Exception Hierarchy)
# Giúp caller có thể bắt chung lỗi của cả module (AppBaseError) hoặc bắt chi tiết lỗi con
class AppBaseError(Exception):
    """Lớp cha cho toàn bộ ngoại lệ trong ứng dụng."""
    pass

class DatabaseConnectionError(AppBaseError):
    pass

class DatabaseError(AppBaseError):
    pass

class RecordNotFoundError(DatabaseError):
    pass

print("\n--- 3.3. Exception Hierarchy ---")
try:
    raise DatabaseConnectionError("Failed to connect to primary replica")
except AppBaseError as e:
    print(f"Caught by AppBaseError handler: {type(e).__name__} -> {e}")

# Exception Chaining: Chuỗi ngoại lệ với từ khóa 'from' (PEP 3134)
# 1. Giữ nguyên nguyên nhân gốc (raise ... from err)
print("\n--- 4.1. Exception Chaining (with cause) ---")
try:
    try:
        raw_port = "abc"
        port = int(raw_port)
    except ValueError as err:
        raise RuntimeError("Server configuration failed") from err
except RuntimeError as e:
    print("Caught outer error:", e)
    print("Root cause (__cause__):", e.__cause__)

# 2. Ẩn nguyên nhân gốc (raise ... from None)
print("\n--- 4.2. Exception Chaining (suppress cause) ---")
try:
    try:
        val = int("xyz")
    except ValueError:
        raise KeyError("Invalid secret key") from None
except KeyError as e:
    print("Clean error:", e)
    print("Cause (__cause__):", e.__cause__)

# Câu lệnh 'assert': Kiểm tra điều kiện nội bộ khi debug/test
print("\n--- 5. Assert statement ---")
try:
    temperature_kelvin = -10
    assert temperature_kelvin >= 0, "Kelvin temperature cannot be negative!"
except AssertionError as e:
    print("AssertionError:", e)

# Gắn ghi chú chẩn đoán với Exception.add_note() (Python 3.11+ PEP 678)
print("\n--- 6. Exception.add_note() (Python 3.11+) ---")
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
