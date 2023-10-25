#Thomas Alvarado
def decode(password):
    original = ""
    for i in password:
        if i == 0:
            original += "7"
        elif i == 1:
            original += "8"
        elif i == 2:
            original += "9"
        else:
            original += f"{int(i)-3}"
    print(f"The encoded password is {password}, and the original password is {original}")

def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"
    option = int(input(menu))
    while option != 3:
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
        elif option == 2:
            decode(encoded_password)
        option = int(input(menu))
if __name__ == "__main__":
    main()
