# Đọc file TOML với thư viện chuẩn tomllib (Python 3.11+ PEP 680)
import tomllib

# Chuỗi cấu hình định dạng TOML (chuẩn hiện đại của pyproject.toml)
toml_data = """
[project]
name = "code-graph-analyzer"
version = "1.0.0"
dependencies = ["kuzu", "tree-sitter"]

[database]
backend = "kuzu"
location = "./data/flask"
"""

# Parse chuỗi TOML thành dictionary bằng tomllib.loads()
config = tomllib.loads(toml_data)

print("Project Name:", config["project"]["name"])
print("Dependencies:", config["project"]["dependencies"])
print("Database Backend:", config["database"]["backend"])
