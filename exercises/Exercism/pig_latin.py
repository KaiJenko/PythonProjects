#Practicing slicing

def translate(text):

    ay_words = ["a", "e", "i", "o", "u", "xr", "yt"]
    text = text.lower()

    individual_words = text.split()
    translated = []

    for word in individual_words:
        #check for beginning with a vowel or matching "xr"/"yt"
        if word[0] in ay_words or word[0:2] in ay_words:
            translated.append(word + "ay")

        else:
            for index, char in enumerate(word):
                #check for qu
                if char == "q" and word[index:index + 2] == "qu":
                    translated.append(word[index + 2:] + word[:index + 2] + "ay")
                    break
                else:
                    #check for consonants or y
                    if char in ay_words or (char == "y" and index != 0):
                        translated.append(word[index:] + word[:index] + "ay")
                        break

    return " ".join(translated)


print(translate("quick fast run"))


#top community solution, insane use of advanced regex.

# RE = re.compile('^(x(?!r)|y(?!t)|[^aeiouqxy]*(?:qu?)?)(.+)$')


