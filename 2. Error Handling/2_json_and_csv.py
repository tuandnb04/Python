import csv
import json
import os

# BÀI HỌC: XỬ LÝ TỆP DỮ LIỆU CÓ CẤU TRÚC (JSON & CSV)
#
# BẢN CHẤT & GIA PHẢ:
# - Trong thực tế, dữ liệu hiếm khi được lưu dưới dạng văn bản thô vô cấu trúc (.txt).
# - Hai định dạng tệp tin kinh điển nhất trong kỹ thuật phần mềm:
#   1. JSON (JavaScript Object Notation): Dạng cây lồng nhau (Key-Value, Lists),
#      là định dạng chuẩn mực số 1 khi giao tiếp qua REST API và lưu trữ cấu hình.
#   2. CSV (Comma-Separated Values): Dạng bảng 2 chiều (Hàng và Cột phân tách bằng dấu phẩy),
#      là định dạng chuẩn mực trong xuất nhập báo cáo Excel và xử lý dữ liệu bảng.


# 1. Thao tác với định dạng JSON (json.loads, json.dumps, json.load, json.dump)
# Phân biệt chữ cái cuối:
# - 's' (String): loads() & dumps() thao tác trên chuỗi văn bản trong bộ nhớ.
# - Không có 's' (File): load() & dump() thao tác trực tiếp với File I/O qua file stream.

print("--- 1. Working with JSON Data ---")

data_payload = {
    "organization": "OpenTech",
    "active": True,
    "members_count": 3,
    "skills": ["Python", "FastAPI", "Docker"],
    "settings": {
        "theme": "dark",
        "notifications": False
    }
}

# dumps(): Chuyển đổi Python Dict -> JSON String
json_string = json.dumps(data_payload, indent=2)
print("Serialized JSON String:\n", json_string)

# loads(): Phân tích chuỗi JSON String -> Python Dict
parsed_dict = json.loads(json_string)
print("\nParsed from JSON string:", parsed_dict["organization"], "| Active:", parsed_dict["active"])

# Ghi và đọc file JSON trực tiếp xuống ổ cứng:
json_filename = "demo_config.json"

# dump(): Ghi dữ liệu ra file
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(data_payload, f, indent=2, ensure_ascii=False)
print(f"Successfully saved to {json_filename}")

# load(): Đọc dữ liệu từ file
with open(json_filename, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("Loaded skills from file:", loaded_data["skills"])


# 2. Thao tác với định dạng CSV (csv.reader, csv.writer)
print("\n--- 2. Working with Standard CSV ---")

csv_filename = "demo_users.csv"
rows_data = [
    ["User ID", "Full Name", "Department"],
    [101, "Alice Johnson", "Engineering"],
    [102, "Bob Smith", "Marketing"],
    [103, "Charlie Brown", "Finance"]
]

# Ghi file CSV dạng hàng (csv.writer):
# Bắt buộc đặt newline="" khi mở file CSV trong Python để tránh bị thừa dòng trắng trống trên Windows.
with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows_data)

# Đọc file CSV dạng hàng (csv.reader):
with open(csv_filename, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("CSV Header:", header)
    for row in reader:
        print(f" -> ID: {row[0]}, Name: {row[1]}, Dept: {row[2]}")


# 3. CSV chuyên nghiệp với DictReader và DictWriter
# DictReader và DictWriter giúp truy cập cột bằng TÊN CỘT thay vì số chỉ mục index.
# Nhờ vậy, nếu thứ tự cột trong file CSV bị xáo trộn, code vẫn chạy an toàn không lỗi!

print("\n--- 3. Modern CSV with DictReader and DictWriter ---")

dict_csv_file = "demo_dict_users.csv"
fieldnames = ["id", "username", "role", "score"]
users_list = [
    {"id": 1, "username": "alice", "role": "Admin", "score": 98.5},
    {"id": 2, "username": "bob", "role": "Editor", "score": 85.0},
    {"id": 3, "username": "charlie", "role": "Viewer", "score": 72.5},
]

# Ghi CSV bằng DictWriter:
with open(dict_csv_file, "w", newline="", encoding="utf-8") as f:
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()  # Ghi dòng tiêu đề
    dict_writer.writerows(users_list)

# Đọc CSV bằng DictReader:
with open(dict_csv_file, "r", encoding="utf-8") as f:
    dict_reader = csv.DictReader(f)
    for user_row in dict_reader:
        print(f"User: {user_row['username']:<10} | Role: {user_row['role']:<8} | Score: {user_row['score']}")


# Dọn dẹp các tệp tạm tạo ra trong lúc thực thi
for temp_file in [json_filename, csv_filename, dict_csv_file]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
print("\nTemporary demonstration files cleaned up.")
