# 1. Toán tử so sánh (<, >, ==, !=, <=, >=) và thành viên (in, not in)
# Đánh giá biểu thức và trả về một giá trị bool (True hoặc False):
age = 18
print("Comparison (age >= 18):", age >= 18)                    # True (so sánh số)
print("String compare:", "Banana" == "Cherry")                 # False (so sánh chuỗi)
print("Membership ('a' in 'banana'):", "a" in "banana")         # True (nằm trong)
print("Membership ('z' not in 'banana'):", "z" not in "banana") # True (không nằm trong)

# 2. Hàm kiểm tra bool() và các giá trị Falsy (Truthy & Falsy)
# Hầu hết mọi giá trị đều là True, ngoại trừ các giá trị 'rỗng' sau đây trả về False:
# 0, "" (chuỗi rỗng), None, [] (list rỗng), () (tuple rỗng), {} (dict rỗng)
print("bool('hello'):", bool("hello"))             # True
print("bool(0):      ", bool(0))                   # False
print("bool(''):     ", bool(""))                  # False

# 3. Câu lệnh if và cấu trúc if - else (Quy tắc thụt lề Indentation)
# Python dùng thụt lề (4 dấu cách) để xác định khối lệnh thay vì cặp ngoặc {}.
# Từ khóa else viết cùng cấp thụt lề với if, chạy khi điều kiện trả về False:
user_age = 15

if user_age >= 18:
    print("Adult")
else:
    print("Minor")

# 4. Cấu trúc nhiều nhánh if - elif - else (elif viết tắt của "else if")
# Python kiểm tra từ trên xuống dưới, chỉ chạy khối đầu tiên thỏa mãn rồi bỏ qua phần còn lại.
# Mệnh đề else ở cuối là tùy chọn, chỉ chạy khi không có nhánh nào khớp:
score = 85

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

# 5. Câu lệnh if lồng nhau (Nested if):
# Câu lệnh if nằm bên trong một if khác gọi là Nested if:
person_age = 20
if person_age > 18:
    print("Adult")
    if person_age > 65:
        print("Senior")
    else:
        print("Working age")

# Dùng từ khóa 'and' để gộp điều kiện ngắn gọn trên 1 dòng:
if person_age > 18 and person_age < 65:
    print("Working age (via and)")
else:
    print("Not working")

# 6. Toán tử logic kết hợp điều kiện (and, or, not):
has_ticket = True
has_vip_pass = False

if has_ticket or has_vip_pass:
    print("Can enter event (or)!")

print("not has_ticket:", not has_ticket)  # False

# 7. Biểu thức 3 ngôi - if-else trên 1 dòng (Ternary Expression)
# Cú pháp: val = a if condition else b (Đúng lấy a, sai lấy b):
age = 48
s = "Yes" if age > 70 else "No"
print("Ternary result (s):", s)

# 8. Câu lệnh pass trong khối if trống:
# Dùng làm placeholder giữ chỗ khi chưa viết mã, tránh lỗi SyntaxError:
if person_age > 100:
    pass

# 9. So khớp mẫu với match - case (Python 3.10+):
# So sánh giá trị với các mẫu và thực thi khối mã đầu tiên trùng khớp:
http_status = 404
match http_status:
    case 200:
        print("Response: OK")
    case 404:
        print("Response: Not Found")
    case _:
        # Dấu gạch dưới '_' đại diện cho trường hợp mặc định (chạy khi không khớp case nào):
        print("Response: Other")
