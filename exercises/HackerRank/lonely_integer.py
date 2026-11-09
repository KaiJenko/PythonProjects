import math
import os
import random
import re
import sys




def lonely_integer(a):

    # if not isinstance(a, list):
    #     raise TypeError("Input is not a list")
    #
    # lonely_dict = {}
    #
    # for number in a:
    #     if not number in lonely_dict:
    #         lonely_dict.update({number: 1})
    #     else:
    #         lonely_dict[number] += 1
    #
    # for number in lonely_dict:
    #     if lonely_dict[number] == 1:
    #         return number

    lonely_set = set()

    for number in a:
        if number not in lonely_set and (number + 1 not in a and number - 1 not in a):
            lonely_set.add(number)

        elif number in lonely_set:
            lonely_set.remove(number)
            continue


    return lonely_set


if __name__ == '__main__':

    print(lonely_integer([1,1,2,5,7,8]))