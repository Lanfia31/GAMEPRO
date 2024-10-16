import random

choices = ['pierre', 'feuille', 'ciseau']

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
    if user_choice == computer_choice:
        print("EQUAL!!!")
    
    elif user_choice == "pierre" and computer_choice == "ciseaux":
        print("YOUPIII!")
    
    elif user_choice == "feuille" and computer_choice == "pierre":
        print("YOUPIII!")
    
    elif user_choice == "ciseaux" and computer_choice == "feuille":
        print("YOUPIII!")
    
    else:
        print("LOSER :)")
    

def game():
    print("READY? SET, MATCH!!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour Choice: {user_choice}")
    print(f"\nComputer Choice: {computer_choice}")

    result = arbitre(user_choice,computer_choice)

while True:
    game()
    replay = input("\nAnother round loser ;) ? ")

    if replay != "yes":
        print("Bayi :-( ")
        break