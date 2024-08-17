import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
                      '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\',
                      ']', '^', '_', '`', '{', '|', '}', '~']
print('Welcome to this Password Generator')
nr_letters = int(input('How many letters would you like in your Password? '))
nr_numbers = int(input('How many numbers would you like? '))
nr_symbols = int(input('How many Symbols would you like? '))
# Easy Method
# password = ''
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for number in range(0, nr_numbers):
#     password += random.choice(numbers)
# for symbol in range (0, nr_symbols):
#     password+= random.choice(symbols)
# print(f'your Password is : {password}')

# Hard Method
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for symbol in range (0, nr_symbols):
    password_list+= random.choice(symbols)
print(password_list)

# using shuffle method
random.shuffle(password_list)
print(password_list)

# using another for loop
password = ''
for char in password_list:
    password += char
print(f'your password is: {password}')
