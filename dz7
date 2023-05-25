import os
from collections import Counter


# Функція-декоратор retry
def retry(attempts=5, desired_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(attempts):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
            print("Не вдалося досягнути бажаного значення")
            return result
        return wrapper
    return decorator


# Функція для копіювання вмісту файлу
def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file:
            content = source_file.read()
        with open(destination_path, 'w') as destination_file:
            destination_file.write(content)
        print("Файл успішно скопійовано.")
    except FileNotFoundError:
        print("Файл не знайдено.")


# Функція для читання великого файлу
def read_large_file(file_path):
    line_count = 0
    byte_size = os.path.getsize(file_path)
    top_chars = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
            top_chars.update(line.strip())

    # Видалення символів перенесення рядка та пробілів зі словника
    del top_chars['\n']
    del top_chars[' ']

    # Отримання топ-3 символів
    top_chars = top_chars.most_common(3)

    result = {
        'line_count': line_count,
        'byte_size': byte_size,
        'top_chars': top_chars
    }
    return result


# Приклад використання

# Функція, яку будемо декорувати
@retry(attempts=3, desired_value=100)
def calculate_sum(a, b):
    return a + b

# Приклад виклику декорованої функції


result = calculate_sum(10, 20)
print("Результат обчислення:", result)

# Приклад використання функції для копіювання файлу
copy_file("source.txt", "destination.txt")

# Приклад використання функції для читання великого файлу
file_info = read_large_file("large_file.txt")
print("Кількість рядків:", file_info['line_count'])
print("Розмір файла (в байтах):", file_info['byte_size'])
print("Топ-3 символи:", file_info['top_chars'])
