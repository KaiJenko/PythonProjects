
def egg_count(display_value):

    #binary to decimal, decimal to E, return number of Es
    binary = []

    for x in range(display_value.bit_length(), -1, -1):
        if display_value >= 2**x:
            binary.append(1)
            display_value -= 2**x

    return len(binary)

print(egg_count(2000000000))