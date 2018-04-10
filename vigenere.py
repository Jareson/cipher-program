def encrypt(text, key, type):
    encrypt_list = ["Encrypt", "encrypt"]
    if type in encrypt_list:
        from encrypt_aid import alphabet_position, rotate_character
        encryption = ""
        key_list = []
        list_pos = 0
        for i in key:
            digit = alphabet_position(i)
            key_list.append(digit)
        for char in text:
            char = rotate_character(char, key_list[list_pos])
            if char.isalpha() == True:
                if list_pos < len(key_list)-1:
                    list_pos += 1
                else:
                    list_pos = 0
            encryption += char
        return encryption
    if type not in encrypt_list:
        from decrypt_aid import alphabet_position, rotate_character
        encryption = ""
        key_list = []
        list_pos = 0
        for i in key:
            digit = alphabet_position(i)
            key_list.append(digit)
        for char in text:
            char = rotate_character(char, key_list[list_pos])
            if char.isalpha() == True:
                if list_pos < len(key_list)-1:
                    list_pos += 1
                else:
                    list_pos = 0
            encryption += char
        return encryption

def main():
    from sys import argv, exit
    try:
        if argv[1].isalpha() == True:
            text = input("Type a message: ")
            key = argv[1]
        else:
            print('usage: python caesar.py keyword\nArguments:\n'+'-'+'keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.')
            text = input("Type a message: ")
            key = input("Encryption key: ")
    except IndexError:
        #print('usage: python caesar.py keyword\nArguments:\n'+'-'+'keyword : The string to be used as a "key" to encrypt your message. Should only contain alphabetic characters-- no numbers or special characters.')
        text = input("Type a message: ")
        key = input("Encryption key: ")
    while key.isalpha() == False:
        print('The string to be used as a "key" to encrypt your message should only contain alphabetic characters-- no numbers or special characters.')
        key = input("Encryption key: ")
    action_options = ["Encrypt", "encrypt", "Decrypt", "decrypt"]
    action = input("Encrypt or Decrypt? ")
    #if action not in action_options:
    while action not in action_options:
        print('Must either enter "decrypt" or "encrypt".')
        action = input("Encrypt or Decrypt? ")
        if action in action_options:
            break
    print(encrypt(text, key, action))
            


if __name__ == "__main__":
    main()