with open("Labs/Lab_3/2/log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()



for line in lines:
    if "ERROR" in line:
        print(f"#{lines.index(line)} {line}")