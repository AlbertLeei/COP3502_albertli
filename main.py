def encode():
    enc_pass = ""
    un_pass = input('Please enter your password to encode: ')
    for i in range(len(un_pass)):
        enc_pass += str(int(un_pass[i]) + 3)
    print('Your password has been encoded and stored!')
    return enc_pass


def main():
    choice = 1
    while choice != 3:
        # Menu
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:  # Encryption
            x = encode()
        if choice == 2:
            # decode(x)

if __name__ == "__main__":
    main()