import string

def count_words(sentence):

    unique_words = {}

    for punctuation in string.punctuation:
        if punctuation == "'":
            continue
        sentence = sentence.replace(punctuation, " ").strip("'")


    for word in sentence.lower().split():
        word = word.strip("'")
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1

    return unique_words

print(count_words("'First: don't laugh. Then: don't cry. You're getting it.'"))