import re

with open('neutral_words.txt', 'r', encoding='utf-8') as file:
    text = file.read().lower()

words = re.split(r',\s|\s|:\s|;\s|\?\s|.\s', text)

set_words = set()
for word in words:
    if not word in set_words:
        set_words.add(word)
print(', '.join(set_words))