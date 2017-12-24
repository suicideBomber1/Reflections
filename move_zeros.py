def move_zeros(array):
    arr = array[:]
    n = 0
    for index, item in enumerate(arr):
		try:
            if item == 0 and item != False:
                value = int(array.pop(index - n))
                array.append(value)
                n += 1
        except Exception:
            continue
    return array


# result = move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"])
# print(result)
