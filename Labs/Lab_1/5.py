stop_word = ""
while stop_word != "stop":
    print("Type your number:")
    num = int(input())
    if num < 2:
        print("The number is ruling out!")
    elif num == 3:
        print("The number is prime!")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("The number is not prime!")
                break
            else:
                print("The number is prime!")
                break
    print("If you want to stop operation type 'stop', else 'no'")
    stop_word = str(input())