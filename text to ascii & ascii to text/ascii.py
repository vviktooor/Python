from art import *

def main():
    tprint("ASCII TO TEXT  OR  TEXT TO ASCII", font='small')
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
    converted = []
    user_input = input("WRITE SOMETHING IN TEXT.TXT FILE AND TYPE OK:\n")
    filename = "ascii.txt"

    if user_input.lower() == "ok":
        with open(filename, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                list_of_inputs.append(i.split())


    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(chr(int(char)))
    with open('text.txt', 'w', encoding="utf-8") as f:
        for i in range(len(converted)):
            f.write(str(converted[i]))
def text_to_ascii():
    list_of_inputs = []
    converted = []
    user_input = input("WRITE SOMETHING IN TEXT.TXT FILE AND TYPE OK:\n")
    filename = "text.txt"

    if user_input.lower() == "ok":
        with open(filename, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                list_of_inputs.append(i)
    for i in range(len(list_of_inputs)):
        for char in list_of_inputs[i]:
            converted.append(ord(char))

    with open('ascii.txt', 'w') as f:
        for i in range(len(converted)):
            f.write(str(converted[i]) + " ")
if __name__ == '__main__':
    main()