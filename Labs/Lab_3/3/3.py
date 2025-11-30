with open("Labs/Lab_3/3/article.txt", "r", encoding="utf-8") as file:
    text = file.read()

paragraphs = text.split("\n\n")
i = 1
for paragraph in paragraphs:
    with open(f"part_{i}.txt", "w", encoding="utf-8") as f:
        f.write(paragraph)
    i += 1
