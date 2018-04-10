alphabet_digit = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
def alphabet_position(letter):
    letter = letter.lower()
    digit = alphabet_digit[letter]
    return digit

def rotate_character(char, rot):
    if char.isalpha() == True:
        char_digit = alphabet_position(char)
        rotated = char_digit - rot
        if rotated < 25:
            rotated = rotated % 26
            for l, d in alphabet_digit.items():
                if d == rotated:
                    if char.isupper() == True:
                        l = l.upper()
                        return l
                    else:
                        return l
        else:
            for l, d in alphabet_digit.items():
                if d == rotated:
                    if char.isupper() == True:
                        l = l.upper()
                        return l
                    else:
                        return l
    else:
        return char