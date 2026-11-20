from idlelib.editor import keynames


def score(word):

    scrabble_dict = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }

    scrabble_score = 0

    for char in word.upper():
        for amount, letter in scrabble_dict.items():
            if char in letter:
                scrabble_score += amount

    return scrabble_score

print(score("cabbage"))