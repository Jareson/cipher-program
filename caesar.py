def encrypt(text, rot, type):
    encrypt_list = ["Encrypt", "encrypt"]
    if type in encrypt_list:
        from encrypt_aid import alphabet_position, rotate_character
        encryption = ""
        for char in text:
            char = rotate_character(char, rot)
            encryption += char
        return encryption
    elif type not in encrypt_list:
        from decrypt_aid import alphabet_position, rotate_character
        encryption = ""
        for char in text:
            char = rotate_character(char, rot)
            encryption += char
        return encryption

def main():
    from sys import argv, exit
    try:
        if argv[1].isdigit() == True:
            text = input("Type a message: ")
            rot = argv[1]
        else:
            print('usage: python caesar.py n\nArguments:\n'+'-'+'n : The integer to be used to encrypt your message. Should only contain integers-- no letters or special characters')
            text = input("Type a message: ")
            rot = input("Rotate by: ")
    except IndexError:
        #print('usage: python caesar.py n\nArguments:\n'+'-'+'n : The integer to be used to encrypt your message. Should only contain integers-- no letters or special characters')
        text = input("Type a message: ")
        rot = input("Rotate by: ")
    while rot.isdigit() == False:
        print('The integer to be used to encrypt your message should only contain integers-- no letters or special characters')
        rot = input("Rotate by: ")
    rot = int(rot)
    action_options = ["Encrypt", "encrypt", "Decrypt", "decrypt"]
    action = input("Encrypt or Decrypt? ")
    #if action not in action_options:
    while action not in action_options:
        print('Must either enter "decrypt" or "encrypt".')
        action = input("Encrypt or Decrypt? ")
        if action in action_options:
            break
    print(encrypt(text, rot, action))

if __name__ == "__main__":
    main()