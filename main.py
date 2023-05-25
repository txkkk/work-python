import random
import string
import time


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


def repeat_elements(words, num):
    repeated_list = []
    for _ in range(num):
        repeated_list.extend(words)
        words.append(words[0])
        words = words[1:]
    return repeated_list[:num]


def generate_password():
    password_length = 4
    characters = string.ascii_letters
    password = ''
    for _ in range(password_length):
        for char in characters:
            guess = password + char
            start_time = time.time()
            check_password(guess)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 0.1:
                password += char
                break
    return password


def check_password(guess):
    password = generate_password()
    return guess == password


# Приклад використання

# Функція повторення елементів списку
words_list = ['apple', 'banana', 'cherry']
repeated = repeat_elements(words_list, 7)
print(repeated)
# Output: ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple']

# Функція генерації та перевірки паролю
password = generate_password()
print(password)
# Example output: "AbCd"

print(check_password('AbCd'))
# True
print(check_password('abcd'))
# False
