"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))
with open(INPUT_FILE, 'r', encoding = "UTF-8") as f:
    header = next(f)

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)
    curr_best = ["placeholder", 0]
    math_grades = []
    python_grades = []
    english_grades = []
    student_counter = 0
    for line in f:
        line = line.strip()
        words = line.split(",")
        name = words[0]
        math_grade = int(words[1])
        python_grade = int(words[2])
        english_grade = int(words[3])
# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент
        math_grades.append(math_grade)
        python_grades.append(python_grade)
        english_grades.append(english_grade)
        student_counter += 1

        avg_grade = (math_grade + python_grade + english_grade)/3
        if avg_grade > curr_best[1]:
            curr_best[0] = name
            curr_best[1] = avg_grade
# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)
average_english = sum(english_grades) / student_counter
average_math = sum(math_grades) / student_counter
average_python = sum(python_grades) / student_counter

# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.
print("Середній бал по класу:")
print(f"math: {average_math:.1f}")
print(f"python: {average_python:.1f}")
print(f"english: {average_english:.1f}")
print(" ")
print(f"Найкращий студент: {curr_best[0]} ({curr_best[1]})")

with open(OUTPUT_FILE, 'w', encoding= "UTF-8") as f:
    f.write("Середній бал по класу:\n")
    f.write(f"math: {average_math:.1f}\n")
    f.write(f"python: {average_python:.1f}\n")
    f.write(f"english: {average_english:.1f}\n")
    f.write(" \n")
    f.write(f"Найкращий студент: {curr_best[0]} ({curr_best[1]:.1f})")


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
