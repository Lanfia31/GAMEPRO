import random

choices = ['pierre', 'feuille', 'ciseaux']
historique = []

def get_computer_choice():
    return random.choice(choices)


def get_user_choice():
    while True:
        user_choice = input("Pick between pierre, feuille, ciseaux : ")

        if user_choice in ['pierre', 'feuille', 'ciseaux']:
            return user_choice

        else:
            print("Invalid")

def arbitre(user_choice,computer_choice):
    if user_choice == computer_choice:
        result = "EQUAL"
        print("EQUAL!!!")


    elif user_choice == "pierre" and computer_choice == "ciseaux":
        result = "VICTORY"
        print("YOUPIII!")

    elif user_choice == "feuille".lower() and computer_choice == "pierre":
        result = "VICTORY"
        print("YOUPIII!")

    elif user_choice == "ciseaux" and computer_choice == "feuille":
        result = "VICTORY"
        print("YOUPIII!")

    else:
        result = "LOSS"
        print("LOSER :)")
    return result

def afficher_historique():
    if historique:
        print("\nHistorique des résultats :")
        for index, resultat in enumerate(historique, 1):
            print(f"Manche {index}: {resultat}")
    else:
        print("Aucun historique disponible.")

def game():
    print("READY? SET, MATCH!!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour Choice: {user_choice}")
    print(f"\nComputer Choice: {computer_choice}")
    
    result = arbitre(user_choice, computer_choice)
    historique.append(result)


while True:
    game()
    replay = input("\nAnother round ;) ? (yes/no): ")

    if replay == "yes":
        continue
    elif replay == "no":
        print("Bye Bye")
        afficher_historique()  
        break
    else:
        print("Invalid option, please retry.")
