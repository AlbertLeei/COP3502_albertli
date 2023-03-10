def decode(encoded):
    decoded_str = ""
    for i in encoded:
        if int(i) < 3:
            num = int(i) + 7
            decoded_str += str(num)
        else:
            num = int(i) - 3
            decoded_str += str(num)
    return decoded_str


def encode():
    enc_pass = ""
    un_pass = input('Please enter your password to encode: ')
    for i in range(len(un_pass)):
        enc_pass += str(int(un_pass[i]) + 3)
    print('Your password has been encoded and stored!')
    return enc_pass


def main(): # hello
    choice = 1
    while choice != 3:
        # Menu
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:  # Encryption
            x = encode()
        if choice == 2:
            print(f'The encoded password is {x}, and the decoded password is {decode(x)}')


if __name__ == "__main__":
    main()