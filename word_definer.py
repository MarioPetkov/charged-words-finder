import re
from tabulate import tabulate
import matplotlib.pyplot as plt

# Функция за четене на думите от файл
def read_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        # Връщаме множество от думите, прочетени от файла
        return set(file.read().lower().split(', '))

# Функция за категоризиране на думите
def categorize_words(text, positive_words, negative_words, neutral_words):
    # Разделяне на текста на думи
    words = re.findall(r'\b\w+\b', text)

    # Категоризиране на думите
    found_positive_words = set()
    found_negative_words = set()
    found_neutral_words = set()

    for word in words:
        if word in positive_words:
            found_positive_words.add(word)
        elif word in negative_words:
            found_negative_words.add(word)
        elif word in neutral_words:
            found_neutral_words.add(word)

    return found_positive_words, found_negative_words, found_neutral_words

# Функция за извеждане на табличен формат
def display_table(found_positive_words, found_negative_words, found_neutral_words):
    head = ['Тип заредени думи', 'Брой']
    data = [["Положително", len(found_positive_words)],
            ["Отрицателно", len(found_negative_words)],
            ["Неутрално", len(found_neutral_words)]]
    print(tabulate(data, headers=head, tablefmt='grid'))

# Функция за извеждане на текстов формат
def display_text(found_positive_words, found_negative_words, found_neutral_words):
    print("\nТекстов формат:")
    print("Положителни думи:", ', '.join(found_positive_words))
    print("Отрицателни думи:", ', '.join(found_negative_words))
    print("Неутрални думи:", ', '.join(found_neutral_words))

# Функция за извеждане на графичен формат
def display_chart(found_positive_words, found_negative_words, found_neutral_words):
    labels = ['Положителни', 'Отрицателни', 'Неутрални']
    sizes = [len(found_positive_words), len(found_negative_words), len(found_neutral_words)]
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'red', 'blue'])
    plt.axis('equal')
    plt.title('Диаграма на типовете заредени думи')
    plt.show()

# Основна функция
def main():
    document = input('Моля въведете името на текстовия документ: ')
    file_name_with_extension = document + '.txt'

    # Четене на текста и списъците с думи
    with open(file_name_with_extension, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Зареждане на положителните, отрицателните и неутралните думи
    positive_words = read_words('positive_words.txt')
    negative_words = read_words('negative_words.txt')
    neutral_words = read_words('neutral_words.txt')

    # Категоризиране на думите
    found_positive_words, found_negative_words, found_neutral_words = categorize_words(text, positive_words, negative_words, neutral_words)

    # Извеждане на информацията в табличен формат
    display_table(found_positive_words, found_negative_words, found_neutral_words)

    # Извеждане на информацията в текстов формат
    display_text(found_positive_words, found_negative_words, found_neutral_words)

    # Извеждане на информацията в графичен формат
    display_chart(found_positive_words, found_negative_words, found_neutral_words)

if __name__ == "__main__":
    main()
