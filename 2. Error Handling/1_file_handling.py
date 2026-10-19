import os

# 1. Khái niệm File Handling & Các chế độ mở file (Modes)
# Cú pháp: f = open(filename, mode)
#
# Bốn chế độ mở file:
# - "r" (Read - Mặc định): Mở để đọc. Báo lỗi FileNotFoundError nếu file không tồn tại.
# - "w" (Write): Mở để ghi. Tạo file nếu chưa có, xóa sạch nội dung cũ nếu file đã tồn tại.
# - "a" (Append): Mở để ghi nối tiếp. Tạo file nếu chưa có, nối nội dung mới vào cuối file.
# - "x" (Create): Tạo file mới độc quyền. Báo lỗi FileExistsError nếu file đã tồn tại.

demo_file = "demofile.txt"

# Chuẩn bị file mẫu demofile.txt:
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Hello! Welcome to demofile.txt\nThis file is for testing purposes.\nGood Luck!")

# 2. Đọc dòng đầu tiên với open() và f.close() thủ công
f = open(demo_file, "r", encoding="utf-8")
print("Reading first line (f.close):")
print(f.readline().strip())
f.close()

# 3. Sử dụng câu lệnh 'with' & Đọc toàn bộ nội dung với f.read()
# f.read() trả về toàn bộ nội dung file dưới dạng một chuỗi:
print("\nFull file content with f.read():")
with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read())

# 4. Đọc theo số lượng ký tự & Cơ chế con trỏ file (File Pointer)
# Con trỏ tệp tin tự động tịnh tiến sau mỗi lần đọc. Hết file sẽ trả về chuỗi rỗng:
print("Reading characters (file pointer moves forward):")
with open(demo_file, "r", encoding="utf-8") as f:
    print(f.read(10))
    print(f.read(10))
    print(f.read(2))

# 5. Đọc từng dòng với .readline() vs Đọc danh sách dòng với .readlines()
# .readline(): Đọc 1 dòng, con trỏ tự động chuyển sang dòng tiếp theo
with open(demo_file, "r", encoding="utf-8") as f:
    print("\nReading with .readline():")
    print("Line 1:", f.readline().strip())
    print("Line 2:", f.readline().strip())

# .readlines(): Đọc toàn bộ các dòng và trả về một list chuỗi (truy xuất theo chỉ mục)
with open(demo_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("Third line by index (lines[2]):", lines[2].strip())

# 6. Duyệt file từng dòng bằng vòng lặp for (Loop through the file line by line)
# Cách đọc file hiệu quả nhất: đọc dạng stream, không nạp toàn bộ file vào RAM cùng lúc:
print("\nLooping through file line by line:")
with open(demo_file, "r", encoding="utf-8") as f:
    for line in f:
        print("Line:", line.strip())

# 7. Ghi file (Writing): Nối tiếp (Append "a") vs Ghi đè (Write "w")
# 7.1. Chế độ "a" (Append): Giữ nguyên nội dung cũ, nối thêm vào cuối (tự tạo file nếu chưa có).
# Lưu ý: Không thể đọc trực tiếp khi đang mở bằng mode "a", phải mở lại ở chế độ đọc:
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("\nHey! New content!")

with open(demo_file, "r", encoding="utf-8") as f:
    print("\nContent after append:\n", f.read())

# 7.2. Chế độ "w" (Write): Xóa sạch nội dung cũ và ghi đè mới (tự tạo file nếu chưa có).
# Có thể gọi f.write() nhiều lần liên tiếp để ghi tiếp nội dung vào phiên làm việc:
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("This was new! ")
    f.write("Oh my days.")

# Mở lại để đọc nội dung mới ghi đè:
with open(demo_file, "r", encoding="utf-8") as f:
    print("\nContent after overwrite:\n", f.read())

# 8. Chế độ tạo file an toàn "x" (Create)
# "x" tạo file mới. An toàn hơn "w" vì báo lỗi FileExistsError nếu file đã có, tránh ghi đè mất dữ liệu cũ:
new_file = "new.txt"
with open(new_file, "x", encoding="utf-8") as f:
    f.write("Created!")

with open(new_file, "r", encoding="utf-8") as f:
    print("\nRead from new file ('x' mode):", f.read())

# Nếu mở lại bằng "x" khi file đã tồn tại:
try:
    with open(new_file, "x", encoding="utf-8") as f:
        pass
except FileExistsError:
    print(f"Note: '{new_file}' already exists, FileExistsError was raised!")

# 9. Xóa file (Delete a File) với module os
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

# Dọn dẹp file new.txt sau khi thử nghiệm:
if os.path.exists(new_file):
    os.remove(new_file)
    print(f"Cleaned up '{new_file}' successfully.")

# 10. Xóa thư mục (Delete Folder) với os.rmdir()
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

# 11. Quản lý tệp tin và đường dẫn hiện đại với pathlib.Path (Khuyên dùng từ Python 3.4+)
from pathlib import Path

path_file = Path("modern_demo.txt")

# Ghi và đọc nội dung siêu nhanh chỉ với 1 dòng:
path_file.write_text("Hello from modern pathlib!", encoding="utf-8")
print("Pathlib read:", path_file.read_text(encoding="utf-8"))

# Thuộc tính phân tích đường dẫn và xóa file:
print("Pathlib name:  ", path_file.name)
print("Pathlib suffix:", path_file.suffix)
if path_file.exists():
    path_file.unlink()  # Xóa file an toàn
    print("Pathlib file cleaned up.")
