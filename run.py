# import section
import random  # generates random numbers
import string  # module for string (ascii, emojis) manipulation
import sys
from time import sleep  # time delay for print statements
import os
from words import *
from intro import *
from six_scoops import *
from colorama import Fore, Style, init

init(autoreset=True)  # sets text to its default values


alphabet = set(string.ascii_uppercase)  # stores letters A-Z
scoops = 6  # number ice cream scoops that can be lost


def choose_level(level):
    """ Chooses level based on user input """
    if level == "1":
        print(
            f"{Fore.LIGHTBLUE_EX}Easy:{Fore.RESET} " +
            "Get your 🍦 easily cause it is 🔥.\n"
        )
        return "easy"
    elif level == "2":
        print(
            f"{Fore.LIGHTYELLOW_EX}Medium:{Fore.RESET} Get " +
            "your 🍦 smartly cause it is 🔥.\n"
        )
        return "medium"
    elif level == "3":
        print(
            f"{Fore.LIGHTRED_EX}Hard:{Fore.RESET} Strain " +
            "your brain to get 🍦 cause it is 🔥.\n"
        )
        return "hard"
    elif level == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


def validate_level(value):
    """
    Checks if user input for level choice equals
    1, 2, 3 or 4 for back
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"
        and (value != "4")):
            raise ValueError(
                f"Please only enter 1, 2, 3 or 4. You typed "
                f"{Style.BRIGHT}{Fore.YELLOW}{value}{Fore.RESET}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data:{Fore.RESET} {e}," +
            " please try again.")
        return False
    return True


def user_level():
    """ Gets user level value and generates word list accordingly """
    while True:
        input_text = f"""
        {Fore.GREEN}Choose your level by typing 1, 2, 3 or 4 to go back:

        1. Easy
        2. Medium
        3. Hard
        4. Back
        {Fore.RESET}

        """
        chosen_level = input(input_text)
        level = choose_level(chosen_level)

        if validate_level(chosen_level):
            select_words(words, level)
            break
    word_list = select_words(words, level)
    return word_list


def select_words(words, level):
    """
    Selects words by length and gathers into three lists
    depending on user level choice
    """

    if level == "easy":
        easy = [word for word in words if len(word) == 3]
        return easy
    elif level == "medium":
        medium = [word for word in words if len(word) == 4]
        return medium
    elif level == "hard":
        hard = [word for word in words if len(word) == 5]
        return hard


def get_word(words):
    """
    Chooses randomly a word from the chosen words list
    and returns it in uppercase
    """
    word = random.choice(words)
    return word.upper()


def users_letter():
    """
    Asks a user to type a letter and checks
    if it is in the word
    """
    while True:
        guess = input("Please guess a letter:\n").upper()
        if validate_letter(guess):
            break
    return guess


def validate_letter(letter):
    """ Validates user input if letter is in alphabet """
    try:
        if letter not in alphabet:
            raise ValueError(
                f"Please enter a single letter from A to Z. "
                f"You typed {Style.BRIGHT}{Fore.YELLOW}{letter}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data:{Fore.RESET} {e}.\n")
        return False
    return True


def start_game():
    """
    Runs and updates game development, provides
    feedback to the user until the game is over.
    """
    # variables
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # stores letters guessed by user
    global scoops
    print("Let's play!")
    # prints a scoops numberand displays the word to guess
    print(display_scoops(scoops))
    print(
        f"""
        Guess this word: {Fore.LIGHTBLUE_EX}{word_completion}
        
        """
    )
    # handles the users input
    while not guessed and scoops > 0:
        guess = users_letter()
        print(
            f"You've guessed these letters so far: "
            f"{Style.BRIGHT}{Fore.YELLOW}{' '.join(guessed_letters)}\n"
        )
        # checks if a letter has already been guessed or belongs to word
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(
                    f"❌ Sorry, you've already guessed this one. "
                    f"Try a different letter!"
                )
            elif guess not in word:
                scoops_number()
                guessed_letters.append(guess)
            else:
                print("Good job!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        else:
            print(f"{Fore.RED}It is not a valid guess.")
        print(display_scoops(scoops))
        print(
            f"""
            {Fore.LIGHTBLUE_EX}{word_completion}

            """
        )
    # shows the end of the game: user wins or loses
    if guessed:
        print("Congrats, you guessed the word! 😎 You win!")
    else:
        print(f"Sorry, your cane is empty 😢. Game is over!")
        print(f"The word was ➡️  {Style.BRIGHT}{word}.")


def scoops_number():
    """ Decrements scoops for each wrong guess """
    global scoops
    scoops -= 1
    print(
        f"❌ Wrong letter! "
        f"You have {Style.BRIGHT}{Fore.YELLOW}{scoops}{Style.RESET_ALL}"
        f" scoops of 🍦 left."
        )


def game_rules():
    """
    Function to ask the player if he wants
    to read the game rules
    """
    while True:
        print(
            f"Do you want to read the game "
            f"{Style.BRIGHT}{Fore.YELLOW}rules? (Y/N)"
        )
        answer = input().upper().strip()
        if answer == "Y":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(RULES_PART_1)
            sleep(1)
            print(RULES_PART_2)
            sleep(1)
            print(RULES_PART_3)
            sleep(2)
            print(RULES_PART_4)
            sleep(2)
            print(RULES_PART_5)
            sleep(1)
            print(RULES_PART_6)
            sleep(1)
            return True
        elif answer == "N":
            # Clears the terminal
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Let's get started!\n")
            return False
        else:
            print(
                f"{Fore.RED}Invalid choice:{Style.RESET_ALL}"
                f" please enter 'Y' or 'N'."
            )


def run_intro():
    """ Displays logo and welcoming message """
    print(f"{Style.BRIGHT}{Fore.RED}{LOGO}")
    typewriter("Welcome!")
    sleep(1)
    typewriter(
        f"Here you can get the Extra Large treat "
        f"with Six Scoops of Ice Cream.\n"
    )
    typewriter("🍦🍦🍦🍦🍦🍦")
    sleep(1)
    typewriter("Oh, it is not that easy. But yummy! 🤤")
    sleep(0.5)
    typewriter(
        f"Here are the rules on how to get your "
        f"Extra Large treat!\n"
    )


def typewriter(text, color=Fore.WHITE):
    """ Function to add a typewriter effect to print statements """
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        sleep(.02)
    print()


def restart_game():
    """ Asks player if he wants to play again """
    global scoops, word
    scoops = 6  # reset scoops to 6
    
    while True:
        print(
            f"Do you want to play "
            f"{Style.BRIGHT}{Fore.YELLOW}again? (Y/N)"
        )
        choice = input().upper().strip()
        # Starts the game from choosing the level
        if choice == "Y":
            word_list = user_level()
            word = get_word(word_list)
            start_game()
            restart_game()
            return True
        elif choice == "N":
            print("Bye! Hope, you did like the 🍦 game!")
            return False
        else:
            print(
                f"{Fore.RED}Invalid choice:{Style.RESET_ALL}"
                f" please enter 'Y' or 'N'."
            )


def main():
    """ Runs entire application """
    global word_list, word
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    run_intro()
    game_rules()
    word_list = user_level()
    word = get_word(word_list)
    start_game()
    restart_game()


if __name__ == "__main__":
    main()
