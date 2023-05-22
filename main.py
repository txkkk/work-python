def reverse_string(input_string):
    return input_string[::-1]


def get_string_length(input_string):
    return len(input_string)


def string_to_list(input_string):
    return list(input_string)


def merge_every_third_element(char_list):
    return '|'.join(char_list[2::3])


def count_characters_count(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = input_string.count(char)
    return char_count


def count_characters_no_count(input_string):
    char_count = {}
    for char in input_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


def find_longest_string(string_list):
    longest_string = ''
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string


def divide_and_glue(input_string, delimiter):
    splitted_list = input_string.split(delimiter)
    sorted_string = delimiter.join(sorted(splitted_list))
    return sorted_string


def convert_ascii(numbers):
    characters = [chr(num) for num in numbers]
    return ''.join(characters)


# Завдання 1: Створити змінну рядкового типу

input_string = "Hello, world!"


# Завдання 2: Вивести рядок в оберненому порядку
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

# Завдання 3: Записати довжину рядка в другу змінну
string_length = get_string_length(input_string)
print("String length:", string_length)

# Завдання 4: Створити третю змінну - список символів рядка
char_list = string_to_list(input_string)
print("Character list:", char_list)

# Завдання 5: Створити четверту змінну - строку з кожного третього символу списку
merged_string = merge_every_third_element(char_list)
print("Merged string:", merged_string)

# Завдання 6: Створити функцію, що повертає словник з кількістю входжень символів
char_count_with_count = count_characters_count(input_string)
print("Character count with count method:", char_count_with_count)

char_count_without_count = count_characters_no_count(input_string)
print("Character count without count method:", char_count_without_count)

# Завдання 7: Створити функцію, що повертає найбільший рядок зі списку
string_list = ["apple", "banana", "cherry", "durian"]
longest_string = find_longest_string(string_list)
print("Longest string:", longest_string)

# Завдання 8: Створити функцію, що склеює відсортовані елементи рядка з роздільником
input_string = "c/a/b"
delimiter = "/"
sorted_string = divide_and_glue(input_string, delimiter)
print("Sorted string:", sorted_string)


# Приклад використання
numbers = [119, 101, 108, 108, 32, 100, 111, 110, 101]
result = convert_ascii(numbers)
print("Result:", result)
