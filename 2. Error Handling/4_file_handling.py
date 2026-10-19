import os

# 1. Khái niệm File Handling & Hàm open()
# Python cung cấp hàm tích hợp open() để làm việc với tệp tin (File I/O).
# Cú pháp:
#   f = open(filename, mode)
#
# Các chế độ mở file (Modes):
# - "r" (Read - Mặc định): Mở để đọc. Báo lỗi FileNotFoundError nếu file không tồn tại.
# - "a" (Append): Mở để ghi nối tiếp vào cuối file. Tự tạo file mới nếu chưa tồn tại.
# - "w" (Write): Mở để ghi đè (xóa toàn bộ nội dung cũ). Tự tạo file mới nếu chưa tồn tại.
# - "x" (Create): Tạo file mới độc quyền. Báo lỗi FileExistsError nếu file đã tồn tại.
#
# Định dạng nội dung:
# - "t" (Text - Mặc định): Dữ liệu dạng văn bản chuỗi (str). Mặc định là "rt".
# - "b" (Binary): Dữ liệu dạng nhị phân byte (bytes) dành cho hình ảnh, âm thanh...
#
# Cú pháp ngắn gọn:
#   open("demofile.txt") tương đương open("demofile.txt", "rt")

demo_file = "demofile.txt"

# Chuẩn bị file mẫu demofile.txt:
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")

# 2. Mở file ở cùng thư mục vs Đường dẫn khác (Relative vs Absolute Path)
# - Cùng thư mục: Chỉ cần truyền tên file: open("demofile.txt")
# - Thư mục khác: Truyền đường dẫn đầy đủ (dùng raw string r"..." hoặc thoát dấu gạch chéo \\):
#   Ví dụ: f = open(r"D:\myfiles\welcome.txt") hoặc f = open("D:\\myfiles\\welcome.txt")

# 3. Đọc toàn bộ nội dung với .read()
# Mở file và đọc toàn bộ nội dung bằng phương thức .read():
f = open(demo_file, "r", encoding="utf-8")
print("Reading with open() and f.read():")
print(f.read())
f.close()

# 4. Sử dụng câu lệnh 'with' (With Statement - Chuẩn Pythonic)
# Khi dùng 'with', Python tự động giải phóng và đóng file khi kết thúc khối lệnh,
# bạn không cần phải lo lắng về việc quên đóng file:
print("\nReading with 'with open(...)' statement:")
with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read())

# 5. Đóng file (f.close()) & Cơ chế bộ đệm (Buffering)
# - Khi không dùng 'with', BẮT BUỘC phải gọi f.close() sau khi xử lý xong.
# - Lưu ý về Buffering: Do hệ điều hành sử dụng bộ đệm (buffer) để tối ưu hiệu năng ghi,
#   các thay đổi có thể chưa được lưu thật sự xuống ổ đĩa cho đến khi bạn gọi f.close() hoặc f.flush().
f = open(demo_file, "r", encoding="utf-8")
print("\nRead first line before manual close:")
print(f.readline().strip())
f.close()

# 6. Đọc một phần của file (Read Only Parts of the File)
# Mặc định .read() trả về toàn bộ nội dung, nhưng có thể truyền số lượng ký tự cần đọc:
# Đọc 5 ký tự đầu tiên của file:
with open(demo_file, "r", encoding="utf-8") as f:
    print("\nFirst 5 characters of the file:")
    print(f.read(5))  # 'Hello'

# 7. Đọc từng dòng với .readline() (Read Lines)
# Mỗi lần gọi .readline() sẽ đọc dòng tiếp theo:
with open(demo_file, "r", encoding="utf-8") as f:
    print("\nReading first two lines with readline():")
    print("Line 1:", f.readline().strip())
    print("Line 2:", f.readline().strip())

# 8. Duyệt file từng dòng bằng vòng lặp for (Loop through the file line by line)
# Cách đọc file hiệu quả nhất: đọc dạng stream, không nạp toàn bộ file vào RAM cùng lúc:
print("\nLooping through file line by line:")
with open(demo_file, "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())

# 9. Ghi file (Writing): Nối tiếp (Append "a") vs Ghi đè (Write "w")
# 9.1. Chế độ "a" (Append): Nối thêm vào cuối file
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("\nNow the file has more content!")

with open(demo_file, "r", encoding="utf-8") as f:
    print("\nContent after append:\n", f.read())

# 9.2. Chế độ "w" (Write): Ghi đè toàn bộ nội dung cũ
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Woops! I have deleted the content!")

with open(demo_file, "r", encoding="utf-8") as f:
    print("\nContent after overwrite:\n", f.read())

# 10. Tạo file mới (Create a New File)
# Để tạo file mới trong Python, sử dụng phương thức open() với các tham số:
# - "x" (Create): Tạo file mới, trả về ngoại lệ FileExistsError nếu file đã tồn tại.
# - "a" (Append): Tạo file mới nếu file chưa tồn tại (nếu đã có thì ghi nối tiếp vào cuối).
# - "w" (Write): Tạo file mới nếu file chưa tồn tại (nếu đã có thì ghi đè nội dung).

# Ví dụ tạo file rỗng mới có tên "myfile.txt":
my_new_file = "myfile.txt"
f = open(my_new_file, "x", encoding="utf-8")
f.close()
print("\nCreated a new empty file 'myfile.txt' with 'x' mode.")

# Lưu ý: Nếu gọi lại mode "x" trên file đã tồn tại, Python sẽ ném lỗi FileExistsError:
try:
    f_duplicate = open(my_new_file, "x", encoding="utf-8")
    f_duplicate.close()
except FileExistsError:
    print(f"Note: '{my_new_file}' already exists, FileExistsError was raised!")

# 11. Xóa file (Delete a File) với module os
# Để xóa một tệp tin, cần import module os và gọi hàm os.remove():
# Kiểm tra file có tồn tại hay không bằng os.path.exists() trước khi xóa để tránh FileNotFoundError:
print("\nDeleting files with os.remove() & os.path.exists():")
if os.path.exists(demo_file):
    os.remove(demo_file)
    print(f"File '{demo_file}' deleted successfully.")
else:
    print(f"The file '{demo_file}' does not exist.")

# Thử xóa file không tồn tại để kiểm tra nhánh else:
if os.path.exists("non_existent_file.txt"):
    os.remove("non_existent_file.txt")
else:
    print("The file does not exist (handled safely).")

# Dọn dẹp nốt file myfile.txt nếu còn:
if os.path.exists(my_new_file):
    os.remove(my_new_file)
    print(f"Cleaned up '{my_new_file}' successfully.")

# 12. Xóa thư mục (Delete Folder) với os.rmdir()
# Để xóa một thư mục rỗng, ta sử dụng phương thức os.rmdir():
# Lưu ý quan trọng: os.rmdir() CHỈ xóa được thư mục RỖNG (sẽ báo OSError nếu thư mục có chứa tệp tin):
my_folder = "myfolder"
if not os.path.exists(my_folder):
    os.mkdir(my_folder)
    print(f"\nCreated empty folder '{my_folder}' for testing.")

if os.path.exists(my_folder):
    os.rmdir(my_folder)
    print(f"Removed folder '{my_folder}' successfully with os.rmdir().")
else:
    print(f"Folder '{my_folder}' does not exist.")
