import heapq



#heapq.heapify() turn list into heap, heappop() remove smallest value and return, heappush() - adds a number

# numbers = [12, 5, 20, 3, 9]
# heapq.heapify(numbers)
# smallest = heapq.heappop(numbers)
# print(smallest)

# def process_numbers(numbers):
#
#     heapq.heapify(numbers)
#     heapq.heappush(numbers, 4)
#     smallest = []
#     for x in range(2):
#         smallest.append(heapq.heappop(numbers))
#     return smallest
#
# print(process_numbers([10, 5, 8, 2]))

# def smallest_number(numbers, k):
#
#     heapq.heapify(numbers)
#
#     smallest = []
#
#     for x in range(k):
#         smallest.append(heapq.heappop(numbers))
#
#     return smallest
#
#
# print(smallest_number([15, 3, 8, 20, 1, 12, 5, 7], 3))

# def largest_number(numbers, k):
#
#     heapq.heapify_max(numbers)
#     largest = []
#
#     for x in range(k):
#         largest.append(heapq.heappop_max(numbers))
#
#     return largest
#
# print(largest_number([15, 3, 8, 20, 1, 12, 5, 7], 3))


def customers(transactions):

    sorted_transactions = transactions.copy()
    sorted_transactions.sort(key= lambda transaction: transaction["amount"])

    highest_spenders = []

    heapq.heapify_max(sorted_transactions)

    for x in range(2):
        highest_spenders.append(heapq.heappop_max(sorted_transactions))

print(customers([
    {"customer": "A", "amount": 50},
    {"customer": "B", "amount": 100},
    {"customer": "A", "amount": 150},
    {"customer": "C", "amount": 75},
    {"customer": "B", "amount": 25},
    {"customer": "D", "amount": 200}
]))