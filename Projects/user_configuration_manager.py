def add_setting(settings: dict, setting_tuple: tuple) -> str:
    key, value = setting_tuple
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings: dict, setting_tuple: tuple) -> str:
    key, value = setting_tuple
    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings: dict, key: str) -> str:
    key = str(key).lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."

    output = "Current User Settings:\n"
    for key, value in settings.items():
        output += f"{key.capitalize()}: {value}\n"

    return output

test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
}

print(add_setting(test_settings, ("font_size", 14)))
print(update_setting(test_settings, ("theme", "light")))
print(delete_setting(test_settings, "volume"))
print(view_settings(test_settings))


# 8. Bài tập thực hành nâng cao: Trình phân tích Tần suất Từ (Word Frequency Analyzer)

def analyze_text_frequency(text: str) -> dict[str, int]:
    """
    Phân tích tần suất xuất hiện của mỗi từ trong văn bản.
    Kết quả trả về dictionary với key là từ (viết thường, không dấu) và value là số lần xuất hiện.
    Sử dụng strip() để loại khoảng trắng thừa ở hai đầu, lower() để chuẩn hóa,
    và xây dựng dictionary thông qua vòng lặp for với kiểm tra điều kiện.
    """
    frequency = {}
    cleaned_text = text.strip().lower()
    words = cleaned_text.split()

    for word in words:
        word = word.strip(",.!?")
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    return frequency


def print_top_words(frequency: dict[str, int], n: int) -> None:
    """
    In ra n từ có tần suất cao nhất từ dictionary tần suất.
    Sử dụng sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    để sắp xếp các cặp (key, value) theo giá trị giảm dần.
    """
    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    print(f"Top {n} most frequent words:")
    for word, count in sorted_words[:n]:
        print(f"  {word}: {count}")


# Kiểm tra hoạt động
text_to_analyze = "Hello world! Hello Python! Python is great."
analyzed = analyze_text_frequency(text_to_analyze)
print_top_words(analyzed, 3)

