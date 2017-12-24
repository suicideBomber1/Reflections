import numpy as np


def openorsenior(data):
    tags = []
    data = np.array(data)
    m, n = data.shape
    for i in range(m):
        if (data[i][0] > 55) and (data[i][1] > 7):
            tags.append("Senior")
        else:
            tags.append("Open")
    return tags


data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
result = openorsenior(data)
print(result)
