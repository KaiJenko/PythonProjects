from collections import Counter

def shoe_shop(num_shoes, shoe_sizes, customers, purchases):
    # if not (0 < num_shoes < 10 ** 3 or 0 < customers <= 10 ** 3):
    #     raise ValueError("Invalid Input used")
    #
    # total = 0
    # for purchase in purchases:
    #     if not 20 < purchase[1] < 100:
    #         raise TypeError("Invalid shoe price input")
    #     for size in shoe_sizes:
    #         if not 2 <= size < 20:
    #             raise ValueError("Invalid size input used")
    #
    #         if purchase[0] == size:
    #             shoe_sizes.remove(size)
    #             total += purchase[1]
    #             break
    #
    # return total


    total = 0
    shoe_counter = Counter(shoe_sizes)
    for purchase in purchases:
        if purchase[0] in shoe_counter and shoe_counter[purchase[0]] > 0:
            total += purchase[1]
            shoe_counter[purchase[0]] -= 1

    return total


print(shoe_shop(10, [2, 3, 4, 5, 6, 8, 7, 6, 5, 18], 6, [[6, 55], [6, 45], [6, 55], [4, 40], [18, 60], [10, 50]]))