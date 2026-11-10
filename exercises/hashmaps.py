# def unique_cities(deliveries):
#
#     driver_cities = {}
#     multiple_cities = []
#
#     for delivery in deliveries:
#         driver_id = delivery["driver_id"]
#         city = delivery["city"]
#
#         if driver_id not in driver_cities:
#             driver_cities[driver_id] = set()
#
#         driver_cities[driver_id].add(city)
#
#     for driver in driver_cities:
#         if len(driver_cities[driver]) > 1:
#             multiple_cities.append(driver)
#
#     return multiple_cities
#
#
#
#
# print(unique_cities([
#     {"driver_id": "D1", "city": "London"},
#     {"driver_id": "D2", "city": "Manchester"},
#     {"driver_id": "D1", "city": "Birmingham"},
#     {"driver_id": "D2", "city": "Manchester"},
#     {"driver_id": "D3", "city": "Leeds"},
#     {"driver_id": "D1", "city": "London"},
#     {"driver_id": "D3", "city": "Leeds"}
# ]))
from exercises.bug_hunts.bug_hunt_4 import print_display_names


# def purchasing(transactions):
#
#     customer_purchases = {}
#     vip_customer = {}
#
#     for transaction in transactions:
#         customer_id, _, amount = transaction.values()
#
#         if customer_id not in customer_purchases:
#             customer_purchases[customer_id] = amount
#         else:
#             customer_purchases[customer_id] += amount
#
#     for customer, total in customer_purchases.items():
#         if total > 100:
#             vip_customer[customer] = total
#
#     return vip_customer
#
# print(purchasing([
#     {"customer_id": "C1", "product": "Laptop", "amount": 80},
#     {"customer_id": "C2", "product": "Mouse", "amount": 20},
#     {"customer_id": "C1", "product": "Keyboard", "amount": 40},
#     {"customer_id": "C2", "product": "Monitor", "amount": 100},
#     {"customer_id": "C3", "product": "Mouse", "amount": 15},
#     {"customer_id": "C1", "product": "Mouse", "amount": 30},
#     {"customer_id": "C2", "product": "Keyboard", "amount": 10}
# ]))


# def sensor_readings(readings):
#
#     sensors = {}
#     hot_sensors = {}
#
#     for reading in readings:
#
#         sensor_id = reading["sensor_id"]
#         temperature = reading["temperature"]
#
#         if sensor_id not in sensors:
#             sensors[sensor_id] = {"total_temp": temperature, "count": 1}
#
#         else:
#             sensors[sensor_id]["total_temp"] += temperature
#             sensors[sensor_id]["count"] += 1
#
#     for sensor, sensor_list in sensors.items():
#         average_temp = sensor_list["total_temp"] / sensor_list["count"]
#         if average_temp > 25:
#             hot_sensors[sensor] = average_temp
#
#     return hot_sensors
#
# print(sensor_readings([
#     {"sensor_id": "S1", "temperature": 20},
#     {"sensor_id": "S2", "temperature": 30},
#     {"sensor_id": "S1", "temperature": 30},
#     {"sensor_id": "S2", "temperature": 40},
#     {"sensor_id": "S3", "temperature": 15},
#     {"sensor_id": "S1", "temperature": 40},
#     {"sensor_id": "S3", "temperature": 20}
# ]))


# def products(purchases):
#
#     records = {}
#     most_frequent = {}
#
#     for purchase in purchases:
#         if purchase["product"] not in records:
#             records[purchase["product"]] = 1
#
#         else:
#             records[purchase["product"]] += 1
#
#     for item in records.items():
#         if item[1] == max(records.values()):
#             most_frequent[item[0]] = item[1]
#
#     return most_frequent
#
# print(products([
#     {"customer_id": "C1", "product": "Laptop"},
#     {"customer_id": "C2", "product": "Mouse"},
#     {"customer_id": "C3", "product": "Laptop"},
#     {"customer_id": "C1", "product": "Keyboard"},
#     {"customer_id": "C2", "product": "Mouse"},
#     {"customer_id": "C4", "product": "Laptop"},
#     {"customer_id": "C3", "product": "Keyboard"},
#     {"customer_id": "C5", "product": "Mouse"}
# ]))