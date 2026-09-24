# Kỹ thuật lặp qua Dictionary trong Python
# Dùng để duyệt qua các cặp key-value nhằm xử lý logic hoặc cập nhật dữ liệu

products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

# Lặp qua Values (.values())
for price in products.values():
    print(price)

# Lặp qua Keys (.keys() hoặc lặp trực tiếp)
for product in products.keys():
    print(product)

# Hoặc:
# for product in products:
#     print(product)

# Lặp qua cả Keys và Values (.items())
# Mỗi phần tử trả về là 1 tuple (key, value)
for product in products.items():
    print(product)

# Tách riêng thành 2 biến (Unpacking key, value)
for product, price in products.items():
    print(product, price)

# Ví dụ thực tế: Giảm giá 20% cho tất cả sản phẩm
for product, price in products.items():
    products[product] = round(price * 0.8)

print(products)

# Sử dụng hàm enumerate() để thêm bộ đếm (index/counter)
# Mặc định bộ đếm bắt đầu từ 0

# Với keys:
for index, product in enumerate(products):
    print(index, product)

# Với values:
for index, price in enumerate(products.values()):
    print(index, price)

# Với items():
for index, product in enumerate(products.items()):
    print(index, product)

# Tùy chỉnh số bắt đầu bằng đối số thứ 2 (start = 1):
for index, product in enumerate(products.items(), 1):
    print(index, product)
