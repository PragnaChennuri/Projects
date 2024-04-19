# A password generator that allows users to customize the length and composition of their passwords. 
# Users can choose the number of letters, symbols, and numbers in their password and opt to randomize the order of characters.


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# allowing the user to indicate the number of passwords they would like 
print("Welcome to the PyPassword Generator!")
password_num = int(input(f"Please indicate the number of password you would like: "))

# based on the number of passwords the user has entered the loop will execute that many times
# for each iteration the user will be asked the number of letters, symbols, and numbers they would like to include in their password
# and, the user can choose to have their password randomized or follow a specific pattern which would be letter, symbols followed by the numbers
i = 1
while i <= password_num:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    r_order = input("Please indicate if you would like the order of your password to be randomised. Type 'yes' or 'no': ")

    # using the choices method from the random module we can now randomly choose the number of letters, symbols, and numbers
    # as indicated by the user by setting the frequency to the number that the user gave
    r_letters = random.choices(letters, k=nr_letters)
    r_symbols = random.choices(symbols, k = nr_symbols)
    r_num = random.choices(numbers, k = nr_numbers)

    # concatenating the letters, symbols, and numbers but will return a list
    password = r_letters + r_symbols + r_num

    # based on the user's choice to have their password randomized or not it will enter one of the two conditionals

    # if the user wants to randomize the order of the password then we use the shuffle method which will jumble the order
    # of the password list
    if(r_order == "yes"):
        random.shuffle(password)
        # using .join method to make the password to a string
        s_password = ''.join(password)
        print(f"Your password is: {s_password}\n")

    # if the user wants the password to be a specific order we simply call password which contains the concatenated version
    # of the password except in the form of a list
    # use .join method to make the password to a string
    else:
        c_password = ''.join(password)
        print(f"Your password is: {c_password}\n")
    
    # don't forget to increment the iterating variable!!!
    i += 1
