import math
print("Please enter a number.")
print("The program will go on until you don't type stop.")
print("Your number:")
stop_word = ""
while stop_word != "stop":
    num_fac = int(input())
    print(math.factorial(num_fac))
    print("If you want to stop operations type 'stop', else put 'no'")
    stop_word = str(input())
    if stop_word == "stop":
        break
    else:
        print('Enter a new number.')
        continue