import collections


def longest(s1, s2):
    s = s1 + s2
    l = []
    c = collections.Counter(s)
    for i in c.keys():
        l.append(i)
    l.sort()
    return ''.join(l)

    # I dont know what I am doing just testing out some stuff on git


a = "xyaabbbccccdefww"
b1 = "xxxxyyyyabklmopq"
longest(a, b1)
