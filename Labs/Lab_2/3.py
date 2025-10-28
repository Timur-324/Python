import random #модуль для работы со случайными числами
import string 
"""
string - модуль для работы со всеми латинскими буквами всех регистров(string.ascii_letters)
и цифрами(string.digits)
"""

def make_password_generator(length):
    # набор всех символов 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    chars = string.ascii_letters + string.digits

    pswd = ''
    while length != 0:
        pswd += random.choice(chars)
        length -= 1
    return pswd


print("Hello! Type length of the password that you want:")
length = int(input())
gen = make_password_generator(length)
print(gen)