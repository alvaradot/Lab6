# Anastasia Lobanov
# Encode function

def encode(password):
    new = ""
    for element in password:
        new_element = int(element) + 3
        new_element = str(new_element)
        new += new_element[-1]
    print("Your password has been encoded and stored!\n")
    return new


# Thomas Alvarado
def decode(password):
    original = ""
    for i in password:
        if i == "0":
            original += "7"
        elif i == "1":
            original += "8"
        elif i == "2":
            original += "9"
        else:
            original += f"{int(i)-3}"
    print(f"The encoded password is {password}, and the original password is {original}\n")


def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"
    print(menu)
    option = int(input("Please enter an option: "))
    while option != 3:
        if option == 1:
            encoded_password = encode(input("Please enter your password to encode: "))
        elif option == 2:
            decode(encoded_password)
        print(menu)
        option = int(input("Please enter an option: "))


if __name__ == "__main__":
    main()