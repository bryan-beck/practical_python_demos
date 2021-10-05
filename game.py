# import random

# name = input('hello, whats your name?')
# print(name, "I'm thinking of a number between 1 and 100."
# "try to guess my number")
# guess = input(random.randint (1, 100))
# while True
#     response = input()
#     if response == 13:
#         return ('well done, jessica! you found my number!')

# i need to do the infinite loop and the if else statements
import random
name = input('Greetings, what is your name?')
def number_guessing_game(low, high):
    print("Guess a number between {low} and {high}. Good luck to you.".format(low=low, high=high))
    number = random.randint(low, high)
    

    while True:
        guess = input("Enter an integer: ")

        try:
            integer = int(guess)
            if integer == number:
                print('Congratulations you have won!!!')
                return
            elif integer < number:
                print('Try Higher')
            elif integer > number:
                print('Try Lower')

        except ValueError:
            print("You must enter a valid integer.")



number_guessing_game(1, 100)