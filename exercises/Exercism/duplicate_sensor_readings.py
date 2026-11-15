

# def find_duplicates(sensor_readings):
#     seen = set()
#     duplicates = set()
#     for reading in sensor_readings:
#         if reading not in seen:
#             seen.add(reading)
#         else:
#             duplicates.add(reading)
#
#     return duplicates
#
#
# print(find_duplicates([
#     "SENSOR_01",
#     "SENSOR_02",
#     "SENSOR_01",
#     "SENSOR_03",
#     "SENSOR_02",
#     "SENSOR_04",
#     "SENSOR_01"
# ]))

# def count_errors(error_codes):
#
#     code_frequency = {}
#     for code in error_codes:
#         if code not in code_frequency:
#             code_frequency[code] = 1
#         else:
#             code_frequency[code] += 1
#
#     return code_frequency
#
# print(count_errors(["E01", "E02", "E01", "E03", "E02", "E01"]))

# def calculate_average(readings):
#     total = 0
#     for x in readings:
#         total += x
#     return total / len(readings)
#
#
# print(calculate_average([20, 25, 30, 35, 40]))

# def filter_invalid_readings(lower, upper, readings):
#     invalid_readings = []
#
#     for x in readings:
#         if not lower < x < upper:
#             invalid_readings.append(x)
#
#     valid_readings = [x for x in readings if lower < x < upper]
#
#     return invalid_readings, valid_readings
#
# print(filter_invalid_readings(10, 40, [5, 12, 25, 41, 38, 8, 45]))

# def get_hot_sensor(sensor_data):
#     for x in sensor_data:
#         print(x.values([2]))
#
#
#
#
# print(get_hot_sensor([
#         {"id": 101, "location": "Factory A", "temperature": 25},
#         {"id": 102, "location": "Factory B", "temperature": 42},
#         {"id": 103, "location": "Factory C", "temperature": 18}
#     ]))
#
#
# first, last, *middle = [1, 2, 3, 4, 5]
# print(first, last, middle)

# understand and fix
# def generate_error_report(events, ignored_codes=[]):
#
#     report = {}
#
#     for event in events:
#         try:
#             code = event["error_code"]
#             message = event["message"]
#
#             if code in ignored_codes:
#                 continue
#
#             if code not in report:
#                 report[code] = []
#
#             report[code].append(message)
#
#         except:
#             pass
#
#     for code in report:
#         report[code] = list(set(report[code]))
#
#     return report
#
#
# def print_report(report):
#
#     for code in report:
#         print("Error Code: " + code)
#         print("Messages: " + str(report[code]))


# def anomalous_readings(reading):
#
#     sensor_dict = {}
#     for sensor in reading:
#         sensor_id = sensor["sensor_id"]
#         temperature = sensor["temperature"]
#         if sensor_id not in sensor_dict:
#             sensor_dict[sensor_id] =  {
#                 "total" : temperature,
#                 "count" : 1
#             }
#         else:
#             sensor_dict[sensor_id]["total"] += temperature
#             sensor_dict[sensor_id]["count"] += 1
#
#     anomaly = []
#     for sensor in sensor_dict:
#         sensor_dict[sensor]["total"] = sensor_dict[sensor]["total"] / sensor_dict[sensor]["count"]
#         if sensor_dict[sensor]["total"] > 40:
#             anomaly.append(sensor)
#
#     return anomaly
#
# print(anomalous_readings([
#     {"sensor_id": "A", "temperature": 21},
#     {"sensor_id": "B", "temperature": 24},
#     {"sensor_id": "A", "temperature": 22},
#     {"sensor_id": "C", "temperature": 65},
#     {"sensor_id": "B", "temperature": 25},
#     {"sensor_id": "A", "temperature": 23},
#     {"sensor_id": "C", "temperature": 67},
#     {"sensor_id": "B", "temperature": 24},
# ]))


# def getRemovableIndices(str1, str2):
#     # Write your code here
#     removable_char = []
#     for index, char in enumerate(str1):
#         string_slice = str1[:index] + str1[index+1:]
#         print(string_slice)
#         if string_slice == str2:
#             removable_char.append(index)
#
#     return removable_char
#
# print(getRemovableIndices("aabbb", "aabb"))



class Event:
    def __init__(self, event_id, name, capacity):
        self.event_id = event_id
        self.name = name
        self.capacity = capacity
        self.bookings = []


class Booking:
    def __init__(self, customer_id, event_id, tickets):
        self.customer_id = customer_id
        self.event_id = event_id
        self.tickets = tickets


class BookingSystem:
    def __init__(self):
        self.events = []
        self.bookings = []

    def add_event(self, event):
        self.events.append(event)

    def add_booking(self, booking):
        self.bookings.append(booking)

    def get_event(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event

        return None

    #

    def book_tickets(self, customer_id, event_id, tickets):
        pass

