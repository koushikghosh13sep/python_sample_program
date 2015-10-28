import crypt
import os

def verify(Username, Password):

    with open('shadow', 'r') as infile:
        data = infile.read()

    my_list = data.splitlines()

    for lines in my_list:

        passList = str(lines).split(":")

        userName = passList[0]
        if (userName != Username):
            continue

        userPass = passList[1]

        encryptedPassList = str(userPass).split("$")
        encryptedType = encryptedPassList[1]
        passwordSalt = encryptedPassList[2]

        genPass = crypt.crypt(Password, "$"+encryptedType+"$"+passwordSalt+"$")

        if(genPass == userPass and userName == Username):
            return 1
        else:
            return 0
    
    return 0

if __name__ == "__main__":

    Username = raw_input("Username:")
    os.system("stty -echo")
    Password = raw_input("Password:")
    os.system("stty echo")

    if verify(Username, Password) == 1:
        print "\nvalid user"
    else:
        print "\ninvalid user"

