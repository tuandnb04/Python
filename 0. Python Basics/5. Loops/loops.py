# Khái niệm Vòng lặp (Loops & Iteration):
# Vòng lặp là cấu trúc điều khiển cho phép thực thi lặp đi lặp lại một khối lệnh
# khi một điều kiện còn đúng (while) hoặc lặp qua từng phần tử của một dãy (for).

# 1. Vòng lặp while (While loop)
# Cú pháp:
#   while <điều_kiện>:
#       <khối_lệnh>
# Vòng lặp sẽ tiếp tục chạy chừng nào <điều_kiện> còn là True (hoặc truthy).
# BẮT BUỘC phải có bước cập nhật biến đếm/trạng thái để tránh vòng lặp vô tận!
count = 1
while count <= 5:
    print(f"while count: {count}")
    count += 1  # Tăng biến đếm, nếu thiếu dòng này vòng lặp sẽ chạy mãi mãi

print("Finished basic while loop.\n")

# 2. Toán tử Walrus (:=) trong vòng lặp while
# Vừa gán giá trị mới cho biến vừa kiểm tra điều kiện ngay tại đầu vòng lặp:
countdown = 4
while (countdown := countdown - 1) > 0:
    print(f"Countdown with walrus: {countdown}")
print("Countdown finished.\n")

# 3. Hàm range() - Tạo dãy số nguyên bất biến (Immutable integer sequence)
# Cú pháp: range(stop) hoặc range(start, stop[, step])
# - range chỉ nhận số nguyên (int), không nhận float.
# - range sinh số dạng "lười" (lazy evaluation): chỉ sinh số khi được duyệt tới,
#   giúp tiết kiệm bộ nhớ RAM tuyệt đối kể cả khi biểu diễn hàng triệu số.

# 3.1. Chỉ truyền 'stop' (mặc định bắt đầu từ 0, bước nhảy là 1):
print("range(4):")
for num in range(4):
    print(num, end=" ")
print()  # Xuống dòng

# 3.2. Truyền cả 'start' và 'stop' (từ start đến trước stop):
print("range(5, 9):")
for num in range(5, 9):
    print(num, end=" ")
print()

# 3.3. Truyền thêm 'step' (bước nhảy dương):
print("range(0, 10, 2):")
for num in range(0, 10, 2):
    print(num, end=" ")
print()

# 3.4. Đếm lùi với bước nhảy âm (negative step):
print("range(5, 0, -1):")
for num in range(5, 0, -1):
    print(num, end=" ")
print("\n")

# 4. Vòng lặp for duyệt qua chuỗi ký tự (String)
# Chuỗi văn bản (str) là một chuỗi tuần tự các ký tự, có thể duyệt trực tiếp:
word = "Python"
print(f"Looping through string '{word}':")
for char in word:
    print(f"Character: {char}")
print()

# 5. Điều khiển vòng lặp: break, continue, pass
# - 'break'   : Lập tức dừng và thoát hoàn toàn khỏi vòng lặp hiện tại.
# - 'continue': Bỏ qua phần còn lại của lần lặp hiện tại, nhảy sang lần lặp kế tiếp.
# - 'pass'    : Lệnh giữ chỗ rỗng (placeholder), không làm gì cả.

# Ví dụ về 'continue' (bỏ qua số lẻ, chỉ in số chẵn):
print("continue demo (even numbers only):")
for n in range(1, 8):
    if n % 2 != 0:
        continue  # Bỏ qua số lẻ
    print(f"Even: {n}")
print()

# Ví dụ về 'break' (dừng vòng lặp khi gặp số 4):
print("break demo (stop at 4):")
for n in range(1, 10):
    if n == 4:
        print("Met 4, stopping loop via break!")
        break
    print(f"n: {n}")
print()

# 6. Vòng lặp lồng nhau (Nested loops)
# Một vòng lặp nằm bên trong một vòng lặp khác:
print("Multiplication grid (2x1 to 3x3):")
for row in range(2, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}", end="  |  ")
    print()  # Hết một hàng
print()

# 7. Cấu trúc for ... else & while ... else
# Khối 'else' gắn với vòng lặp sẽ:
# - ĐƯỢC CHẠY: khi vòng lặp hoàn thành bình thường (chạy hết các phần tử).
# - KHÔNG CHẠY: nếu vòng lặp bị ngắt cưỡng bức bởi lệnh 'break'.

# 7.1. Ví dụ với for ... else (tìm kiếm ký tự trong từ):
search_word = "sky"
print(f"Checking vowels in '{search_word}':")
for ch in search_word:
    if ch in "aeiouAEIOU":
        print(f"Found vowel: {ch}")
        break
else:
    print(f"'{search_word}' has no vowels (loop completed normally).")

search_word_2 = "apple"
print(f"Checking vowels in '{search_word_2}':")
for ch in search_word_2:
    if ch in "aeiouAEIOU":
        print(f"Found vowel '{ch}' (stopped by break).")
        break
else:
    print(f"'{search_word_2}' has no vowels.")
print()

# 7.2. Ví dụ với while ... else:
attempts = 3
while attempts > 0:
    attempts -= 1
else:
    print("while ... else: All attempts exhausted (loop completed normally).")
