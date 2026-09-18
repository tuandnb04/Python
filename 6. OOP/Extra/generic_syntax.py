# Cú pháp Generic mới & type Statement trong Python 3.12+ (PEP 695)

# => TẠI SAO CÚ PHÁP GENERIC MỚI LÀ CẢI TIẾN LỚN?
#    + Không cần phải import và khai báo `TypeVar('T')` thủ công rườm rà.
#    + Cú pháp `[T]` trực quan, quen thuộc với các lập trình viên hiện đại (giống TypeScript, Rust, C++).
#    + Tối ưu hóa hiệu năng kiểm tra kiểu (Type Checking) ở mức sâu hơn.

# 1. Type Alias Statement với từ khóa 'type'
type Coordinates = tuple[float, float]
type JSONDict = dict[str, str | int | bool]

point: Coordinates = (10.5, 20.8)
data: JSONDict = {"status": "ok", "count": 42}
print("Coordinates:", point)
print("JSONDict:", data)

# 2. Generic Function với cú pháp [T] trực tiếp (không cần TypeVar)
def get_first_element[T](items: list[T]) -> T:
    return items[0]

first_str = get_first_element(["Flask", "Django", "FastAPI"])
first_int = get_first_element([100, 200, 300])
print("First string:", first_str)
print("First int:", first_int)

# 3. Generic Class với cú pháp [T]
class SimpleContainer[T]:
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

container = SimpleContainer("Code Graph Node")
print("Container value:", container.get_value())
