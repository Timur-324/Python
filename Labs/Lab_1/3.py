print("Please enter a number.")
print("The program will go on until you don't type stop.")
print("Your number:")
stop_word = ""
while stop_word != "stop":
    num = int(input())
    if num % 2 == 0:
        print("Your number is even!")
    else:
        print("Your number is not even!")
    print("If you want to stop operations type 'stop', else put 'no'")
    stop_word = str(input())
    if stop_word == "stop":
        break
    else:
        print('Enter a new number.')
        continue


