# Decorators trong Python (Hàm bao bọc và mở rộng chức năng)
# - Dựa trên kiến thức: Hàm lồng nhau (Nested Functions), *args, **kwargs và functools.wraps
import functools

# Cấu trúc một Decorator chuẩn hiện đại (Luôn dùng @functools.wraps)
# => TẠI SAO PHẢI DÙNG @functools.wraps(func)?
#    + Nếu không có: Hàm sau khi bọc sẽ bị mất __name__, __doc__ và biến thành 'wrapper'.
#    + Chuẩn hiện đại: Bảo toàn toàn bộ metadata gốc và hỗ trợ công cụ debug/profiler.
def my_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}")
        return result
    return wrapper

# Áp dụng Decorator bằng cú pháp @
# Cú pháp @my_logger tương đương với việc gán lại: greet = my_logger(greet)
@my_logger
def greet(name, title="Mr."):
    return f"Hello, {title} {name}"

@my_logger
def add(a, b):
    return a + b

print(greet("Alice", title="Dr."))
print("Sum:", add(10, 20))
