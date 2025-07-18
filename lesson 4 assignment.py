from random import randrange

def menu():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Choose your weapon (1-3): ")
    #the try block will run the code inside it if there are no errors otherwise it will not run.
    try:
        choice = int(choice)
        if choice < 1 or choice > 3:
            print("Invalid choice. Please try again.")
            return menu()
        #except value error will deal with non-integer inputs and return the prompt to put in a number
    except ValueError:
        print("Invalid input. Please enter a number.")
        return menu()
    return choice

def play():
    player_choice = menu()
    computer_choice = randrange(1, 4)  
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 1 and computer_choice == 3):
        print("Rock beats scissors. You win!")
    elif (player_choice == 2 and computer_choice == 1):
        print("Paper beats rock. You win!")
    elif (player_choice == 3 and computer_choice == 2):
        print("Scissors beats paper. You win!")
    else:
        if (computer_choice == 1 and player_choice == 3):
            print("Rock beats scissors. Computer wins!")
        elif (computer_choice == 2 and player_choice == 1):
            print("Paper beats rock. Computer wins!")
        elif (computer_choice == 3 and player_choice == 2):
            print("Scissors beats paper. Computer wins!")

    replay = input("Play again? (y/n): ")
    if replay == 'y':
        play()
    else:
        print("Thanks for playing!")
        print("Completed by, John Benites")

if __name__ == "__main__":
    play()