from random import randint
random_number = randint(1, 100)
print("I think of a number. Try to guess it!")
print("Type number and I will give you a clue is it true or false.")
user_num = 0
while user_num != random_number:
    user_num = int(input())
    if user_num < random_number:
        print("The number is to small")
    elif user_num > random_number:
        print("The number is to big")
    else:
        print("Your right! I thought of a number:" + str(user_num))
