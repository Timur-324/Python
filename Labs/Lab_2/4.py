# Ввод данных
text = input("Enter the text:\n")
top_n = int(input("How many most popular words you want to see?:\n"))
min_len = int(input("Type minimal length of the word:\n"))

# Убираем знаки
for ch in ",.!?;:-()\"'«»":
    text = text.replace(ch, "")

# Приводим к нижнему регистру и разбиваем на слова
words = text.lower().split()

# Фильтруем слова по длине
filtered_words = []
for w in words:
    if len(w) > min_len:
        filtered_words.append(w)

# Подсчёт слов вручную
freq = {}
for w in filtered_words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

# Подсчёты
word_count = len(filtered_words)
char_count = 0
for w in filtered_words:
    char_count += len(w)

# Сортируем по убыванию частоты
sorted_words = []
# freq — это словарь вида {'слово': количество}
# Сначала превращаем его в список пар [("слово", число), ...]
word_list = list(freq.items())

#фильтруем по количеству
for i in range(len(word_list)):
    for j in range(i + 1, len(word_list)):
        if word_list[j][1] > word_list[i][1]:
            word_list[i], word_list[j] = word_list[j], word_list[i]

# Результаты
print(f"\nHow many words : {word_count}")
print(f"How many symbols: {char_count}\n")
print(f"Top-{top_n} most popular words:")
# Берём только первые top_n слов
sorted_words = word_list[:top_n]
# Выводим результат
for pair in sorted_words:
    word = pair[0]
    count = pair[1]
    print(word, "-", count)