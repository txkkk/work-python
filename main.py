import json


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def info(self):
        return {"first_name": self.first_name, "last_name": self.last_name}


class Storage:
    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def get(self, prefix):
        filtered_words = sorted([word for word in self.words if word.startswith(prefix)])
        return filtered_words[:5]


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def to_json(self):
        students_info = [student.info() for student in self.students]
        course_data = {
            "course_name": self.course_name,
            "students": students_info
        }
        return json.dumps(course_data)


# Приклад використання

# Створюємо об'єкти студентів
student1 = Student("John", "Doe")
student2 = Student("Jane", "Smith")
student3 = Student("Alice", "Johnson")

# Викликаємо метод info для студента
print(student1.info())  # {'first_name': 'John', 'last_name': 'Doe'}

# Створюємо об'єкт зберігання
storage = Storage()

# Додаємо слова до зберігання
storage.add("apple")
storage.add("banana")
storage.add("cat")
storage.add("dog")

# Отримуємо відфільтрований список слів
filtered_words = storage.get("c")
print(filtered_words)  # ['cat']

# Створюємо об'єкт курсу
course = Course("Python Programming")

# Додаємо студентів на курс
course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

# Перетворюємо об'єкт курсу в JSON
course_json = course.to_json()
print(
    course_json)  # {"course_name": "Python Programming", "students": [{"first_name": "John", "last_name": "Doe"}, {"first_name": "Jane", "last_name": "Smith"}, {"first_name": "Alice", "last_name": "Johnson"}]}
