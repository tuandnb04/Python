# Trie (Prefix Tree - Cây tiền tố):
# - Cấu trúc cây dùng để lưu trữ tập hợp các chuỗi ký tự
# - Tối ưu cho tính năng Autocomplete (tự động gợi ý từ) và Spell Check (kiểm tra chính tả)
# - Độ phức tạp tìm kiếm/chèn: O(L) với L là độ dài của từ

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
