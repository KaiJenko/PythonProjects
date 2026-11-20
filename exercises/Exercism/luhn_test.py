import string


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        card_num = self.card_num
        if len(card_num.strip()) <= 1:
            raise ValueError("string length must be more than one")

        double = False
        validation = []
        reversed_string = card_num[::-1].replace(" ", "").strip()

        for punctuation in string.punctuation:
            reversed_string.replace(punctuation, "")

        for num in reversed_string:

            if not num.isdigit():
                return False

            num = int(num)

            if double:
                double = False
                if (num * 2) > 9:
                    validation.append((num * 2)- 9)
                else:
                    validation.append(num * 2)
            else:
                validation.append(num)
                double = True

        total = 0
        for num in validation:
            total += num

        if total % 10 == 0:
            return True
        return False


print(Luhn("055-444-285").valid())