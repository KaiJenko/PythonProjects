def sum_of_multiples(limit, multiples):
    energy_points = set()
    for x in multiples:
        if x == 0: continue
        for y in range(1,limit):
            if y % x == 0:
                energy_points.add(y)

    return sum(energy_points)