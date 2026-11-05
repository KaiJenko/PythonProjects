# If you know the person's name (e.g. if they're named Do-yun), then you will say:
# One for Kai, one for me.
# If you don't know the person's name, you will say you instead.
# One for you, one for me.
from idlelib.pyshell import use_subprocess


# def two_fer(name=""):
#
#     return f"One for {name}, one for me." if name != "" else "One for you, one for me."
#
# print(two_fer("kai"))


# def square_root(number):
#
#     return number ** 0.5
#
# print(square_root(5))

def is_paired(input_string):

    opened = "[{("
    closed = "]})"
    stack = []

    for char in input_string:
        if char in opened:
            stack.append(char)

        elif char in closed:
             if not stack or opened[closed.index(char)] != stack.pop():
                return False

    return not stack


print(is_paired(""))