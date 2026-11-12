
from collections import deque

#stack - LIFO - stack of plates - []
def reverse_stack(numbers):

    stack = []
    new_list = []

    for num in numbers:
        stack.append(num)

    for x in range(len(stack)):
        new_list.append(stack.pop())

    return new_list

print(reverse_stack([1, 2, 3, 4, 5]))

#queue - FIFO - queue of people - deque()

def process_queue(numbers):

    queue = deque()
    new_list = []

    for num in numbers:

        queue.append(num)

    for x in range(len(queue)):
        new_list.append(queue.popleft())

    return new_list

print(process_queue([1, 2, 3, 4, 5]))

def parenthesis(brackets):

    stack = []

    bracket_dict = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    for char in brackets:
        print(char, stack)
        if char in bracket_dict:
            stack.append(char)

        elif char in bracket_dict.values():
            opening = stack.pop()
            if bracket_dict[opening] == char:
                print(char)
                continue
            else:
                return False

        else:
            continue

    if not stack:
        return True

    else:
        return False

print(parenthesis("()[]{}"))



