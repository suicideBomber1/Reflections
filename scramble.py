import collections


def scramble(s1, s2):
    count = 0
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    for i in c2.keys():
        for j in c1.keys():
            if j == i and c1[j] >= c2[i]:
                count += c2[i]
    if count == len(s2):
        return True
    else:
        return False


result = scramble('cedewaraaossoqqyt', 'codewars')
print(result)
