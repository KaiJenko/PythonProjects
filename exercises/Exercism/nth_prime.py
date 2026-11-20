
def prime(number):

    prime_numbers = []
    count = 2

    while len(prime_numbers) < number:

        prime = True

        for x in range(2, count):

            if count % x == 0:
                prime = False
                break

        if prime:
            prime_numbers.append(count)

        count += 1

    print(prime_numbers)
    return prime_numbers[number - 1]




print(prime(10001))