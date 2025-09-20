# Multi-Feature Chatbot with TravelBot, Sentiment Analysis, Rock Paper Scissors, Info Search, and TicTacToe

'''
    THIS IS MY FIRST EVER CHATBOT PROJECT
    I NAMED IT YUAAN GPT
    IT TOOK ME 9 DAYS TO CODE THIS ENTIRE PROJECT
    I USED SOME YOUTUBE VIDEOS TO HELP ME.
    BUT MOSTLY I CODED IT ALL BY MYSELF.
    I HOPE YOU LIKE IT!
    THANK YOU!
    - Yuaan
'''

# -------------------- IMPORTS --------------------
# Importing necessary libraries for chatbot features
import re, random, datetime, os
from colorama import Fore, Style, init
from textblob import TextBlob
from langdetect import detect
init(autoreset=True)  # Automatically reset colorama styles after each print

# -------------------- DATASETS --------------------
# Data for travel recommendations, weather, news, and time zones

# Destination Suggestion dataset for travel recommendations
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

# Weather dataset for simulated weather info
weather_data = {
    "bali": "Sunny, 30°C",
    "maldives": "Partly cloudy, 28°C",
    "phuket": "Rainy, 26°C",
    "tokyo": "Clear, 22°C",
    "paris": "Cloudy, 18°C",
    "new york": "Windy, 20°C"
}

# News headlines dataset for simulated news updates
news_headlines = [
    "Global travel demand surges in 2025.",
    "New eco-friendly resorts open in Maldives.",
    "Tokyo hosts international food festival."
]

# City timezones for local time feature
city_timezones = {
    "tokyo": 9,
    "paris": 2,
    "new york": -4
}

# File to store conversation history for memory feature
HISTORY_FILE = "travelbot_history.txt"

# -------------------- MEMORY FUNCTIONS --------------------
# Functions to save and load conversation history

def save_history(text):
    """Append a line of text to the conversation history file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as history:
        history.write(text + "\n")

def load_history():
    """Load and return the entire conversation history as a string."""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as history:
            return history.read()
    return ""

# -------------------- INPUT HANDLING --------------------
# Functions for normalizing and matching user input

def normalize_input(text):
    """Normalize user input by stripping whitespace and converting to lowercase."""
    return re.sub(r"\s+", " ", text.strip().lower())

# Keyword lists for intent matching
recommend_keywords = ["recommend", "suggest", "destination", "place"]
weather_keywords = ["weather", "forecast", "temperature"]
news_keywords = ["news", "update", "headlines"]
time_keywords = ["time", "clock", "local time"]

def match_keywords(user_input, keywords):
    """Return True if any keyword is found in the user input."""
    for kw in keywords:
        if re.search(rf"\b{kw}\b", user_input):
            return True
    return False

# -------------------- TRAVELBOT FEATURES --------------------
# Functions for travel recommendations, weather, news, and time

def recommend():
    """Recommend travel destinations based on user preference, with repeat option."""
    keep_running = True
    while keep_running:
        print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
        preference = input(Fore.YELLOW + "Where would you love to go: ")
        preference = normalize_input(preference)
        save_history(f"User asked for recommendation: {preference}")

        # Suggest a destination based on user preference
        if preference in destinations:
            suggestion = random.choice(destinations[preference])
            print(Fore.GREEN + f"TravelBot: How about visiting {suggestion}?")
            print(Fore.CYAN + "Do you like it? (yes/no): ")
            answer = input(Fore.YELLOW + "You:").strip().lower()
            save_history(f"User response to suggestion: {answer}")

            if answer == "yes":
                print(Fore.GREEN + "TravelBot: Awesome! Have a great trip!")
            elif answer == "no":
                print(Fore.RED + "TravelBot: Let's try another")
                continue  # Loop again for another suggestion
            else:
                print(Fore.RED + "TravelBot: I'll suggest again")
                continue  # Loop again for another suggestion
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
            continue  # Loop again for valid input

        # Ask if user wants another recommendation
        again = input(Fore.YELLOW + "Would you like another recommendation? (yes/no): ").strip().lower()
        if again != "yes":
            keep_running = False

def weather_info():
    """Provide simulated weather info for a location, with repeat option."""
    keep_running = True
    while keep_running:
        print(Fore.CYAN + "TravelBot: Which city or destination's weather would you like to know?")
        place = input(Fore.YELLOW + "Enter location: ").strip().lower()
        save_history(f"User asked for weather: {place}")
        info = weather_data.get(place)
        if info:
            print(Fore.BLUE + f"TravelBot: The weather in {place.title()} is {info}.")
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have weather info for that location.")

        # Ask if user wants to check another weather
        again = input(Fore.YELLOW + "Would you like to check another weather? (yes/no): ").strip().lower()
        if again != "yes":
            keep_running = False

def news_update():
    """Show simulated travel news headlines, with repeat option."""
    keep_running = True
    while keep_running:
        print(Fore.CYAN + "TravelBot: Here are the latest travel news headlines:")
        for headline in news_headlines:
            print(Fore.MAGENTA + "- " + headline)
        save_history("User asked for news updates.")

        # Ask if user wants to see news again
        again = input(Fore.YELLOW + "Would you like to see the news again? (yes/no): ").strip().lower()
        if again != "yes":
            keep_running = False

def local_time():
    """Show local time for a city based on simulated timezone data."""
    print(Fore.CYAN + "TravelBot: Which city's local time do you want?")
    city = input(Fore.YELLOW + "Enter city: ").strip().lower()
    save_history(f"User asked for local time: {city}")
    offset = city_timezones.get(city)
    if offset is not None:
        utc_now = datetime.datetime.utcnow()
        city_time = utc_now + datetime.timedelta(hours=offset)
        print(Fore.GREEN + f"TravelBot: Local time in {city.title()} is {city_time.strftime('%H:%M')}.")
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't know the timezone for that city.")

def show_history():
    """Display the conversation history from file."""
    history = load_history()
    if history:
        print(Fore.LIGHTBLACK_EX + "TravelBot: Here's your conversation history:")
        print(Fore.LIGHTBLACK_EX + history)
    else:
        print(Fore.LIGHTBLACK_EX + "TravelBot: No previous history found.")

def chat():
    """Main TravelBot chat loop for travel-related features."""
    print(Fore.CYAN + Style.BRIGHT + "Hello! I'm TravelBot. What's your name?")
    name = input(Fore.YELLOW + "Your Name: ")
    print(Fore.CYAN + f"Nice to meet you {name}!")
    save_history(f"User name: {name}")

    # Show history at start (optional)
    show_history()

    while True:
        user_input = input(Fore.YELLOW + "How may I help you: ")
        user_input_norm = normalize_input(user_input)
        save_history(f"User: {user_input}")

        # Intent matching using keywords
        if match_keywords(user_input_norm, recommend_keywords):
            recommend()
        elif match_keywords(user_input_norm, weather_keywords):
            weather_info()
        elif match_keywords(user_input_norm, news_keywords):
            news_update()
        elif match_keywords(user_input_norm, time_keywords):
            local_time()
        elif user_input_norm in ["exit", "quit", "bye"]:
            print(Fore.CYAN + f"TravelBot: Goodbye {name}! Safe travels!")
            save_history("User exited the chat.")
            break
        elif "history" in user_input_norm:
            show_history()
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
            # NLP could help here to clarify ambiguous requests

# -------------------- SENTIMENT ANALYSIS FEATURE --------------------
# Function for sentiment analysis, word roles, and language detection

def sentiment_analysis(name):
    """Sentiment analysis chatbot with options for polarity, word roles, and language detection."""
    keep_running = True
    print(Fore.CYAN + f"\nNice to meet you {name}. How was your day?")
    mood = input(Fore.YELLOW + "Your mood: ").lower()

    # Respond to user's mood
    if mood == "good":
        print(Fore.GREEN + "\nGlad to know your day is going well!!\n")
    elif mood == "bad":
        print(Fore.RED + "\nSorry to hear that!\n")
    else:
        print(Fore.LIGHTMAGENTA_EX + "\nSometimes it's hard to put into words!\n")

    # Ask if user wants to proceed to sentiment analysis
    Boolean = input(Fore.CYAN + f"Should we proceed to Sentiment Analysis? (yes/no): ")
    if Boolean.lower() == 'no':
        print(Fore.CYAN + "\nAlright, have a great day ahead!!\n")
        return
    elif Boolean.lower() == 'yes':
        print(Fore.CYAN + "\nGreat! Let's proceed to Sentiment Analysis.\n")

        while keep_running:
            # Sentiment analysis options
            option = input(
                Fore.YELLOW +
                "What should we identify in the sentence:\n"
                "      1) Sentiment Polarity\n"
                "      2) Role of words in a sentence\n"
                "      3) Sentence Language Detection\n\n"
            )
            sentence = input(Fore.YELLOW + "Enter your sentence:\n")

            # Sentiment polarity detection
            if option == "1":
                pol = TextBlob(sentence).sentiment.polarity
                if pol > 0.25:
                    print(Fore.GREEN + "The sentence is Positive\n")
                elif pol < -0.25:
                    print(Fore.RED + "The sentence is Negative\n")
                else:
                    print(Fore.BLUE + "The sentence is Neutral\n")
            # Word role identification
            elif option == "2":
                sentence_tag = TextBlob(sentence)
                print(Fore.CYAN + "Word roles:")
                try:
                    for word, tag in sentence_tag.tags:
                        print(Fore.YELLOW + f"{word}: {tag}")
                except Exception as e:
                    print(Fore.RED + "Word role identification failed. Please enter a sentence in English with proper grammar.")
            # Language detection
            elif option == "3":
                try:
                    if sentence.strip() == "":
                        print(Fore.RED + "Please enter a non-empty sentence for language detection.")
                    elif len(sentence.strip().split()) < 5:
                        print(Fore.RED + "Please enter a longer, natural sentence in English for accurate language detection.")
                    else:
                        lang = detect(sentence)
                        print(Fore.GREEN + f"Detected language: {lang}\n")
                except Exception as e:
                    print(Fore.RED + f"Language detection failed: {e}")

            # Ask if user wants to analyze another sentence
            user_input = input(Fore.YELLOW + "\nDo You Want To Enter another Input? (yes/no): ")
            if user_input.lower() != 'yes':
                keep_running = False

        # Rating System after analysis loop ends
        rating = input(Fore.CYAN + "\nRATE US FROM 1-10: ")
        try:
            rating = int(rating)
        except ValueError:
            print(Fore.RED + "\nI didn't quite get that!! 😕\n")
        else:
            if rating in [1, 2, 3, 4]:
                print(Fore.RED + "\nWe will try to improve next time 😔\n")
            elif rating in [5, 6, 7]:
                print(Fore.YELLOW + "\nThank you! 😌\n")
            elif rating in [8, 9, 10]:
                print(Fore.GREEN + "\nThank you, it was an honour to serve you ☺️\n")
            else:
                print(Fore.RED + "\nI didn't quite get that!! 😕")
        print(Fore.CYAN + "\nHave a great day ahead!!\n")

# -------------------- ROCK PAPER SCISSORS FEATURE --------------------
# Function for Rock Paper Scissors game

def rps_chat():
    """Rock Paper Scissors game chatbot."""
    def user_choice():
        choices = ['rock', 'paper', 'scissors']
        choice = None
        while choice not in choices:
            choice = input(Fore.GREEN + "Choose Rock, Paper, or Scissors: ").lower()
        return choice

    def computer_choice():
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(user, computer):
        if user == computer:
            print(Fore.YELLOW + "It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print(Fore.YELLOW + "You win!")
        else:
            print(Fore.YELLOW + "Computer wins!")

    print(Fore.LIGHTMAGENTA_EX + "Welcome to Rock Paper Scissors!")
    name = input(Fore.LIGHTMAGENTA_EX + "What is your name?" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + f"Nice to meet you {name}! Let's play!\n\n\n")
    keep_running = True
    while keep_running:
        user = user_choice()
        computer = computer_choice()
        print(Fore.LIGHTRED_EX + f"You chose: {user}")
        print(Fore.LIGHTRED_EX + f"Computer chose: {computer}")
        determine_winner(user, computer)
        again = input(Fore.YELLOW + "Play again? (yes/no): ").strip().lower()
        if again != "yes":
            keep_running = False

# -------------------INFO SEARCH FEATURE --------------------
# Function for advanced info search (simulated search engine)

def info_search():
    """
    Advanced info search function that simulates a search engine.
    Matches user queries to travel, weather, news, time, or returns a fun fact.
    Loops until user types 'exit'.
    """
    fun_facts = [
        "The Eiffel Tower can be 15 cm taller during hot days.",
        "Honey never spoils. Archaeologists have found edible honey in ancient tombs.",
        "Bananas are berries, but strawberries are not.",
        "Octopuses have three hearts.",
        "The longest place name on the planet is 85 letters long."
    ]
    print(Fore.CYAN + "Welcome to Info Search! Type anything to search, or 'exit' to return to the menu.")
    keep_running = True
    while keep_running:
        query = input(Fore.YELLOW + "Search: ").strip().lower()
        if query == "exit":
            print(Fore.CYAN + "Exiting Info Search. Returning to main menu.")
            keep_running = False
            continue

        found = False
        # Destination search
        for category, places in destinations.items():
            if any(place.lower() in query for place in places) or category in query:
                print(Fore.GREEN + f"Popular {category.title()} destinations: {', '.join(places)}")
                found = True
                break

        # Weather search
        if not found and (any(city in query for city in weather_data.keys()) or "weather" in query):
            for city in weather_data:
                if city in query:
                    print(Fore.BLUE + f"Weather in {city.title()}: {weather_data[city]}")
                    found = True
                    break
            if not found:
                print(Fore.BLUE + "Please specify a city for weather info.")
                found = True

        # News search
        if not found and ("news" in query or "headline" in query or "update" in query):
            print(Fore.MAGENTA + "Latest travel news headlines:")
            for headline in news_headlines:
                print(Fore.MAGENTA + "- " + headline)
            found = True

        # Time search
        if not found and (any(city in query for city in city_timezones.keys()) or "time" in query):
            for city in city_timezones:
                if city in query:
                    utc_now = datetime.datetime.utcnow()
                    city_time = utc_now + datetime.timedelta(hours=city_timezones[city])
                    print(Fore.GREEN + f"Local time in {city.title()}: {city_time.strftime('%H:%M')}")
                    found = True
                    break
            if not found:
                print(Fore.GREEN + "Please specify a city for local time info.")
                found = True

        # Fun fact fallback
        if not found:
            print(Fore.LIGHTMAGENTA_EX + "Here's a fun fact:")
            print(Fore.LIGHTMAGENTA_EX + random.choice(fun_facts))

# -------------------- TICTACTOE FEATURE --------------------
# Function for TicTacToe game

def tictactoe():
    """Tic Tac Toe game chatbot."""
    def check_full(board):
        return all(not spot.isdigit() for spot in board)

    def display_board(board):
        print()
        def colored(cell):
            if cell == 'X':
                return Fore.RED + cell + Style.RESET_ALL
            elif cell == 'O':
                return Fore.BLUE + cell + Style.RESET_ALL
            else:
                return Fore.YELLOW + cell + Style.RESET_ALL
        print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
        print(Fore.CYAN + '-----------' + Style.RESET_ALL)
        print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
        print(Fore.CYAN + '-----------' + Style.RESET_ALL)
        print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
        print()

    def player_choice():
        symbol = ''
        while symbol not in ['X', 'O']:
            symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
        if symbol == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def player_move(board, symbol):
        move = -1
        while move not in range(1, 10) or not board[move - 1].isdigit():
            try:
                move = int(input("Enter your move (1-9): "))
                if move not in range(1, 10) or not board[move - 1].isdigit():
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        board[move - 1] = symbol

    def ai_move(board, ai_symbol, player_symbol):
        # Try to win or block player
        for i in range(9):
            if board[i].isdigit():
                board_copy = board.copy()
                board_copy[i] = ai_symbol
                if check_win(board_copy, ai_symbol):
                    board[i] = ai_symbol
                    return
        for i in range(9):
            if board[i].isdigit():
                board_copy = board.copy()
                board_copy[i] = player_symbol
                if check_win(board_copy, player_symbol):
                    board[i] = ai_symbol
                    return
        # Otherwise, pick random move
        possible_moves = [i for i in range(9) if board[i].isdigit()]
        move = random.choice(possible_moves)
        board[move] = ai_symbol

    def check_win(board, symbol):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),    # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),    # Vertical
            (0, 4, 8), (2, 4, 6)                # Diagonal
        ]
        for cond in win_conditions:
            if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
                return True
        return False

    def TicTacToe():
        print("Welcome to Tic Tac Toe!")
        input(Fore.GREEN + "What is your name?" + Style.RESET_ALL)

        while True:
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            player_symbol, ai_symbol = player_choice()
            turn = 'Player'
            game_on = True

            while game_on:
                display_board(board)
                if turn == 'Player':
                    player_move(board, player_symbol)
                    if check_win(board, player_symbol):
                        display_board(board)
                        print("Congratulations! You have won the game!")
                        game_on = False
                    else:
                        if check_full(board):
                            display_board(board)
                            print("The game is a draw!")
                            break
                        else:
                            turn = 'AI'
                else:
                    ai_move(board, ai_symbol, player_symbol)
                    if check_win(board, ai_symbol):
                        display_board(board)
                        print("AI has won! Better luck next time.")
                        game_on = False

                    else:
                        if check_full(board):
                            display_board(board)
                            print("It is a draw!")
                            break
                        else:
                            turn = 'Player'
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
    # Start the TicTacToe game loop
    TicTacToe()

# -------------------- MAIN MENU --------------------
# Main menu for selecting chatbot features

def main_menu():
    """Main menu for selecting chatbot features."""
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the Multi-Feature Chatbot!")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.CYAN + f"Hi {name}! What would you like to do today?")
    while True:
        # Display feature options
        print(Fore.MAGENTA + "\nOptions:")
        print(Fore.MAGENTA + "  1) TravelBot (recommendations, weather, news, time, history)")
        print(Fore.MAGENTA + "  2) Sentiment Analysis")
        print(Fore.MAGENTA + "  3) Rock Paper Scissors Game")
        print(Fore.MAGENTA + "  4) Info Search")
        print(Fore.MAGENTA + "  5) TictacToe Game")        
        print(Fore.MAGENTA + "  6) Exit")
        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4/5/6): ").strip()
        # Call the appropriate function based on user choice
        if choice == "1":
            chat()
        elif choice == "2":
            sentiment_analysis(name)
        elif choice == "3":
            rps_chat()
        elif choice == "4":
            info_search()
        elif choice == "5":
            tictactoe()
        elif choice == "6":
            print(Fore.CYAN + f"Goodbye {name}! Have a great day!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, 3, 4, 5 or 6.")

# -------------------- PROGRAM ENTRY POINT --------------------
# Start the chatbot program

if __name__ == "__main__":
    main_menu()

'''THANK YOU FOR USING YUAAN GPT!!!!'''