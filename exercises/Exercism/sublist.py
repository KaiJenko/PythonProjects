
SUBLIST = "sublist"
SUPERLIST = "superlist"
EQUAL = "equal"
UNEQUAL = "unequal"


def sublist(list_one, list_two):

    if list_one == list_two:
        return EQUAL

    if not list_one:
        return SUBLIST

    if not list_two:
        return SUPERLIST

    for x in range(len(list_two)):
        if list_two[x:x + len(list_one)] == list_one:
            print(list_two[x:x + len(list_one)])
            return SUBLIST

    for x in range(len(list_one)):
        if list_one[x:x + len(list_two)] == list_two:
            print(list_one[x:x + len(list_two)])
            return SUPERLIST
    else:
        return UNEQUAL

print(sublist([1,2,5], [0, 1, 2, 3, 1, 2, 5, 6]))