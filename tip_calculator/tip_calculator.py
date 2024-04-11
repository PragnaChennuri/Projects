# A simple python program that calculates the tip based on the responses given by the user
# the program takes in the following: total bill, tip, and number of ways to split
# it will final output the total amount each person has to pay including the tip

print("Welcome! This is a simple tip calculator that will seamlessly help you split your bill equally among your group.\n")
print("Please enter the total amount, the amount of tip you would like to add, and how many people you would like to split the bill between when prompted.\n")
total_bill = float(input("What is the total amount: $"))
custom_tip = int(input("Please enter the tip amount: "))
num_people = int(input("How many ways would you like to split the bill: "))
# converting the tip to a decimal
tip_percent = float(custom_tip / 100)
# calcualting the total amount including the tip
bill_with_tip = float(total_bill + (tip_percent * total_bill))
# dividing the total bill with the number of people
bill = bill_with_tip / num_people
#final amount displayed
print(f"Thank you for your responses. We have calculated that each person needs to pay ${bill:.2f}. Hope that helps!")
