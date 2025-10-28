print("Please enter a number.")
print("The program will go on until you don't type stop.")
print("Your number:")
stop_word = ""
summ = 0
while stop_word != "stop":
    num = int(input())
    print("You want to continue? If Yes print 'yes', else print 'stop'")
    stop_word = str(input())
    if stop_word == "stop":
        summ = summ + num
        print(summ)
        break
    else:
        summ = summ + num
        print('Enter a new number.')
        continue