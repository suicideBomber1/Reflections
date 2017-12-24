def triple_double(num1, num2):
    m = 0
    n = 0
    for x in range(10):
        if str(x) * 3 in str(num1):
            m = 1
        if str(x) * 2 in str(num2):
            n = 1
    return m and n

    # l1 = [int(d) for d in str(num1)]
    # l2 = [int(d) for d in str(num2)]
    # m = 0
    # n = 0
    # for i in range(len(l1)):
    #     try:
    #         if l1[i] == l1[i + 1] and l1[i + 1] == l1[i + 2]:
    #             m = 1
    #             break
    #     except IndexError:
    #         pass

    # for j in range(len(l2)):
    #     try:
    #         if l2[j] == l2[j + 1]:
    #             n = 1
    #             break

    #     except IndexError:
    #         pass

    # return m and n


result = triple_double(1222345, 12345)
print(result)
