# Decorator @override trong Kế thừa OOP (Python 3.12+ PEP 698)
from typing import override

# => TẠI SAO @OVERRIDE TỐT HƠN CÁCH VIẾT CŨ KHÔNG CÓ DECORATOR?
#    + Trước Python 3.12: Nếu bạn gõ sai tên phương thức ở class con (ví dụ: `analize_repository` thay vì `analyze_repository`),
#      Python sẽ xem đây là phương thức mới hoàn toàn mà KHÔNG BÁO LỖI, dẫn đến bug ngầm khi chạy chương trình.
#    + Từ Python 3.12: Với `@override`, các công cụ Type Checker (Mypy, Pyright, IDE) sẽ phát hiện và cảnh báo lỗi
#      ngay lập tức nếu phương thức đó không tồn tại ở class cha.

class BaseAnalyzer:
    def analyze_repository(self, repo_url: str) -> str:
        return f"Base analysis on {repo_url}"

    def get_supported_languages(self) -> list[str]:
        return ["python"]

class CodeGraphAnalyzer(BaseAnalyzer):
    @override
    def analyze_repository(self, repo_url: str) -> str:
        return f"CodeGraph technical indexing on {repo_url}"

    @override
    def get_supported_languages(self) -> list[str]:
        return ["python", "javascript", "typescript"]

analyzer = CodeGraphAnalyzer()
print(analyzer.analyze_repository("https://github.com/pallets/flask"))
print("Supported:", analyzer.get_supported_languages())
