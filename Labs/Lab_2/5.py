events = [
    {"title": "Math", "start": "09:00", "end": "10:30"},
    {"title": "English", "start": "10:00", "end": "11:00"}
]

#Функция, чтобы перевести время в число (например, "09:30" -> 930)
def to_number(time_str):
    return int(time_str.replace(":", ""))

#Проверка корректности времени
for e in events:
    if to_number(e["start"]) >= to_number(e["end"]):
        print("Ошибка во времени у события:", e["title"])

#Сортировка по времени начала
events.sort(key=lambda x: to_number(x["start"]))

#Поиск пересечений
for i in range(len(events)):
    for j in range(i + 1, len(events)):
        if to_number(events[i]["end"]) > to_number(events[j]["start"]):
            print(f"Конфликт: {events[i]['title']} ({events[i]['start']}–{events[i]['end']}) и "
                  f"{events[j]['title']} ({events[j]['start']}–{events[j]['end']})")