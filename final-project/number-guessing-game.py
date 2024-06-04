import random

def number_guessing_game():
    target_number = random.randint(1, 20)

    chances_left = 5

    while chances_left > 0:
        try:
          user_guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
          print("Invalid input. Please enter numeric values.")
          input("Press Enter to continue...")
          continue

        chances_left -= 1

        if user_guess > target_number:
            print("{0} is higher than the target number.".format(user_guess))
            print("{0} chances left.".format(chances_left))
        elif user_guess < target_number:
            print("{0} is lower than the target number.".format(user_guess))
            print("{0} chances left.".format(chances_left))
        else:
            print("You won with {0} guess.".format(5 - chances_left))
            return

    print("You didn't guess {0} correctly. Better luck next time!".format(target_number))

number_guessing_game()