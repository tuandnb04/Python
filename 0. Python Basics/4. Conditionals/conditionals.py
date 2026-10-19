# Truthy và Falsy (Kiểm tra bằng hàm bool)
# Falsy: 0, 0.0, '', None, False, và các container rỗng ([], (), {}, set()) | Truthy: Các giá trị còn lại (1, 'Hello', [1])
print(bool(0), bool(''), bool([]), bool('Hello'), bool(1))  # False False False True True


# Toán tử logic (Logical Operators: and, or, not)
# Dùng để kết hợp hoặc đảo ngược các biểu thức điều kiện:
# - 'and': Trả về True nếu CẢ HAI điều kiện đều đúng
# - 'or' : Trả về True nếu ÍT NHẤT MỘT trong các điều kiện đúng
# - 'not': Đảo ngược giá trị logic (True -> False, False -> True)
x_log = 5
print("Logical and (x > 0 and x < 10):", x_log > 0 and x_log < 10)    # True
print("Logical or  (x < 5 or x > 10): ", x_log < 5 or x_log > 10)     # False
print("Logical not (not(x > 3 and x < 10)):", not (x_log > 3 and x_log < 10))  # False

# Cơ chế Short-circuiting (Đánh giá đoản mạch nâng cao):
# - 'and': Dừng lại và trả về falsy đầu tiên hoặc giá trị cuối cùng nếu tất cả đều truthy
# - 'or' : Dừng lại và trả về truthy đầu tiên hoặc giá trị cuối cùng nếu tất cả đều falsy
print("Short-circuit and:", True and 25)  # 25
print("Short-circuit or: ", 19 or False)  # 19
print("Short-circuit not:", not '', not 'Hi')  # True False

# Toán tử so sánh (Comparison Operators - Luôn trả về Boolean True / False):
# - '==' (Equal): So sánh bằng
# - '!=' (Not equal): So sánh khác
# - '>'  (Greater than): Lớn hơn
# - '<'  (Less than): Nhỏ hơn
# - '>=' (Greater than or equal to): Lớn hơn hoặc bằng
# - '<=' (Less than or equal to): Nhỏ hơn hoặc bằng
x_cmp, y_cmp = 5, 3
print("x == y:", x_cmp == y_cmp)  # False
print("x != y:", x_cmp != y_cmp)  # True
print("x > y: ", x_cmp > y_cmp)   # True
print("x < y: ", x_cmp < y_cmp)   # False
print("x >= y:", x_cmp >= y_cmp)  # True
print("x <= y:", x_cmp <= y_cmp)  # False

# Chaining Comparison Operators (So sánh chuỗi liên tiếp):
# Python cho phép viết gộp các phép so sánh liên tiếp một cách ngắn gọn (Pythonic):
# Cú pháp `1 < x < 10` tương đương logic với `1 < x and x < 10`
print("Chaining (1 < 5 < 10):      ", 1 < x_cmp < 10)  # True
print("Equivalent 'and' logic:    ", 1 < x_cmp and x_cmp < 10)  # True
print("Range check (10 <= 5 <= 20):", 10 <= x_cmp <= 20)  # False

# Toán tử danh tính (Identity Operators: is, is not)
# - 'is'    : Trả về True nếu cả hai biến cùng trỏ tới MỘT đối tượng trong bộ nhớ (cùng id())
# - 'is not': Trả về True nếu cả hai biến trỏ tới các đối tượng KHÁC NHAU
# - Phân biệt giữa 'is' (Identity) và '==' (Equality):
#   + '==' : So sánh GIÁ TRỊ (Value) của hai đối tượng
#   + 'is' : So sánh ĐỊNH DANH (Identity trong RAM) - hai biến có cùng trỏ tới MỘT đối tượng không (id(x) == id(y))
# - Chuẩn PEP 8: Luôn dùng 'is' hoặc 'is not' khi kiểm tra với None:
val_none = None
print("Identity val_none is None:    ", val_none is None)      # True
print("Identity val_none is not None:", val_none is not None)  # False

# Ví dụ so sánh hai biến trỏ cùng một chuỗi / đối tượng:
str_a = "Python"
str_b = str_a
str_c = "Py" + "thon"
print("Identity str_a is str_b:      ", str_a is str_b)        # True (cùng trỏ đến một đối tượng)
print("Equality str_a == str_c:      ", str_a == str_c)        # True (cùng giá trị nội dung)

# Toán tử thành viên (Membership Operators: in, not in)
# Dùng để kiểm tra sự tồn tại của chuỗi con trong chuỗi văn bản (String - Có phân biệt hoa thường):
# - 'in'    : Trả về True nếu giá trị có xuất hiện trong chuỗi
# - 'not in': Trả về True nếu giá trị KHÔNG xuất hiện trong chuỗi
text = "Hello World"
print("Is 'H' in text:               ", "H" in text)                 # True
print("Is 'World' in text:           ", "World" in text)             # True
print("Is 'hello' in text:           ", "hello" in text)             # False (do phân biệt hoa thường)
print("Is 'z' not in text:           ", "z" not in text)             # True

# Lưu ý về so sánh Boolean và Số nguyên:
# Trong Python, False == 0 và True == 1 đều là True khi so sánh giá trị.
# Để phân biệt chính xác False với 0, ta dùng toán tử identity 'is' hoặc kiểm tra 'type(x) is bool':
val = 0
print(False == val, True == 1)  # type: ignore # True True
print(False is val)  # type: ignore # False (False và 0 là hai đối tượng khác nhau)
print(type(False) is bool)  # True

# Đếm số điều kiện thỏa mãn bằng phép cộng Boolean:
# Ví dụ kiểm tra có đúng 2 trong 3 số là số dương:
a, b, c = 5, -2, 3
is_two_positive = (a > 0) + (b > 0) + (c > 0) == 2
print("Are exactly two positive:", is_two_positive)  # True

# Phân biệt isinstance() vs type() is (Kiểm tra kiểu dữ liệu):
# - isinstance(True, int) trả về True vì bool được coi như dạng số nguyên trong Python.
# - type(True) is int trả về False vì kiểm tra chính xác kiểu dữ liệu thuần túy.
print("isinstance(True, int):", isinstance(True, int))  # True
print("type(True) is int:    ", type(True) is int)  # False (chính xác kiểu số nguyên)

# Kiểm tra an toàn trước khi xử lý (không nhầm lẫn True/False với 1/0):
test_val = True
if type(test_val) is int:
    print("Exact integer:", test_val)
else:
    print("Not an integer (type is bool or other):", type(test_val).__name__)

# Câu lệnh điều kiện if - elif - else & từ khóa pass
# Quy tắc thụt lề (Indentation):
# - Python không dùng cặp ngoặc `{}` như C/Java mà dùng khoảng trắng thụt lề để xác định khối mã (Code Block).
# - Chuẩn PEP 8: Dùng 4 khoảng trắng (4 spaces) cho mỗi cấp độ thụt lề. Tuyệt đối không trộn Tab và Space.
# - Quên thụt lề sau dấu `:` hoặc thụt lề sai mức sẽ gây lỗi: IndentationError.
# - Khối lệnh 1 dòng (One-liner if): Hợp lệ cho lệnh đơn giản:
if 5 > 2: print("Five is greater than two!")

age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')

# Toán tử 3 ngôi (Ternary Operator / Conditional Expression):
# - Cú pháp: val_if_true if condition else val_if_false
# - Bản chất trong Python: Đây là biểu thức điều kiện (Conditional Expression) trả về giá trị,
#   không phải một toán tử ký hiệu riêng (như '?:' trong C/C++/Java/JS).
status = 'Adult' if age >= 18 else 'Minor'
print("Ternary status:", status)  # 'Minor'

# - Toán tử 3 ngôi lồng nhau nối tiếp thay thế cho elif (Chained Ternary Expression):
num = 6
day_type = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "Weekday"
print("Chained ternary result:", day_type)  # 'Sat'

# Toán tử Walrus (:=) trong câu lệnh điều kiện (Assignment Expression - Python 3.8+):
# Vừa gán giá trị cho biến vừa kiểm tra điều kiện trong cùng một biểu thức
text_sample = "Antigravity"
if (count := len(text_sample)) > 5:
    print(f"String has {count} characters (evaluated with walrus operator)")

# 'pass' dùng làm placeholder khi chưa viết code cho block
if age < 0:
    pass

# if lồng nhau (Nested if)
if age < 18:
    if age < 13:
        print('Child under 13')

# Cấu trúc if - elif - else nhiều nhánh với toán tử logic (and, or, not)
score = 75
if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 50:
    grade = 'C'
else:
    grade = 'F'
print("Grade result:", grade)  # 'B'

# Structural Pattern Matching (match - case)
# Khớp giá trị cụ thể (Literal Matching)
status_code = 404

match status_code:
    case 200:
        print("Success: OK")
    case 400:
        print("Error: Bad Request")
    case 404:
        print("Error: Not Found")
    case 500:
        print("Error: Internal Server Error")
    case _:
        print("Unknown Status Code")  # case _ tương đương 'else'

# Khớp mẫu với điều kiện bổ sung (Guards với từ khóa 'if')
score = 85

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 80:
        print("Grade: B")
    case s if s >= 70:
        print("Grade: C")
    case _:
        print("Grade: F")

# Khớp mẫu với nhiều giá trị (OR pattern với '|')
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Unknown day")

# Khớp mẫu kết hợp gán biến (as pattern)
role = "admin"

match role:
    case "admin" | "superuser" as privileged_role:
        print(f"Privileged access granted for: {privileged_role}")
    case "guest":
        print("Guest access only")
    case _:
        print("Standard user access")
