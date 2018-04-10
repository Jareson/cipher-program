from encrypt_aid import alphabet_position, rotate_character

def encrypt(text, rot):
    encryption = ""
    for char in text:
        char = rotate_character(char, rot)
        encryption += char
    return encryption

def main():
    from sys import argv
    text = input("Type a message: ")
    rot = int(argv[1])
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()