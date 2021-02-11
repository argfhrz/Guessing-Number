import random
countAttempts = []
def disp_score():
    if len(countAttempts) <= 0:
        print("There is no high score yet!")
    else:
        print("High score is {} attempts".format(min(countAttempts)))
def start_game():
    print("Let's Start The Game !!")
    randomNumber = int(random.randint(1,1000))
    print(randomNumber)
    playerName = input("Please Input Name: ")
    checkReady = input("{}, Are you ready? (yes/no) ".format(playerName))
    attempts = 0
    after = 1
    disp_score()
    while checkReady == 'yes':
        if randomNumber%2 == 0 and after == 1:
            print("First Clue 'number' are even ")
            after = 0
        elif randomNumber%2 != 0 and after == 1:
            print("First Clue 'number' are odd ")
            after = 0
        try:
            guessNumber = input("Pick a number between 1 to 1000: ")
            midNumber = abs((randomNumber - int(guessNumber)))
            if midNumber >10 and midNumber < 100:
                print("Almost there")
                if randomNumber%3 == 0:
                    print("Last Clue. It can be divided by 3")
                    attempts += 1
                elif randomNumber%5 == 0:
                    print("Last Clue. It can be divided by 5")
                    attempts += 1
                elif randomNumber%7 == 0:
                    print("Last Clue. It can be divided by 7")
                    attempts += 1
            elif midNumber >=100 and midNumber <200 :
                print("You far away, Try to + 100 or - 100 ")
                attempts += 1
            elif midNumber >=200:
                print("That's too far, Try to + 200 or - 200 ")
                attempts += 1
            elif midNumber >=1 and midNumber<=10:
                print("Really Close")
                if int(guessNumber) > randomNumber:
                    print("Try lower")
                    attempts += 1
                else:
                    print("Try higher")
                    attempts += 1
            #number not in range
            if int(guessNumber) < 1 or int(guessNumber) > 1000:
                raise ValueError("Please guess a number within the given range")
            #logic
            if int(guessNumber) == randomNumber:
                print("OMG! You Are Awesome")
                attempts += 1
                countAttempts.append(attempts)
                print("It took you {} attempts".format(attempts))
                playAgain = input("Would you like to play again? (yes/no) ")
                attempts = 0
                disp_score()
                randomNumber = int(random.randint(1, 1000))
                print(randomNumber)
                if playAgain == "no":
                    print("Bye, Have a nice day !")
                    break
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("Bye, Have a nice day !")
if __name__ == '__main__':
    start_game()
