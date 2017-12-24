def increment_string(s):
    n = []
    rs = []
    for i in reversed(s):
        if i.isdigit():
            n.append(i)
        else:
            break
    num = ''.join(n)
    for i in reversed(s):
        rs.append(i)

    rs = ''.join(rs)
    if num in rs:
        rest = rs.replace(num, '')
    l = rest[::-1]
    # print(l)
    # 'rest' is a string containing the rest of the required num. part
    # 'num' is string containing the required numerical part
    if n == []:
        n.append(1)
        n = str(1)

    else:
        # n = str(int(''.join(n)) + 1).zfill()
        l1 = len(n)
        n = n[::-1]
        m = str(int(''.join(n)) + 1)
        l2 = len(str(m))
        n = m.zfill(l1)
        # print(n)

    return l + n


# result = increment_string(.F84183_v. < t~)1372673 < Ph"(nQT20086183C+!"G1x; > 99666', % h`jqB9858 + 2159495368475700000000028816620)
# print(result)
