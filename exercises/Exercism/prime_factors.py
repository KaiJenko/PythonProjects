
def factors(value):

    prime_factors = []
    x = 2
    while value > 1:
        if value % x == 0:
            value //= x
            prime_factors.append(x)
        else:
            x += 1
    return prime_factors

print(factors(60))

