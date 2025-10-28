print("Please enter two numbers and one operator.")
print("Available operations: addition - '+', subtraction - '-',\
multiplication - '*', division - '/'")
print("The program will go on until you don't type stop.")
print("First type first number, than second number and at the end operator.")
stop_word = "none"
while stop_word != "stop":
    num1 = int(input())
    num2 = int(input())
    operator = str(input())
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    print("If you want to stop operations type 'stop', else just put 'no'")
    stop_word_extra = str(input())
    if stop_word_extra == "stop":
        break
    else:
        print('Enter a new numbers and operator.')
        continue