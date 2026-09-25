# 1. getattr(): Đọc thuộc tính động khi tên thuộc tính chưa biết trước (Class Person)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

person = Person('John Doe', 30)

print(getattr(person, 'name'))            # John Doe
print(getattr(person, 'age'))             # 30
print(getattr(person, 'city', 'Milano'))  # Milano (giá trị mặc định khi không tìm thấy)


# 2. dir() & callable(): Duyệt qua các thuộc tính dữ liệu của đối tượng
for attr in dir(person):
    # Bỏ qua dunder methods (__init__, __str__) và các phương thức thông thường
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')


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

print(config_obj.server_url)   # type: ignore # https://api.example.com
print(config_obj.timeout_sec)  # type: ignore # 30

# Cách hiện đại: Dùng vars().update() nạp toàn bộ dict vào object trong 1 dòng
config_fast = Configuration()
vars(config_fast).update(settings_data)
print("vars().update():", config_fast.server_url) # type: ignore


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
attributes_to_clean = ['auth_token', 'temp_counter', 'non_existing_field']

# Cách 1 - Chuẩn EAFP: Xóa bằng delattr và bỏ qua nếu không tồn tại (tránh check hasattr thừa)
for attr in attributes_to_clean:
    try:
        delattr(session, attr)
        print(f'Removed attribute: {attr}')
    except AttributeError:
        pass

# Cách 2 - Chuẩn Pythonic dùng vars() / __dict__.pop() an toàn trong 1 dòng:
# vars(session).pop('temp_counter', None)

print('\nFinal attributes remaining (via vars):', vars(session))




