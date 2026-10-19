from datetime import date, datetime, timedelta

# 1. Tạo đối tượng date (chỉ ngày) và datetime (ngày và giờ)
target_date = date(2027, 5, 17)
print("Date:", target_date)

target_datetime = datetime(2027, 5, 17, 14, 30)
print("Datetime:", target_datetime)

# 2. Phép toán thời gian với timedelta
# timedelta dùng để cộng hoặc trừ một khoảng thời gian (ngày, tuần...):
base_date = datetime(2020, 5, 17)
future_date = base_date + timedelta(weeks=3)
print("After 3 weeks:", future_date)

# 3. Truy xuất thuộc tính ngày và giờ
# Lấy năm, tháng, ngày:
date_obj = datetime(2026, 11, 18)
print("Year:", date_obj.year)
print("Month:", date_obj.month)
print("Day:", date_obj.day)

# Lấy giờ, phút, giây:
time_obj = datetime(2026, 12, 25, 10, 30, 0)
print("Hour:", time_obj.hour)
print("Minute:", time_obj.minute)
print("Second:", time_obj.second)

# 4. Thay đổi thông tin bằng phương thức replace()
# replace() trả về đối tượng datetime mới, không thay đổi đối tượng ban đầu:
original = datetime(2026, 1, 20)
updated = original.replace(year=2027)
print("Original:", original)
print("Updated:", updated)

# 5. Định dạng ngày giờ thành chuỗi với strftime() (String Format Time)
# Dùng các mã định dạng (%d: ngày, %m: tháng, %Y: năm 4 số, %B: tên tháng, %A: thứ, %I:%M %p: giờ 12h):
d = datetime(2026, 11, 18, 17, 1)
print("Custom format:", d.strftime("%d/%m/%Y"))
print("Text with date:", d.strftime("The date is %B %d"))
print("Weekday (%A):", d.strftime("%A"))
print("Month (%B / %b):", d.strftime("%B"), "/", d.strftime("%b"))
print("Time 12h (%I:%M %p):", d.strftime("%I:%M %p"))

# 6. Múi giờ UTC chuẩn hiện đại (Python 3.12+ thay thế datetime.utcnow() đã bị deprecate)
from datetime import timezone

now_utc = datetime.now(timezone.utc)
print("Now UTC (timezone.utc):", now_utc)
