# Thuật toán Luhn (Luhn Algorithm / Modulo 10 Checksum)
# - Chuẩn quốc tế: ISO/IEC 7812-1
# - Ứng dụng thực tế:
#   + Xác thực số thẻ thanh toán (Visa, MasterCard, Amex, Discover,...)
#   + Xác thực số IMEI của thiết bị di động
#   + Mã số định danh cá nhân / Thẻ căn cước tại nhiều quốc gia
# - Độ phức tạp:
#   + Thời gian (Time Complexity): O(n) với n là số chữ số.
#   + Không gian (Space Complexity): O(n) với slicing hoặc O(1) với vòng lặp đơn.
#
# - Nguyên lý hoạt động:
#   Duyệt các chữ số từ PHẢI sang TRÁI (bắt đầu từ chữ số kiểm tra - check digit ở cuối cùng):
#   1. Giữ nguyên các chữ số ở vị trí lẻ (vị trí 1, 3, 5,... tính từ phải sang).
#   2. Nhân đôi (x2) các chữ số ở vị trí chẵn (vị trí 2, 4, 6,... tính từ phải sang).
#   3. Nếu kết quả nhân đôi > 9, cộng 2 chữ số lại (tương đương với việc lấy số đó trừ 9).
#      Ví dụ: 7 * 2 = 14 -> 1 + 4 = 5 (hoặc 14 - 9 = 5).
#   4. Tính tổng tất cả các chữ số sau khi xử lý.
#   5. Nếu tổng chia hết cho 10 (total % 10 == 0), số thẻ hợp lệ!


def verify_luhn(card_number: str) -> bool:
    """
    Kiểm tra tính hợp lệ của số thẻ theo thuật toán Luhn (Cách tiếp cận Pythonic với Slicing).
    """
    if not isinstance(card_number, str):
        return False

    # 1. Làm sạch dữ liệu: loại bỏ khoảng trắng và dấu gạch ngang
    clean = card_number.replace("-", "").replace(" ", "")

    # 2. Xử lý ngoại lệ & Edge cases:
    # - Chuỗi rỗng hoặc chứa ký tự không phải chữ số: loại bỏ ngay
    # - Thẻ ngân hàng thực tế có độ dài từ 13 đến 19 chữ số
    if not clean.isdigit() or len(clean) < 13 or len(clean) > 19:
        return False

    # Chuyển chuỗi thành danh sách số nguyên
    digits = [int(c) for c in clean]

    # 3. Kỹ thuật Negative Slicing (Duyệt từ phải sang trái):
    # - Vị trí lẻ từ phải: digits[-1::-2] (ví dụ: chỉ số -1, -3, -5,...)
    check_digits = digits[-1::-2]

    # - Vị trí chẵn từ phải: digits[-2::-2] (ví dụ: chỉ số -2, -4, -6,...)
    # Mẹo toán học: d * 2 - 9 if d * 2 > 9 else d * 2
    # Vì với số nhân đôi từ 10 đến 18, tổng 2 chữ số (1 + x) luôn bằng chính nó trừ 9.
    doubled_digits = [d * 2 - 9 if d * 2 > 9 else d * 2 for d in digits[-2::-2]]

    total = sum(check_digits) + sum(doubled_digits)
    return total % 10 == 0


def verify_luhn_optimized(card_number: str) -> bool:
    """
    Phiên bản tối ưu bộ nhớ: O(1) Space Complexity.
    Duyệt một vòng lặp ngược trực tiếp, không tạo mảng phụ.
    """
    if not isinstance(card_number, str):
        return False

    clean = card_number.replace("-", "").replace(" ", "")
    if not clean.isdigit() or len(clean) < 13 or len(clean) > 19:
        return False

    total = 0
    # Cờ đảo để xác định chữ số hiện tại có cần nhân đôi hay không
    # Chữ số đầu tiên từ phải sang (check digit) không nhân đôi (is_even_position = False)
    is_even_position = False

    for c in reversed(clean):
        digit = ord(c) - ord("0")

        if is_even_position:
            digit *= 2
            if digit > 9:
                digit -= 9

        total += digit
        is_even_position = not is_even_position

    return total % 10 == 0


def detect_card_brand(card_number: str) -> str:
    """
    Nhận diện nhà phát hành thẻ (IIN/BIN - Issuer Identification Number)
    kết hợp xác thực tính toàn vẹn bằng thuật toán Luhn.
    """
    if not verify_luhn(card_number):
        return "Invalid Card"

    clean = card_number.replace("-", "").replace(" ", "")
    length = len(clean)

    # Visa: Bắt đầu bằng 4, độ dài 13, 16 hoặc 19
    if clean.startswith("4") and length in (13, 16, 19):
        return "Visa"

    # Mastercard: 51-55 hoặc 2221-2720, độ dài 16
    if length == 16:
        prefix_2 = int(clean[:2])
        prefix_4 = int(clean[:4])
        if (51 <= prefix_2 <= 55) or (2221 <= prefix_4 <= 2720):
            return "MasterCard"

    # American Express (Amex): Bắt đầu bằng 34 hoặc 37, độ dài 15
    if length == 15 and clean[:2] in ("34", "37"):
        return "American Express"

    # Discover: Bắt đầu bằng 6011, 65, hoặc trong dải 644-649, độ dài 16
    if length == 16 and (clean.startswith("6011") or clean.startswith("65") or 644 <= int(clean[:3]) <= 649):
        return "Discover"

    return "Valid (Unknown Brand)"


if __name__ == "__main__":
    test_cases = [
        ("4532-0150-1234-5671", "Valid Visa"),
        ("4532 0150 1234 5670", "Invalid check digit"),
        ("5424-1801-2345-6789", "Valid MasterCard"),
        ("3782-822463-10005", "Valid American Express"),
        ("6011-0009-9013-9424", "Valid Discover"),
        ("", "Empty string"),
        ("   ", "Whitespace only"),
        ("4532-ABCD-1234-5670", "Contains letters"),
        ("0", "Single digit"),
        ("1234567890123", "Bad checksum (13 digits)"),
    ]

    print("=" * 76)
    print(f"{'Card Number':<24} | {'Description':<24} | {'Luhn':<7} | {'Brand'}")
    print("=" * 76)

    for card, desc in test_cases:
        is_valid_slicing = verify_luhn(card)
        is_valid_optimized = verify_luhn_optimized(card)

        # Đảm bảo 2 cách cài đặt cho kết quả đồng nhất
        assert is_valid_slicing == is_valid_optimized, f"Mismatch on card: {card}"

        brand = detect_card_brand(card)
        status = "PASS" if is_valid_slicing else "FAIL"

        print(f"{card:<24} | {desc:<24} | {status:<7} | {brand}")

    print("=" * 76)
    print("All test cases passed successfully!")
