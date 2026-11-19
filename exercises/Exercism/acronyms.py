import string


def abbreviate(words):

    individual_word = words
    for punctuation in string.punctuation:
        if punctuation in words:
            if punctuation == "-":
                individual_word = individual_word.replace(punctuation, " ")
            else:
                individual_word = individual_word.replace(punctuation, "")

    individual_word = individual_word.split()
    abbreviated = []

    for word in individual_word:
        abbreviated.append(word[0])

    return "".join(abbreviated).upper()

print(abbreviate("Halley's Comet"))
