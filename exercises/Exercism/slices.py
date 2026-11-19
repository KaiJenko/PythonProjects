
def slices(series, length):

    digit_series = []

    if length > len(series):
        raise ValueError("Length cannot be longer than the digit series")

    for x in range(0, (len(series) - length) + 1):
        digit_series.append(series[x:x + length])

    return digit_series


print(slices("49142", 3))