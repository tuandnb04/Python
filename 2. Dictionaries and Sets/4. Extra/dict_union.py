# Toán tử gộp Dictionary '|' và '|=' (Python 3.9+ PEP 584)

default_config = {"branch": "main", "depth": 1, "backend": "kuzu"}
custom_config = {"backend": "falkordb", "depth": 5}

# 1. Gộp 2 dict tạo dict mới với toán tử '|'
# => TẠI SAO DÙNG TOÁN TỬ '|' LÀ TỐT NHẤT?
#    + Cú pháp tự nhiên, trực quan và đồng bộ với toán tử Union của Set.
#    + Không làm thay đổi dict gốc và bảo toàn kiểu dict con (subclasses).
merged_config = default_config | custom_config
print("Merged config (|):", merged_config)

# 2. Cập nhật trực tiếp (in-place) với toán tử '|='
# => TẠI SAO DÙNG '|=' LÀ TỐT NHẤT?
#    + Ngắn gọn, nhất quán với các toán tử gán tăng cường như +=, -=.
base_config = {"host": "localhost", "port": 8000}
base_config |= {"port": 9000, "debug": True}
print("Updated config (|=):", base_config)
