
def proverb(*inputs, qualifier=None):

    proverb_saying = []

    if not inputs:
        return []

    for index, word in enumerate(inputs):
        if index == len(inputs) - 1:
            continue
        proverb_saying.append(f"For want of a {word} the {inputs[index + 1]} was lost.")

    if qualifier:
        proverb_saying.append(f"And all for the want of a {qualifier} {inputs[0]}.")
    else:
        proverb_saying.append(f"And all for the want of a {inputs[0]}.")

    return proverb_saying

