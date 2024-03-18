# David Zundel
def encode(password1):
    new_password = ""
    for char in password1:
        new_password += str(int(char)+3)
    return new_password


password = ""
cont = True
while cont:
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
    option = int(input("Please enter an option: "))
    if option == 1:
        temporary = input("Please enter your password to encode: ")
        password = encode(temporary)
        print("Your password has been encoded and stored!\n")
    elif option == 2:
        pass
        # decoded_pass = decode(password)
        # print(f"The encoded password is {password}, and the original password is {decoded_pass}.\n")
    else:
        break

