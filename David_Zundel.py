# David Zundel
def encode(password1):
    new_password = ""
    for char in password1:
        res = int(char) + 3
        if res > 9:
            res -= 10
        new_password += str(res)
    return new_password

#Aiden Blackwood
def decode(password):
    decoded_password = ""
    for char in password:
        res = int(char) - 3
        if res < 0:
            res += 10
        decoded_password += str(res)
    return decoded_password

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
        decoded_pass = decode(password)
        print(f"The encoded password is {password}, and the original password is {decoded_pass}.\n")
    else:
        break

