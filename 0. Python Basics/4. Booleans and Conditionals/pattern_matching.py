# Structural Pattern Matching (match - case) trong Python 3.10+ (PEP 634)
# => TẠI SAO MATCH-CASE TỐT HƠN CHUỖI IF-ELIF-ELSE DÀI?
#    + Cú pháp rõ ràng, phân nhánh trực quan theo cấu trúc dữ liệu.
#    + Hỗ trợ 'Guards' (điều kiện if bổ sung) giúp gom nhóm logic gọn gàng hơn.

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
        print("Unknown Status Code")       # case _ tương đương 'else'

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
