# **README.md File**<br>
A password generator that allows users to customize the length and composition of their passwords. Users can choose the number of letters, symbols, and numbers in their password and opt to randomize the order of characters.<br>

Random Module Methods:
- The password generator employs various methods from the random module:
    - random.choices(): Used to randomly select characters for the password.
    - random.shuffle(): Employed to shuffle the characters within the password if the user opts for randomization.
- Loops: Utilized loops to iterate through the password generation process, ensuring that the user's specifications are met.
- Conditionals: Incorporated conditionals to provide users with the option to randomize the order of characters in their password or maintain the order generated.