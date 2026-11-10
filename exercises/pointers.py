
# def target_pair(numbers, target):
#
#     start = 0
#     end = len(numbers) - 1
#
#     while (numbers[start] < numbers[end]) != target:
#
#         if start == end:
#             return "No pair found"
#
#         if (numbers[start] + numbers[end]) > target:
#             end -= 1
#
#         elif (numbers[start] + numbers[end]) < target:
#             start += 1
#
#     return [numbers[start], numbers[end]]
#
# print(target_pair([1, 2, 4, 6, 8, 9, 12], 10))


# def duplicates(numbers):
#
#     start = 0
#     next = 1
#
#     while next < len(numbers):
#         print(numbers[start], numbers[next])
#         if numbers[start] == numbers[next]:
#             next += 1
#
#         else:
#             numbers[start+1] = numbers[next]
#             start += 1
#             next += 1
#
#
#     return len(numbers[:start + 1])
#
# print(duplicates([1, 1, 1, 1]))

# def palindrome(query):
#
#     trim_query = query.replace(" ", "").lower()
#
#     start = 0
#     end = len(trim_query) - 1
#
#     while start < end:
#         if trim_query[start] == trim_query[end]:
#             start += 1
#             end -= 1
#         else:
#             return False
#
#     return True
#
# print(palindrome("he llo"))

def sorted_list(list1, list2):

    pointer_1 = 0
    pointer_2 = 0
    list3 = []

    while pointer_1  < len(list1) and pointer_2 < len(list2):

        if list1[pointer_1] < list2[pointer_2]:
            list3.append(list1[pointer_1])
            pointer_1 += 1
        else:
            list3.append(list2[pointer_2])
            pointer_2 += 1

    list3.extend(list1[pointer_1:])
    list3.extend(list2[pointer_2:])

    return list3

print(sorted_list([1, 4, 7, 9], [2, 3, 5, 8, 10]))