#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
remain_letters = nr_letters
remain_symbols = nr_symbols
remain_numbers = nr_numbers
random_char_index = 0
password_string = ''
outer = [1, 3]
#total_chars = nr_letters + nr_symbols + nr_numbers
remain_total = remain_letters + remain_symbols + remain_numbers
#print(remain_total)

for i in range(1, remain_total + 1):
    if remain_letters > 0 and remain_symbols > 0 and remain_numbers > 0:
        random_char_index = random.randint(1, 3)  # random pick 1,2, or 3
    elif remain_letters > 0 and remain_symbols > 0 and remain_numbers == 0:
        random_char_index = random.randint(1, 2)  # random pick 1 or 2
    elif remain_letters > 0 and remain_symbols == 0 and remain_numbers > 0:
        random_char_index = random.choice(outer)  # random pick 1 or 3, have to use choice and list
    elif remain_letters > 0 and remain_symbols == 0 and remain_numbers == 0:
        random_char_index = 1   # only letters remaining
    elif remain_letters == 0 and remain_symbols > 0 and remain_numbers > 0:
        random_char_index = random.randint(2, 3)  # random pick 2 or 3
    elif remain_letters == 0 and remain_symbols > 0 and remain_numbers == 0:
        random_char_index = 2   # only symbols remaining
    elif remain_letters == 0 and remain_symbols == 0 and remain_numbers > 0:
        random_char_index = 3    # only numbers remaining
    elif remain_letters == 0 and remain_symbols == 0 and remain_numbers == 0:
        random_char_index = 0  #done

## could use random.choice for these instead
    if random_char_index == 1:
        random_letter = letters[random.randint(0, len(letters) - 1)]
        password_string += random_letter
        remain_letters -= 1
        #print(f"remain letters: {remain_letters}")
    elif random_char_index == 2:
        random_symbol = symbols[random.randint(0, len(symbols) - 1)]
        password_string += random_symbol
        remain_symbols -= 1
        #print(f"remain symbols: {remain_symbols}")
    elif random_char_index == 3:
        random_number = numbers[random.randint(0, len(numbers) - 1)]
        password_string += random_number
        remain_numbers -= 1
        #print(f"remain numbers: {remain_numbers}")

print(password_string)
#print(len(password_string))
