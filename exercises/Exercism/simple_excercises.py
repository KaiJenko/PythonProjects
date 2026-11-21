

# If you know the person's name (e.g. if they're named Do-yun), then you will say:
# One for Kai, one for me.
# If you don't know the person's name, you will say you instead.
# One for you, one for me.

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

# def is_paired(input_string):
#
#     opened = "[{("
#     closed = "]})"
#     stack = []
#
#     for char in input_string:
#         if char in opened:
#             stack.append(char)
#
#         elif char in closed:
#              if not stack or opened[closed.index(char)] != stack.pop():
#                 return False
#
#     return not stack
#
#
# print(is_paired(""))


# def palindrome(a):
#     for index, char in enumerate(a):
#         print(char)
#         new_a = a[:index] + a[index+1:]
#         print(new_a)
#         if new_a == new_a[::-1]:
#             return True
#     return False
#
# print(palindrome("boob"))

# def bank_accounts(transactions):
#
#     if not isinstance(transactions, list):
#         raise TypeError("Input is not a list")
#
#     balance = {}
#
#     for record in transactions:
#
#         if not isinstance(record, tuple):
#             raise TypeError("record is not a tuple")
#
#         sender, receiver, amount = record
#
#         if amount <= 0:
#             raise ValueError("Amount is less than or equal to 0")
#
#         balance[sender] = balance.get(sender, 0) - amount
#         balance[receiver] = balance.get(receiver, 0) + amount
#
#     return balance
#
# def owed():
#     balances = bank_accounts([
#     ("alice", "bob", 50),
#     ("bob", "charlie", 30),
#     ("alice", "charlie", 20),
#     ("charlie", "alice", 10),
#     ("bob", "alice", 15)
# ])
#     debtor = []
#     creditor = []
#
#     for user in balances:
#         if balances[user] > 0:
#             creditor.append(balances[user])
#         else:
#             debtor.append(balances[user])
#
#
#
# print(bank_accounts([
#     ("alice", "bob", 50),
#     ("bob", "charlie", 30),
#     ("alice", "charlie", 20),
#     ("charlie", "alice", 10),
#     ("bob", "alice", 15)
# ]))

# input: list of integers
# output: integers which only appear once in list

# def lonely_integer(numbers):
#
#     if not isinstance(numbers, list):
#         raise TypeError("Input requires a list")
#
#     numbers_dict = {}
#     unique_numbers = []
#
#     for num in numbers:
#
#         if not isinstance(num, int):
#             raise ValueError("Individual input requires a integer")
#
#         if num not in numbers_dict:
#             numbers_dict[num] = 1
#
#         else:
#             numbers_dict[num] += 1
#
#     for num, count in numbers_dict.items():
#         if count == 1:
#             unique_numbers.append(num)
#
#     return unique_numbers
#
# print(lonely_integer([4,5,6,5,4]))

#input: string
#output: string of the first character to appear only once

# def first_unique(word):
#
#     word_dict = {}
#
#     for char in word:
#         if char not in word_dict:
#             word_dict[char] = 1
#
#         else:
#             word_dict[char] += 1
#
#     for char, count in word_dict.items():
#         if count == 1:
#             return char
#
# print(first_unique("swiss"))

#input: list of integers
#output: an integer which is missing

# def missing_number(numbers):
#
#     for index, num in enumerate(numbers):
#
#         if numbers[index + 1] != num + 1:
#             return num + 1
#
# print(missing_number([1,2,3,4,5,6,8]))

#input: list of integers
#output: integer which appears an odd amount of times

# def odd_number(numbers):
#
#     number_dict = {}
#
#     for num in numbers:
#         if num not in number_dict:
#             number_dict[num] = 1
#         else:
#             number_dict[num] += 1
#
#     for num, count in number_dict.items():
#         if count % 2 != 0:
#             return num
#
# print(odd_number([2, 3, 3, 4, 4, 4, 4, 2, 7]))

#input: two lists of integers
#output: numbers in common

# def common_numbers(list1, list2):
#
#
#     return set(list1) & set(list2)
#
# print(common_numbers([1,2,3,4,5], [3,4,5,6,7]))

#input: list of integers
#output: most frequent integer, if more than one the smaller

# def frequent_numbers(numbers):
#
#     number_dict = {}
#
#     for num in numbers:
#         if num not in number_dict:
#             number_dict[num] = 1
#         else:
#             number_dict[num] += 1
#
#     number = 0
#     old_count = 0
#
#     for num, count in number_dict.items():
#         if count > old_count:
#             number = num
#             old_count = count
#         elif count == old_count:
#             if number > num:
#                 number = num
#
#     return number
#
# print(frequent_numbers([2, 2, 4, 4, 5]))

#input: list of integers, and a target integer
#output: the index of two numbers that add up to target

def number_target(numbers, target):

    for i, num in enumerate(numbers):

        for j in range(i + 1, len(numbers)):

            if num + numbers[j] == target:
                return [i, j]

    return False

print(number_target([2,7,11,15], 22))

def rotate_list(numbers, rotation):


    if rotation > len(numbers):
        rotation = rotation % len(numbers)

    rotated = numbers[-rotation:] + numbers[:-rotation]   #  2: everything from index two on, -2 last two elements

    return rotated

print(rotate_list([1, 2, 3, 4, 5], 1))

#input: list of integers
#output: a list of numbers appearing more than once

# def repeat_numbers(numbers):
#
#     number_dict = {}
#     repeated = []
#
#     for num in numbers:
#         if num not in number_dict:
#             number_dict[num] = 1
#         else:
#             number_dict[num] += 1
#
#     for num, count in number_dict.items():
#         if count > 1:
#             repeated.append(num)
#
#     return repeated
#
# print(repeat_numbers([4, 4, 4, 2, 2, 7]))

#input: two lists of strings, purchased & registered
#output: list of products that have been purchased, but not registered

# def products(purchased, registered):
#
#     non_registered = []
#
#     for item in purchased:
#         if item not in registered:
#             non_registered.append(item)
#
#     return non_registered
#
# print(products(["Laptop", "Mouse", "Keyboard", "Monitor"], ["Laptop", "Monitor"]))

#input: list of integers, with all numbers occurring three times bar one
#output: integer which appears once

# def individual(numbers):
#
#     number_dict = {}
#
#     for num in numbers:
#         if num not in number_dict:
#             number_dict[num] = 1
#         else:
#             number_dict[num] += 1
#
#     for number, count in number_dict.items():
#         if count == 1:
#             return number
#
#     return None
#
# print(individual([0, 1, 0, 1, 0, 1, 99]))

#input: list of integers, rotation amount
#output: list that has been rotated
#constraints:

# def rotate_list(numbers, rotation):
#
#
#     if rotation > len(numbers):
#         rotation = rotation % len(numbers)
#
#     rotated = numbers[-rotation:] + numbers[:-rotation]   #  2: everything from index two on, -2 last two elements
#
#     return rotated
#
# print(rotate_list([1, 2, 3, 4, 5], 1))

#input; list of integers
#output: integer which appears only once
#only one element will appear once

# def lonely_integer(numbers):
#
#     count_numbers = {}
#
#     for num in numbers:
#         if num not in count_numbers:
#             count_numbers[num] = 1
#         else:
#             count_numbers[num] += 1
#
#     for number, count in count_numbers.items():
#         if count == 1:
#             return number
#
#     return None
#
# print(lonely_integer([1, 2, 3, 4, 3, 2, 1]))

#input: list of integers
#output: num which appears odd amount of times
#constraints: only one num, if no num, return none

def odd_integer(numbers):

    count_numbers = {}

    for num in numbers:
        if num not in count_numbers:
            count_numbers[num] = 1
        else:
            count_numbers[num] += 1

    for number, count in count_numbers.items():
        if count % 2 != 0:
            return number
    return None


print(odd_integer([4, 3, 4, 3, 4, 5, 5, 4]))



