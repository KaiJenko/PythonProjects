
def roman(number):

    numerals = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    total_numerals = []

    for numeral, amount in numerals.items():
        while number >= amount:
            total_numerals.append(numeral)
            number -= amount

    return "".join(total_numerals)


print(roman(5))