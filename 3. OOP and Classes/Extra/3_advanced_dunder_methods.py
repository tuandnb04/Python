# ADVANCED DUNDER / MAGIC METHODS
#
# Các phương thức đặc biệt nâng cao trong Python:
# 1. Custom Sequences / Container protocol (__getitem__, __setitem__, __delitem__, __contains__)
# 2. Callable objects (__call__ biến instance thành hàm)
# 3. Context Managers (__enter__, __exit__ hỗ trợ câu lệnh with)

class CustomList:
    def __init__(self, initial_data: list | None = None) -> None:
        self._data: list = list(initial_data) if initial_data else []

    # Cho phép đọc phần tử qua chỉ số hoặc slice: obj[i], obj[start:stop]
    def __getitem__(self, index: int | slice):
        return self._data[index]

    # Cho phép gán giá trị theo chỉ số: obj[i] = value
    def __setitem__(self, index: int, value) -> None:
        self._data[index] = value

    # Cho phép xóa phần tử theo chỉ số: del obj[i]
    def __delitem__(self, index: int) -> None:
        del self._data[index]

    # Cho phép kiểm tra phần tử tồn tại bằng toán tử `in`: item in obj
    def __contains__(self, item) -> bool:
        return item in self._data

    def __len__(self) -> int:
        return len(self._data)


cl = CustomList(["Python", "Rust", "Go"])
print("cl[1]:", cl[1])               # Rust
print("Is 'Python' in cl?", "Python" in cl)  # True

cl[1] = "TypeScript"
print("After updating cl[1]:", cl[1])   # TypeScript

del cl[0]
print("After deleting cl[0], length is:", len(cl))      # 2


# __call__ cho phép đối tượng instance có thể được gọi như một function: obj()
# Rất hữu ích khi cần duy trì state giữa các lần gọi (Stateful Function/Closure alternative).

class ExecutionCounter:
    def __init__(self, function_name: str) -> None:
        self.function_name = function_name
        self.calls: int = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Function [{self.function_name}] called (call #{self.calls})")
        return args, kwargs


counter = ExecutionCounter("fetch_api")
counter(endpoint="/users")
counter(endpoint="/orders")
print("Total invocations:", counter.calls)


# Cho phép class sử dụng với cú pháp `with ... as ...:`
# Tự động dọn dẹp tài nguyên (kết nối DB, lock, file) kể cả khi có ngoại lệ xảy ra.

class DatabaseSession:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def __enter__(self):
        print(f"[{self.db_name}] Database connection established.")
        return self

    def query(self, sql: str) -> str:
        return f"Executing '{sql}' on {self.db_name}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[{self.db_name}] Closing database connection and cleaning up resources.")
        # Trả về True nếu muốn chặn ngoại lệ không bị nổi bọt ra ngoài, ngược lại trả về None/False
        return False


with DatabaseSession("ProductionDB") as session:
    print(session.query("SELECT * FROM users LIMIT 10"))
