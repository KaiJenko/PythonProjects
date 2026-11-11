

# def top_customers(transactions, k):
#
#     customers = {}
#
#     for transaction in transactions:
#         customer_id = transaction["customer_id"]
#         amount = transaction["amount"]
#         if customer_id not in customers:
#             customers[customer_id] = amount
#
#         else:
#             customers[customer_id] += amount
#
#     customers_sorted = sorted(customers.items(), key=lambda x: x[1], reverse=True)
#
#     return customers_sorted[:k]
#
# print(top_customers([
#     {"customer_id": "A", "amount": 50},
#     {"customer_id": "B", "amount": 100},
#     {"customer_id": "A", "amount": 75},
#     {"customer_id": "C", "amount": 200},
#     {"customer_id": "B", "amount": 25},
#     {"customer_id": "D", "amount": 90}
# ], 2))

# def sorted_products(products):
#     sorted_product = products.copy()
#     sorted_product.sort(key=lambda product: product["price"])
#     product_names = []
#     for product in sorted_product:
#         product_names.append(product["name"])
#
#     return product_names
#
#
# print(sorted_products([
#     {"name": "Laptop", "price": 900},
#     {"name": "Mouse", "price": 25},
#     {"name": "Keyboard", "price": 75},
#     {"name": "Monitor", "price": 250},
#     {"name": "Headphones", "price": 50}
# ]))


# def sort_frequency(numbers):
#
#     frequency = {}
#
#     for number in numbers:
#         if number not in frequency:
#             frequency[number] = 1
#
#         else:
#             frequency[number] += 1
#
#     ordered_frequency = sorted(frequency.items(), key=lambda x:x[1], reverse=True)
#
#     highest = []
#     for number in ordered_frequency:
#         for x in range(number[1]):
#             highest.append(number[0])
#
#     return highest
#
#
# print(sort_frequency([4, 2, 4, 3, 2, 4, 1, 3, 2]))


# def employees_salary(employees):
#
#     sorted_employees = employees.copy()
#     sorted_employees.sort(key= lambda employee: employee["salary"], reverse=True)
#
# print(employees_salary([
#     {"name": "James", "salary": 35000},
#     {"name": "Sarah", "salary": 45000},
#     {"name": "Tom", "salary": 28000},
#     {"name": "Emma", "salary": 55000},
#     {"name": "Alex", "salary": 40000}
# ]))

# def transaction_order(transactions):
#
#     copy_transactions = transactions.copy()
#     copy_transactions.sort(key=lambda transaction: transaction["amount"])
#     return copy_transactions
#
# print(transaction_order([
#     {"customer": "A", "amount": 50},
#     {"customer": "B", "amount": 100},
#     {"customer": "A", "amount": 150},
#     {"customer": "C", "amount": 75},
#     {"customer": "B", "amount": 25}
# ]))

def two_conditions(employees):

    return sorted(employees, key=lambda employee: (-employee["salary"], employee["name"]))

print(two_conditions([
    {"name": "James", "department": "IT", "salary": 40000},
    {"name": "Sarah", "department": "HR", "salary": 45000},
    {"name": "Tom", "department": "IT", "salary": 40000},
    {"name": "Emma", "department": "HR", "salary": 55000},
    {"name": "Alex", "department": "IT", "salary": 30000}
]))