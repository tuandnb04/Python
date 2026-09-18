# 1. Toán tử so sánh (Trả về True / False)
print(3 > 4)    # False
print(3 == 4)   # False
print(3 != 4)   # True
print(3 <= 4)   # True

# 2. Câu lệnh điều kiện if - elif - else & từ khóa pass
age = 12

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # Output: You are a child

# 'pass' dùng làm placeholder khi chưa viết code cho block
if age < 0:
    pass

# 3. Ứng dụng thực tế: Ra quyết định phương tiện di chuyển (Decision Making)
distance_mi = 5
is_raining = False
has_bike = True
has_car, has_ride_share_app = False, False

if not distance_mi:
    can_travel = False
elif distance_mi <= 1:
    can_travel = not is_raining            # Đi bộ nếu không mưa
elif distance_mi <= 6:
    can_travel = has_bike and not is_raining # Đi xe đạp nếu có xe và không mưa -> True
else:
    can_travel = has_car or has_ride_share_app

print("Can travel:", can_travel)          # True