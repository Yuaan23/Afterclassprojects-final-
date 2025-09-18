# Importing necessary libraries
import random
from colorama import init, Fore, Style
init(autoreset=True)


# Rock Paper Scissors Game main code
def user_choice():
    choices = ['rock', 'paper', 'scissors']
    choice = None  # Initialize choice before using it
    while choice not in choices:
        choice = input(Fore.GREEN + "Choose Rock, Paper, or Scissors: ").lower()
    return choice

def computer_choice():
    # Remove Fore.CYAN from the list, only use it for printing
    return random.choice(['rock', 'paper', 'scissors'])

# ...existing code...

# Winner winner chicken dinner
def determine_winner(user, computer):
    if user == computer:
        return print(Fore.YELLOW + "It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return print(Fore.YELLOW + "You win!")
    else:
        return print(Fore.YELLOW + "Computer wins!")

def chat():
    print(Fore.LIGHTMAGENTA_EX + "Welcome to Rock Paper Scissors!")
    name = input(Fore.LIGHTMAGENTA_EX + "What is your name?" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + f"Nice to meet you {name}! Let's play!\n\n\n")
    user = user_choice()
    computer = computer_choice()
    print(Fore.LIGHTRED_EX + f"You chose: {user}")
    print(Fore.LIGHTRED_EX + f"Computer chose: {computer}")
    print(determine_winner(user, computer))

# Call the chat function to start the game
if __name__ == "__main__":
    chat()