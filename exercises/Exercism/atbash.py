
#input: string
#output: the reverse of the string alphabetically, abc = zyx

def decode(to_decode):
    return  encode(to_decode).replace(" ", "")

def encode(to_encode):

    to_encode = to_encode.strip().lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse = alphabet[::-1]
    atbash_string = []
    index = 0

    for char in to_encode:
        if char == " " or not char.isalnum():
            atbash_string.append("")
            continue
        if index % 5 == 0 and index != 0:
            atbash_string.append(" ")
        if char.isalpha():
            atbash_string.append(reverse[alphabet.index(char)])
        else:
            atbash_string.append(char)

        index += 1

    return "".join(atbash_string)

print(encode("Testing,1 2 3, testing."))