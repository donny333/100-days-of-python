#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for number in range(0, nr_letters):
    password += random.choice(letters)

for number in range(0, nr_numbers):
    password += random.choice(numbers)

for number in range(0, nr_symbols):
    password += random.choice(symbols)

print(f"New password is:\n{password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_as_list = []

for number in range(0, nr_letters):
    password_as_list += random.choice(letters)

for number in range(0, nr_numbers):
    password_as_list += random.choice(numbers)

for number in range(0, nr_symbols):
    password_as_list += random.choice(symbols)

hard_password = ""

for number in range(0, len(password_as_list)):
    random_number = random.randint(0, len(password_as_list) - 1)
    hard_password += password_as_list[random_number]
    password_as_list.pop(random_number)

print(f"New hard password is:\n{hard_password}")