import random

choices = ['pierre', 'feuille', 'ciseau']
wins, losses, ties, total_games = 0,0,0,0

def get_computer_choice():
    return random.choice(choices)


def get_user_choice():
    while True:
        user_choice = input("Pick between pierre, feuille, ciseau: ")

        if user_choice in ['pierre', 'feuille', 'ciseau']:
            return user_choice
        
        else:
            print("Invalid")

def arbitre(user_choice,computer_choice):
    global wins, losses, ties
    if user_choice == computer_choice:
        print("EQUAL!!!")
        ties += 1
        return "Egalité"
    
    elif user_choice == "pierre" and computer_choice == "ciseaux":
        print("YOUPIII!")
        wins += 1
        return "Victoire"
    
    elif user_choice == "feuille" and computer_choice == "pierre":
        print("YOUPIII!")
        wins += 1
        return "Victoire"
    
    elif user_choice == "ciseaux" and computer_choice == "feuille":
        print("YOUPIII!")
        wins += 1
        return "Victoire"
    
    else:
        print("LOSER :)")
        losses += 1
        return "Défaite"


def display_statistics():
    global wins, losses, ties, total_games
   
    if total_games > 0:
        win_rate = (wins / total_games) * 100
        loss_rate = (losses / total_games) * 100
        tie_rate = (ties / total_games) * 100
        print("\n--- Statistics ---")
        print(f"Total games played: {total_games}")
        print(f"Win rate: {win_rate:.2f}%")
        print(f"Loss rate: {loss_rate:.2f}%")
        print(f"Draw rate: {tie_rate:.2f}%")
    else:
        print("No games played yet.")  

def game():
    global total_games
    print("READY? SET, MATCH!!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour Choice: {user_choice}")
    print(f"\nComputer Choice: {computer_choice}")

    result = arbitre(user_choice,computer_choice)
    total_games += 1

while True:
    game()
    replay = input("\nAnother round loser ;) ? ")

    if replay != "yes":
        print("Bayi :-( ")
        display_statistics()
        break