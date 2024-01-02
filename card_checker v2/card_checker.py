from art import *

def visa(list_of_user, user_input):
    if len(user_input) == 16 or len(user_input) == 13:
        if list_of_user[0] == "4":
            print(f"Twoja karta o numerze: {user_input} to Visa")

            add_to_file("visa", user_input)
def mastercard(list_of_user, user_input):
    if len(user_input) == 16:
        if list_of_user[0:2] == ["5", "1"] or list_of_user[0:2] == ["5", "5"]:
            print(f"Twoja karta o numerze: {user_input} to Mastercard")

            add_to_file("mastercard", user_input)
        elif list_of_user[0:5] == ["2", "2", "2", "1"] or list_of_user[0:5] == ["2", "7", "2", "0"]:
            print(f"Twoja karta o numerze: {user_input} to Mastercard")
            add_to_file("mastercard", user_input)
def american_express(list_of_user, user_input):
    if len(user_input) == 15:
        if list_of_user[0:2] == ["3", "4"] or list_of_user[0:2] == ["3", "7"]:
            print(f"Twoja karta o numerze: {user_input} to American Express")

            add_to_file("american_express", user_input)
def add_to_file(card, user_input):
    filename = 0

    if card == "visa":
        filename = 'visa.txt'
        with open(filename, 'a') as visa:
            visa.write(user_input + '\n')

    elif card == "mastercard":
        filename = 'mastercard.txt'
        with open(filename, 'a') as mastercard:
            mastercard.write(user_input + '\n')

    elif card == "american_express":
        filename = 'american_express.txt'
        with open(filename, 'a') as american_express:
            american_express.write(user_input + '\n')

def main():
    tprint("CARD CHECKER", font='starwars')
    user_input = input("Proszę podać numer karty: \n")
    list_of_user = []

    for i in user_input:
        list_of_user.append(i)

    visa(list_of_user, user_input)
    mastercard(list_of_user, user_input)
    american_express(list_of_user, user_input)


if __name__ == '__main__':
    main()

# Visa ---> 4251256537686248
# Mastercard --> 5551256537686248
# American Express --> 375125653768624