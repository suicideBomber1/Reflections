def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")
    numbers.remove(min(numbers))
    return numbers


result = remove_smallest([1, 2, 3, 4, 5])
print(result)
