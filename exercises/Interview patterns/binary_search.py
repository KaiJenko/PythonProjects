


# def binary_search(numbers, target):
#
#     left = 0
#     right = len(numbers) - 1
#
#     while left <= right:
#
#         middle = (left + right) // 2
#
#         print(numbers, left, middle, right)
#
#         if numbers[middle] == target:
#             return middle
#
#         elif target < numbers[middle]:
#             right = middle - 1
#
#         elif target > numbers[middle]:
#             left = middle + 1
#
#         else:
#             return middle
#
# print(binary_search([2, 5, 8, 12, 16, 23, 38, 45, 57], 23))

def insertion_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif target < numbers[middle]:
            right = middle - 1

        else:
            left = middle + 1

    return left



print(insertion_search([1, 3, 5, 7, 9], 6))