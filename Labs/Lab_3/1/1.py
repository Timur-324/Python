with open("Labs/Lab_3/1/input_file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lineslength = 0
linesquantity = 0

for line in lines:
    if '\n' in line:
        line = line.replace('\n', '')
    lineslength += len(line)
    linesquantity += 1



print(f"\nLines quantity: {linesquantity}\n"
      f"Quantity of symbols: {lineslength}\n"
      f"Mean quantity of symbols in each line: {lineslength / linesquantity}")