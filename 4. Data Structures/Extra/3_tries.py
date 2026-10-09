# Custom Trie (Prefix Tree - Cây tiền tố tự cài đặt bằng TrieNode)
# - Cấu trúc cây dùng để lưu trữ tập hợp các chuỗi ký tự (strings).
# - Đặc điểm hoạt động:
#   + Gốc (Root) không chứa ký tự nào (đại diện cho chuỗi rỗng "").
#   + Mỗi node đại diện cho 1 ký tự; đường đi từ gốc tới một node biểu diễn một tiền tố (prefix).
#   + Các từ có cùng tiền tố sẽ dùng chung các node (nhánh) đó (ví dụ "tea" và "ten" dùng chung nhánh "te").
#   + Node kết thúc của một từ hoàn chỉnh được đánh dấu bằng `is_end_of_word = True`.
# - Ưu điểm:
#   + Thao tác tìm kiếm và chèn cực nhanh: O(L) với L là độ dài chuỗi (không phụ thuộc số lượng từ).
#   + Tối ưu cho tính năng Autocomplete (gợi ý từ) và Spell Check (kiểm tra chính tả).
# - Nhược điểm:
#   + Tốn bộ nhớ nếu tập chuỗi có nhiều ký tự phân tán, ít dùng chung tiền tố (vì phải tạo nhiều node riêng biệt).


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Chèn từ vào Trie: O(L)
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    # Tìm kiếm từ hoàn chỉnh: O(L)
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    # Kiểm tra tiền tố (Prefix) - Cơ chế cho Autocomplete: O(L)
    def starts_with(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

trie = Trie()
for word in ["top", "tea", "ten"]:
    trie.insert(word)

print("Search 'tea':", trie.search("tea"))                  # True
print("Search 'te':", trie.search("te"))                    # False (vì 'te' chưa kết thúc từ)
print("Prefix 'te' (Autocomplete):", trie.starts_with("te"))# True
