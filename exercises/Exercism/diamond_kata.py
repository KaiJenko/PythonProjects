
#input: a letter, char
#output: a diamond shape based alphabetically, C =
# ····A····
# ···B·B···
# ··C···C··
# ·D·····D·
# E·······E
# ·D·····D·
# ··C···C··
# ···B·B···
# ····A····

def rows(letter):

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    target_index = alphabet.index(letter)
    array = []

    for x in range((target_index * 2) + 1):
        row = []

        for y in range((target_index * 2) + 1):
            if x <= target_index:
                if y == (target_index - x) or y == (target_index + x):
                    row.append(alphabet[x])
                else:
                    row.append(".")
            else:
                if y == (x - target_index) or y == ((target_index * 2) - (x - target_index)):
                    row.append(alphabet[target_index - (x - target_index)])
                else:
                    row.append(".")

        array.append("".join(row))
    return array

print(rows("E"))