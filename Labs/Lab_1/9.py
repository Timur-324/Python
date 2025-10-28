text = input("Enter the text: ")
words = text.split()
if len(words) == 0: #если образовавшийся список пустой, то значит пользователь ничего не ввёл
    print("You entered nothing")
else:
    longest = max(words, key=len) #берём максимальный элемент из words по длине с помощью key=len
    print(f"The most wide word: {longest}")
    print(f"Length of this words is: {len(longest)} symbols")