def encode():
    enc_pass = ""
    un_pass = input('Please enter your password to encode: ')
    for i in range(len(un_pass)):
        enc_pass += str(int(un_pass[i]) + 3)
    print('Your password has been encoded and stored!')
    return enc_pass


def main():
    # Menu
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
    choice = int(input("Please enter an option: "))

    if choice == 1:  # Encryption
        encode()


if __name__ == "__main__":
    main()