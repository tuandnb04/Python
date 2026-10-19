# 1. Vòng lặp for duyệt qua danh sách (List) và chuỗi (String)
# Toàn bộ khối mã bên trong vòng lặp được thực thi lần lượt cho từng phần tử:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    upper_name = fruit.upper()
    print("Fruit:", upper_name)

for char in "Hello":
    print("Char:", char)

# 2. Vòng lặp for với range() (Tạo dãy số)
# range(stop): Mặc định bắt đầu từ 0, tăng 1 và dừng trước stop
print("\nrange(5):")
for i in range(5):
    print(" - Step:", i)

# range(start, stop): Chỉ định giá trị bắt đầu
print("\nrange(3, 7):")
for i in range(3, 7):
    print(" - Num:", i)

# range(start, stop, step): Chỉ định bước nhảy với đối số thứ ba
print("\nrange(3, 10, 2):")
for i in range(3, 10, 2):
    print(" - Step 2:", i)

# 3. Vòng lặp while (Lặp chừng nào điều kiện còn đúng)
# Chừng nào count < 5 thì tiếp tục in và tăng biến đếm (tránh lặp vô tận):
count = 1
print("\nWhile loop:")
while count < 5:
    print("Count:", count)
    count += 1

# 4. Lệnh dừng break (Thoát khỏi vòng lặp for hoặc while ngay lập tức)
print("\nBreak in for loop:")
for x in range(10):
    if x == 3:
        break
    print("x:", x)

# Dừng vòng lặp vô tận while True sau 5 lần lặp:
print("\nBreak in while loop:")
i = 0
while True:
    i += 1
    print("i:", i)
    if i == 5:
        break

# 5. Lệnh continue (Bỏ qua lượt lặp hiện tại, nhảy sang lượt tiếp theo)
print("\nContinue demo (skip 2):")
for x in range(5):
    if x == 2:
        continue
    print("x:", x)

# 6. Vòng lặp lồng nhau (Nested Loop - Vòng lặp nằm trong vòng lặp khác)
print("\nNested loop:")
for x in fruits:
    for j in range(4):
        print(x, j)
