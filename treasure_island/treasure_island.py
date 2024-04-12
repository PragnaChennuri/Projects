# a simple treasure island game where the user is presented choices. Based on their answer, the user will either find the treasure or they will face various challenges and dangers

print("Welcome to Treasure Island, where you will unlock new things at every turn, from hidden riches to untold adventures. Prepare to embark on a journey of discovery unlike any other.")
user_choice = input("You stand before the stone message, contemplating your decision. Will you choose left (L) or right (R)? Your choice will determine the challenges you face and the treasure you seek. Choose wisely, for the island holds many secrets, and only the chosen path will lead to victory: ")
if(user_choice == "R"):
    print("Opting for the right path, you venture cautiously into the darkness. Suddenly, the ground gives way beneath you, and you plummet into a deep hole. Your adventure has come to a premature end, but fear not, for the spirit of adventure lives on. Will you return to Treasure Island someday, armed with newfound knowledge and determination? Or will your tale remain unfinished, a cautionary reminder of the perils that await those who seek fortune in the unknown? The choice is yours. Until then, may your journeys be filled with wisdom and courage.")
else:
    print("You decide to take the left path, embarking on a journey filled with riddles and puzzles that test your intellect and wit. Answer correctly to progress deeper into the island, but beware - a wrong answer could lead to disaster! Navigate the challenges with cunning and skill, and you may just uncover the treasure hidden within.")

    user_choice = input("As you proceed, you reach a river with a swift current. You are presented with two options: 'Swim' or 'Wait.' Choose one wisely: ")
    if(user_choice == "Swim"):
        print("You brave the river's current and begin to swim across. Suddenly, a massive trout emerges from the depths, its sharp teeth glinting in the sunlight. With a swift strike, it attacks, ending your adventure here.")
    else:
        print("You choose to wait, wisely opting to assess the situation before proceeding. After a few moments, the current slows, and you notice a fallen tree trunk drifting by. Seizing the opportunity, you use the makeshift raft to safely cross the river, continuing your quest.")

        user_choice = input("You've braved the perils of the river and now face three imposing doors, each hiding its own fate. Will you unlock the path to glory, or fall victim to the dangers beyond? Before you, three towering doors stand, each adorned with a different color - red, blue, and yellow. Your decision will shape your adventure's outcome. Choose wisely, for only one door leads to victory. Enter 'yellow', 'red,' or 'blue': ")

        if(user_choice == "red"):
            print("You bravely step forward and choose the red door, but as it swings open, you're met with a wall of searing flames. The intense heat consumes you, and your journey ends here.")
        elif(user_choice == "blue"):
            print("Opting for the blue door, you push it open to reveal a dark, cavernous chamber. Suddenly, from the shadows, a fierce beast lunges forward, its fangs bared and hunger in its eyes. With a mighty roar, it pounces, and your adventure comes to a tragic end.")
        elif(user_choice == "yellow"):
            print("With caution and resolve, you select the yellow door. As it creaks open, a chamber bathed in golden light unfolds before you, treasures gleaming in the distance. Congratulations! You've successfully claimed the legendary treasure of Treasure Island. Your courage and cunning led to victory. As you ponder your next adventure, may your journeys be filled with excitement and discovery!")
            
            #ASCII art taken from Dr.Angela Yu's Udemy Course: 100 Days of Code: The Complete Python Pro Bootcamp
            print('''
            *******************************************************************************
                    |                   |                  |                     |
            _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                    |                `"=._o`"=._      _`"=._                     |
            _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                    |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
            _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')