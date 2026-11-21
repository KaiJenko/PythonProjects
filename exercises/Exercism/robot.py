import random
import string



class Robot:

    used_names = set()

    def __init__(self):
        self.name = self.generate_name()

    def generate_name(self):

        characters = []
        digits = []

        characters.append("".join(random.choices(string.ascii_uppercase, k=2)))
        digits.append("".join(random.choices(string.digits, k=3)))
        name = "".join(characters + digits)

        if name in Robot.used_names:
            self.generate_name()

        Robot.used_names.add(name)
        return name

    def reset(self):
        Robot.used_names.remove(self.name)

Robot1 = Robot()
print(Robot1.name)
print(Robot.used_names)
