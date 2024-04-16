#ASCII art taken from Dr.Angela Yu's Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#imported the random module
import random

#list called moves that stores the moves along with the associated ASCII art
moves = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors Game!\n")
user_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#we output the ASCII art of the user's choice
print(moves[user_move])

#using the random module to output the computer's random ASCII art choice
comp_move = random.randint(0, len(moves) - 1)
print(f"Computer Choose:\n{moves[comp_move]}")

# all the possible combination that can be encountered during the game
if(user_move == comp_move):
    print("It's a draw, nobody wins!")
elif((user_move == 0) and (comp_move == 1)):
    print("Oh no, the computer won!")
elif((user_move == 0) and (comp_move == 2)):
    print("Congrats, you won!")
elif((user_move == 1) and (comp_move == 2)):
    print("Oh no, the computer won!")
elif((user_move == 1) and (comp_move == 0)):
    print("Congrats, you won!")
elif((user_move == 2) and (comp_move == 0)):
    print("Oh no, the computer won!")
elif((user_move == 2) and (comp_move == 1)):
    print("Congrats, you won!")


