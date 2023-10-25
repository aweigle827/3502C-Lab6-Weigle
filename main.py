"""
Authors: Aden Weigle & Gian Carlo
"""


def menu():
    return print("""Menu 
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: """, end='')
    ans = input()
    while True:
        if ans == '1':
            password = input("Please enter your password to encode: ")
            encode(password)


def encode(password):
    list = []
    new_password = ''
    for i in password:
        if i < '7':
            x = int(i) + 3
            list.append(str(x))
        elif i >= '7':
            x = int(i) - 7
            list.append(str(x))
    for j in list:
        new_password += j
    return print('Your password has been encoded and stored!')
    return new_password