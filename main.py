#Thomas Alvarado

def main():
    menu = "Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n"
    option = int(input(menu))
    while option != 3:
        if option == 1:
            encode(input("Please enter your password to encode: "))
        elif option == 2:
            decode()
        option = int(input(menu))
if __name__ == "__main__":
    main()