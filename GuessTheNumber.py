# GUESS THE NUMBER

actual_number = 45
attempts = 0

while True:
    attempts = attempts + 1
    guess = int(input("guess the no. "))
    if guess < actual_number:
        print("too low guess")
    elif guess > actual_number:
        print("too high guess")
    else:
        print("!!! you solved it !!!")
            