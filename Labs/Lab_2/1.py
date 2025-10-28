def process_words(words):
    lower_words = map(lambda words: words.lower(), words)
    #с помощью мап применяю действия для всех элементов.
    # С помощью ламбды беру слово и превращяю его в слово с мелкими регистрами.
    filtered_words = filter(lambda words: len(words) > 3, lower_words)
    #с помощью filter оставляю только то, что проходит под условие.
    #внутри скобок условия того, что если слово больше трёх символов, тогда оставляем.
    return sorted(filtered_words)
    #c помощью sorted сортирую слова по алфавиту.

user_input = input("Enter the words separeted by space:")
words = user_input.split()

result = process_words(words)
print("The result of function:", result)