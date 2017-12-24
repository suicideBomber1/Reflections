import decimal


def doubles(maxk, maxn):
    sum = 0
    for j in range(1, maxn + 1):
        for i in range(1, maxk + 1):
            sum += 1 / (i * ((j + 1)**(2 * i)))

    return round(sum, 6)


result = doubles(10, 10000)
print(result)
