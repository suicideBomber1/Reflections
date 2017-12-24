def sum_dig_pow(a, b):
	num = []
    for i in range(a, b + 1, 1):
        l = [int(j) for j in str(i)]
        count = 0
        for j in range(len(l)):
            count += l[j]**(j + 1)

        if count == i:
            num.append(1)
    return num


# result = sum_dig_pow(1, 10)
# print(result)