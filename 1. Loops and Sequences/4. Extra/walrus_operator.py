# Toán tử gán Walrus (:=) trong Python (Python 3.8+ PEP 572)
# => TẠI SAO TOÁN TỬ WALRUS (:=) LÀ CẢI TIẾN QUAN TRỌNG?
#    + Cho phép vừa gán giá trị vừa kiểm tra điều kiện ngay trong biểu thức.
#    + Tránh việc phải gọi hàm hoặc tính toán 2 lần (ví dụ: tính len(w) trong List Comprehension).

# Dùng trong vòng lặp while để vừa gán vừa kiểm tra điều kiện
sample_data = ["repo1", "repo2", "repo3", ""]
index = 0

while (item := sample_data[index]):
    print("Processing item:", item)
    index += 1

# Dùng trong List Comprehension để tránh tính toán 2 lần
words = ["python", "ast", "codegraph", "ai"]
# Chỉ lấy các từ có độ dài > 3 và lưu luôn giá trị độ dài
word_lengths = [(w, length) for w in words if (length := len(w)) > 3]
print("Filtered word lengths:", word_lengths)

