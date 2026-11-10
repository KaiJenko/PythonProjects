# If you know the person's name (e.g. if they're named Do-yun), then you will say:
# One for Kai, one for me.
# If you don't know the person's name, you will say you instead.
# One for you, one for me.
from idlelib.pyshell import use_subprocess

from exercises.bug_hunts.bug_hunt_2 import total
from exercises.bug_hunts.bug_hunt_4 import print_display_names


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



