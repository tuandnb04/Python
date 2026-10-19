# 1. Khai báo chuỗi & Đo độ dài
# Chuỗi đặt trong nháy kép "..." hoặc nháy đơn '...' (kể cả chuỗi rỗng "" vẫn là chuỗi):
text = "Python"
print("Length of text:", len(text))  # 6 ký tự

# 2. Lấy ký tự theo vị trí (Indexing - vị trí bắt đầu từ 0)
# Python xem chuỗi như một dãy các ký tự, truy cập từng ký tự bằng chỉ mục:
print("First character [0]:", text[0])  # 'P'

# 3. Cắt chuỗi [start : end] (Slicing)
# Lấy các ký tự từ vị trí start đến trước end (không bao gồm ký tự tại vị trí end):
print("Slice [0:3]:", text[0:3])        # 'Pyt' (lấy từ 0 đến trước 3)

# 4. Nối chuỗi (+) và Định dạng f-string (F-Strings)
# Dùng dấu + để nối chuỗi (phải tự thêm dấu cách " " ở giữa nếu muốn có khoảng trắng):
full_greeting = "Hello" + " " + "World"
print("Concatenation (+):", full_greeting)

# Cách hiện đại: Dùng f-string (bắt đầu bằng chữ f trước dấu nháy)
# Cặp ngoặc {} là placeholder có thể chứa biến, biểu thức tính toán và định dạng số (:.2f):
name = "Tobias"
price = 14.0
print(f"Hello, {name}!")                 # Chèn biến
print(f"Total: {price * 2:.2f}")         # Tính toán & định dạng 2 chữ số thập phân

# 5. Các phương thức xử lý chuỗi phổ biến (String Methods)
# Lưu ý: Chuỗi là bất biến (Immutable), mọi phương thức đều trả về chuỗi mới chứ không làm đổi chuỗi gốc:
raw_text = "  Python is Easy  "

print("Uppercase:", raw_text.upper())                     # Viết hoa
print("Lowercase:", raw_text.lower())                     # Viết thường
print("Strip whitespace:", raw_text.strip())              # Xóa khoảng trắng 2 đầu
print("Find 'is':", raw_text.find("is"))                  # Tìm vị trí xuất hiện (trả về -1 nếu không thấy)
print("Count 's':", raw_text.count("s"))                  # Đếm số lần xuất hiện
print("Replace word:", raw_text.replace("Easy", "Fun"))   # Thay thế chữ (mặc định thay toàn bộ, có thể thêm count để giới hạn)
print("Split into list:", raw_text.split())               # Tách thành danh sách từ
print("Contains 'Python':", "Python" in raw_text)         # Kiểm tra tồn tại (True/False)
print("Original unchanged:", raw_text)                    # Chuỗi gốc không hề bị thay đổi
