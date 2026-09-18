# Interface theo chuẩn Structural Subtyping với typing.Protocol (PEP 544)
from typing import Protocol

# => TẠI SAO PROTOCOL TỐT HƠN ABC (ABSTRACT BASE CLASS) TRONG NHIỀU TRƯỜNG HỢP?
# 1. Duck Typing an toàn: Các class không cần kế thừa trực tiếp từ Protocol (No explicit inheritance).
#    Chỉ cần có đầy đủ các phương thức tương ứng là tự động tương thích kiểu (Structural Subtyping).
# 2. Giảm tính phụ thuộc chặt chẽ (Decoupling): Dễ dàng viết Mock / Plugin mà không cần sửa class gốc.

class GraphStorage(Protocol):
    def save_node(self, node_id: str, properties: dict) -> bool:
        ...

    def query(self, cypher_query: str) -> list[dict]:
        ...

# 1. Triển khai KuzuDB Storage (Không cần kế thừa GraphStorage)
class KuzuStorage:
    def save_node(self, node_id: str, properties: dict) -> bool:
        print(f"[KuzuDB] Saved node: {node_id}")
        return True

    def query(self, cypher_query: str) -> list[dict]:
        print(f"[KuzuDB] Executing Cypher: {cypher_query}")
        return [{"status": "success"}]

# 2. Triển khai FalkorDB Storage
class FalkorStorage:
    def save_node(self, node_id: str, properties: dict) -> bool:
        print(f"[FalkorDB] Saved node: {node_id}")
        return True

    def query(self, cypher_query: str) -> list[dict]:
        print(f"[FalkorDB] Executing Cypher: {cypher_query}")
        return [{"status": "success"}]

# Hàm chấp nhận bất kỳ Storage nào thỏa mãn Protocol
def run_indexing_pipeline(storage: GraphStorage):
    storage.save_node("Flask.app", {"file": "src/flask/app.py"})
    storage.query("MATCH (n:Module) RETURN n")

run_indexing_pipeline(KuzuStorage())
run_indexing_pipeline(FalkorStorage())
