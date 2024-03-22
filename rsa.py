def factor(num):
    count = 0
    factors = [1]
    for i in range(2, int(num / 2)):
        if num % i == 0:
            count += 1
            factors.append(i)
    if count == 0:
        return [1, num]
    factors.append(num)
    return factors;
