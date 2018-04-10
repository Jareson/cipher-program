from encrypt_aid import alphabet_position, rotate_character

def encrypt(text, key):
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
    from sys import argv
    text = input("Type a message: ")
    key = argv[1]
    print(encrypt(text, key))

if __name__ == "__main__":
    main()