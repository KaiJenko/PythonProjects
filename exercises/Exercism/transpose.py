def transpose(text):

    if "\n" in text:
        text = text.split("\n")

    largest_list = len(max(text, key=len))
    transposed_matrix = []
    matrix = []

    print(text, largest_list, len(text))
    for x in range(largest_list):
        for row in text:
            if x >= len(row):
                transposed_matrix.append(" ")
                continue
            transposed_matrix.append(row[x])
        matrix.append("".join(transposed_matrix).rstrip())
        print(matrix)
        transposed_matrix.clear()

    return "\n".join(matrix)


print(transpose("11\n2\n3333\n444\n555555\n66666"))






    # split = len(text) / 2
    # print(split)
    # first = text[:split]
    # second = text[split:]
    # print(split, first, second)
    # length = max(len(first), len(second))
    # transposed = []
    #
    # for x in range(length):
    #
    #     char1 = first[x] if x < len(first) else ""
    #     char2 = second[x] if x < len(second) else ""
    #
    #     transposed.append(char1 + char2 + "\n")
    #     print(transposed)
    #
    # return "".join(transposed)



