def factor(number):
    count = 0
    factors = [1]
    for i in range(2, int(number / 2)):
        if number % i == 0:
            count += 1
            factors.append(i)
    if count == 0:
        return [1, number]
    factors.append(number)
    return factors;
