# Special / Dunder Methods (__name__): Phương thức đặc biệt tự động gọi khi dùng toán tử hoặc hàm built-in

# Ví dụ Class Book: __len__, __str__, __repr__, __eq__
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # len(book): Lấy số trang sách (thiếu hàm này gọi len(book) sẽ bị lỗi TypeError)
    def __len__(self):
        return self.pages

    # str(book) hoặc print(book): Hiển thị chuỗi cho người dùng (mặc định sẽ in địa chỉ ô nhớ)
    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    # repr(book): Chuỗi đại diện kỹ thuật dùng để tái tạo lại đối tượng (cho dev / debug)
    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    # book1 == book2: So sánh nội dung thay vì so sánh địa chỉ ô nhớ
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages == other.pages

    # book1 < book2: Phép so sánh nhỏ hơn, giúp danh sách Book tự sắp xếp được bằng sorted() / .sort()
    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    # book1 + book2: Nạp chồng toán tử cộng (+) - Operator Overloading
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        raise TypeError("Can only add another Book instance")


book1 = Book("Built Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)
book3 = Book("Python Clean Code", 350)

print(len(book1))        # 420 (gọi ngầm book1.__len__())
print(len(book2))        # 420
print(str(book1))        # 'Built Wealth Like a Boss' has 420 pages (gọi ngầm book1.__str__())
print(str(book2))        # 'Be Your Own Start' has 420 pages
print(repr(book1))       # Book('Built Wealth Like a Boss', 420) (gọi ngầm book1.__repr__())
print(eval(repr(book1)) == book1) # True (tái tạo lại chính đối tượng từ chuỗi repr)
print(book1 == book2)    # True (gọi ngầm book1.__eq__(book2))

# So sánh và sắp xếp (__lt__):
print("book3 < book1:", book3 < book1)  # True (350 < 420)
books = [book1, book3]
books.sort()
print("Sorted books by pages:", [b.title for b in books])  # ['Python Clean Code', 'Built Wealth Like a Boss']

# Toán tử cộng (__add__):
print("Total pages of book1 and book3:", book1 + book3)  # 770


# Ví dụ Class Cart: Giỏ hàng với Container Dunder Methods
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print(f'{item} is not in cart')

    def list_items(self):
        return self.items

    # len(cart): Đếm số lượng phần tử trong giỏ
    def __len__(self):
        return len(self.items)

    # cart[index]: Cho phép truy cập chỉ mục dạng cart[0], cart[3]
    def __getitem__(self, index):
        return self.items[index]

    # 'item' in cart: Kiểm tra tồn tại bằng toán tử 'in'
    def __contains__(self, item):
        return item in self.items

    # for item in cart: Biến đối tượng thành Iterable để duyệt for
    def __iter__(self):
        return iter(self.items)


cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

# Duyệt từng phần tử trong giỏ (gọi ngầm cart.__iter__())
for item in cart:
    print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor
print()

print(len(cart))          # 4 (gọi ngầm cart.__len__())
print(cart[3])            # Monitor (gọi ngầm cart.__getitem__(3))

print('Monitor' in cart)  # True (gọi ngầm cart.__contains__('Monitor'))
print('banana' in cart)   # False

cart.remove('Ergo keyboard')
print(cart.list_items())  # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana')     # banana is not in cart



