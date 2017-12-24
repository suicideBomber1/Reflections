adjacents = {
    '0': ['0', '8'],
    '1': ['1', '2', '4'],
    '2': ['1', '2', '3', '5'],
    '3': ['2', '3', '6'],
    '4': ['1', '4', '5', '7'],
    '5': ['2', '4', '5', '6', '8'],
    '6': ['3', '5', '6', '9'],
    '7': ['4', '7', '8'],
    '8': ['5', '7', '8', '9', '0'],
    '9': ['6', '8', '9']
}


def get_pins(obs):
    if len(obs) == 1:
        return adjacents[obs]
    else:
        first = obs[:1]
        rest = obs[1:]
        l = []
        sub_l = get_pins(rest)
        for i in adjacents[first]:
            for j in sub_l:
                l.append(i + j)

    return l


result = get_pins('3')
print(result)
