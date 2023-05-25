import random
import string


# Рекурсивна функція для обчислення суми всіх чисел у списку
def recursive_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += recursive_sum(item)  # Рекурсивний виклик для списків
    return total

# Приклад використання


nested_list = [1, 2, [3, 4, [5, 6]], 7, [8, [9, 10]]]
result = recursive_sum(nested_list)
print("Sum:", result)


# Функція для повторення елементів списку задану кількість разів
def repeat_elements(words, num):
    repeated_list = []
    for word in words:
        repeated_list.extend([word] * num)
    return repeated_list

# Приклад використання


word_list = ['apple', 'banana', 'cherry']
repeat_num = 3
result = repeat_elements(word_list, repeat_num)
print("Repeated List:", result)


# Функція для генерації випадкового паролю
def generate_password():
    length = 4
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Функція для перевірки коректності паролю


def check_password(password):
    # Виконується якась логіка перевірки пароля
    return True if len(password) == 4 else False

# Приклад використання


password = generate_password()
print("Generated Password:", password)
print("Password is Valid:", check_password(password))
