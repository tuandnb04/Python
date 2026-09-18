import inspect

# Thuộc tính cố định thông thường (Class Car)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car('Lamborghini', 'Gallardo')
print(my_car.brand)  # Lamborghini
print(my_car.model)  # Gallardo


# getattr(): Đọc thuộc tính động khi tên thuộc tính chưa biết trước (Class Person)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)

print(getattr(person, 'name'))            # John Doe
print(getattr(person, 'age'))             # 30
print(getattr(person, 'city', 'Milano'))  # Milano (giá trị mặc định khi không tìm thấy)


# dir() & callable(): Duyệt qua tất cả các thuộc tính dữ liệu của đối tượng
for attr in dir(person):
    # Bỏ qua dunder methods (__init__, __str__) và các hàm/method thông thường
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Cách hiện đại: Dùng inspect.getmembers() để lọc nhanh biến dữ liệu chuẩn xác hơn
data_members = [k for k, v in inspect.getmembers(person) if not k.startswith('__') and not inspect.isroutine(v)]
print("inspect.getmembers():", data_members)  # ['age', 'name']


# setattr(): Gán hoặc tạo mới thuộc tính động (Class Configuration)
class Configuration:
    pass

settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Nạp động các thuộc tính từ dictionary
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)   # https://api.example.com
print(config_obj.timeout_sec)  # 30

# Cách hiện đại: Dùng vars().update() nạp toàn bộ dict vào object trong 1 dòng
config_fast = Configuration()
vars(config_fast).update(settings_data)
print("vars().update():", config_fast.server_url)


# hasattr(): Kiểm tra sự tồn tại của thuộc tính trước khi truy cập (Class Product)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)
required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')


# delattr(): Xóa thuộc tính động (Class UserSession)
class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token   # Dữ liệu nhạy cảm
        self.temp_counter = 0     # Dữ liệu tạm thời

session = UserSession(101, 'a1b2c3d4e5')
attributes_to_clean = ['auth_token', 'temp_counter']

# Xóa các thuộc tính chỉ định
for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')
for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')


# Cách hiện đại: Khóa thuộc tính động bằng __slots__ (Python 3.10+)
# Ngăn chặn người dùng tự ý gán thêm thuộc tính lạ ngoài danh sách và tiết kiệm 30% RAM
class StrictProduct:
    __slots__ = {'name': str, 'price': float}

    def __init__(self, name, price):
        self.name = name
        self.price = price

strict_prod = StrictProduct('T-Shirt', 25.0)
try:
    strict_prod.discount = 10  # Lỗi vì 'discount' không nằm trong __slots__
except AttributeError as e:
    print("Error outside __slots__:", e)
