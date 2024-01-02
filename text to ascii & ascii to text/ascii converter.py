from art import *

def main():
    tprint("ASCII TO TEXT  ||  TEXT TO ASCII", font='small')
    print("PLEASE WRITE: \n 1 --> ASCII TO TEXT \n 2 --> TEXT TO ASCII \n")
    user_choice = int(input("YOUR CHOICE: \n"))

    if user_choice == 1:
        ascii_to_text()
    elif user_choice == 2:
        text_to_ascii()
    else:
        print("THIS OPTION NOT EXIST!")

def ascii_to_text():
    list_of_inputs = []
    user_input = input("WRITE ASCII TO TRANSLATE: \n")
    filename = "ascii.txt"
    for i in user_input:
        list_of_inputs.append((ord(i)))

    with open(filename, 'r+') as file:
        for i in list_of_inputs:
            file.write(str(i) + " ")
        print(f"{user_input} to {str(file.readlines())} w systemie ASCII")
def text_to_ascii():
    text = texteditor.open("This is the starting content")


if __name__ == '__main__':
    main()