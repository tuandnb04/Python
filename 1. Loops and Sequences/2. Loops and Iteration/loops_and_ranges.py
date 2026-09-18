# Khái niệm Iterable: Là đối tượng có thể lặp qua từng phần tử một (List, Tuple, String, Range, Dict, Set)

# Hàm range(start, stop, step) - Tạo dãy số nguyên (chỉ có 'stop' là bắt buộc)
# - range object là BẤT BIẾN (Immutable) và sinh số dạng lười (lazy), tiết kiệm RAM tối đa.
# - Dùng list(range(...)) nếu muốn chuyển đổi thành list các số nguyên hoàn chỉnh.
print("range(3):", list(range(3)))              # [0, 1, 2] (từ 0 đến trước 3: chỉ truyền 'stop')
print("range(1, 5):", list(range(1, 5)))        # [1, 2, 3, 4] (từ 1 đến trước 5: start=1, stop=5)
print("range(2, 11, 2):", list(range(2, 11, 2)))# [2, 4, 6, 8, 10] (bước nhảy step=2)
print("range(40, 0, -10):", list(range(40, 0, -10))) # [40, 30, 20, 10] (đếm lùi khi step âm)

# Các lỗi thường gặp với range():
# - range()     -> TypeError: range expected at least 1 argument, got 0 (bắt buộc phải có stop)
# - range(2.5)  -> TypeError: 'float' object cannot be interpreted as an integer (chỉ nhận số nguyên int)

# Vòng lặp for với range và sequence
# Lặp qua range trực tiếp (không cần bọc list()):
for num in range(3):
    print("num in range(3):", num)

for lang in ['Rust', 'Java', 'Python', 'C++']:
    print("Language:", lang)


# Vòng lặp lồng nhau (Nested for loop)
for category in ['Fruit', 'Vegetable']:
    for item in ['Apple', 'Carrot']:
        print(category, item)

# Vòng lặp while (Chạy cho đến khi điều kiện trở thành False)
count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1

# break (Dừng vòng lặp) & continue (Bỏ qua lần lặp hiện tại)
devs = ['Jess', 'Naomi', 'Tom']

for dev in devs:
    if dev == 'Naomi':
        continue # Bỏ qua Naomi
    print("continue demo:", dev) # In: Jess, Tom

for dev in devs:
    if dev == 'Naomi':
        break    # Dừng ngay khi gặp Naomi
    print("break demo:", dev)    # In: Jess

# for ... else (Khối else chỉ chạy khi vòng lặp kết thúc bình thường, KHÔNG bị 'break')
words = ['sky', 'apple']
for word in words:
    for char in word:
        if char in 'aeiou':
            print(f"'{word}' has vowel '{char}'")
            break
    else:
        print(f"'{word}' has no vowels")
