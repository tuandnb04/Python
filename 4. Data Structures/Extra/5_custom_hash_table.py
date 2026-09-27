# Custom Hash Table (Bảng băm tự cài đặt với Separate Chaining)
# - Cơ chế: Dùng hàm băm ánh xạ key thành hashed_key
# - Xử lý xung đột: Lưu các key trùng hash vào một dictionary con (Separate Chaining)
# - Độ phức tạp: Thao tác add, remove, lookup đạt O(1) trung bình

class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed_key = self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        self.collection[hashed_key][key] = value

    def remove(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection and key in self.collection[hashed_key]:
            del self.collection[hashed_key][key]
            if not self.collection[hashed_key]:
                del self.collection[hashed_key]

    def lookup(self, key):
        hashed_key = self.hash(key)
        if hashed_key in self.collection:
            return self.collection[hashed_key].get(key, None)
        return None


ht = HashTable()
ht.add("name", "Alice")
ht.add("age", 25)
print("Lookup 'name':", ht.lookup("name"))  # Alice
print("Lookup 'age':", ht.lookup("age"))    # 25

ht.remove("age")
print("Lookup 'age' after remove:", ht.lookup("age"))  # None
