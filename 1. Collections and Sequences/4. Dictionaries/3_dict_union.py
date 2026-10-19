# ADVANCED DICTIONARY MERGING & OVERRIDE TECHNIQUES

# 1. SO SÁNH CÁC PHƯƠNG PHÁP GỘP DICTIONARY TRONG PYTHON:
default_config = {"theme": "light", "font_size": 14, "auto_save": True}
custom_config = {"theme": "dark", "font_size": 16}

# Cách 1: Toán tử '|' (Union tạo dict mới)
# - Ưu điểm: Trực quan, bảo toàn dict gốc (không bị mutate).
# - Quy tắc ghi đè: Toán hạng bên phải luôn thắng khi trùng key.
merged_pipe = default_config | custom_config
print("Merged (|):", merged_pipe)

# Cách 2: Cập nhật tại chỗ với '|='
base_config = {"host": "localhost", "port": 8000}
base_config |= {"port": 9000, "debug": True}
print("Updated in-place (|=):", base_config)

# Cách 3: Dictionary Unpacking {**d1, **d2}
merged_unpack = {**default_config, **custom_config}
print("Merged ({**}):", merged_unpack)


# 2. HẠN CHẾ CỦA TOÁN TỬ '|' (SHALLOW MERGE) VỚI DICT LỒNG NHAU:
# Toán tử `|` chỉ gộp nông (Shallow Merge) ở cấp độ 1:
base_app = {
    "server": {"host": "127.0.0.1", "port": 8080},
    "logging": {"level": "INFO"}
}
override_app = {
    "server": {"port": 9000}  # Chỉ muốn ghi đè port, giữ nguyên host
}

# Khi dùng '|', toàn bộ sub-dict 'server' bị thay thế -> Bị mất trường 'host'!
shallow_merged = base_app | override_app
print("\nShallow merged (host lost!):", shallow_merged["server"]) # {'port': 9000}


# 3. KỸ THUẬT DEEP MERGE (GỘP ĐỆ QUY DICT LỒNG NHAU):
# Ứng dụng: Gộp file cấu hình đa môi trường (Default -> Staging/Prod -> Environment Variables)
def deep_merge(base: dict, override: dict) -> dict:
    """Gộp đệ quy 2 dict lồng nhau mà không làm mất các trường con của base."""
    result = base.copy()
    for key, val in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            result[key] = deep_merge(result[key], val)
        else:
            result[key] = val
    return result

full_config = deep_merge(base_app, override_app)
print("Deep merge (preserves host & overrides port):", full_config["server"])
# {'host': '127.0.0.1', 'port': 9000}
