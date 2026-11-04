

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

def filter_invalid_readings(lower, upper, readings):
    invalid_readings = []

    for x in readings:
        if not lower < x < upper:
            invalid_readings.append(x)

    valid_readings = [x for x in readings if lower < x < upper]

    return invalid_readings, valid_readings

print(filter_invalid_readings(10, 40, [5, 12, 25, 41, 38, 8, 45]))

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
def generate_error_report(events, ignored_codes=[]):

    report = {}

    for event in events:
        try:
            code = event["error_code"]
            message = event["message"]

            if code in ignored_codes:
                continue

            if code not in report:
                report[code] = []

            report[code].append(message)

        except:
            pass

    for code in report:
        report[code] = list(set(report[code]))

    return report


def print_report(report):

    for code in report:
        print("Error Code: " + code)
        print("Messages: " + str(report[code]))