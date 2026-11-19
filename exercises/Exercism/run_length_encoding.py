
def decode(string):

    if string == "":
        return ""

    amount = []
    decoded_value = []

    for char in string:

        if char.isdigit():
            amount.append(char)

        elif not amount:
            decoded_value.append(char)

        elif isinstance(char, str):
            joined_amount = int("".join(amount))
            for x in range(joined_amount):
                decoded_value.append(char)
                amount.clear()

    return "".join(decoded_value)


def encode(string):

    if string == "":
        return ""

    previous_char = string[0]
    encoded_value = []
    count = 0

    for char in string:
        print(previous_char, char, count)
        if char == previous_char:
            count += 1

        else:
            if count == 1:
                encoded_value.append(previous_char)
            else:
                encoded_value.append(str(count))
                encoded_value.append(previous_char)
            previous_char = char
            count = 1

    if count != 1:
        encoded_value.append(str(count))
    encoded_value.append(previous_char)

    return "".join(encoded_value)

print(encode("AABBBCCCC"))
print(decode("12WB12W3B24WB"))