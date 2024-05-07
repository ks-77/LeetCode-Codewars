def new_format(string):
    return '{:,.0f}'.format(float(string)).replace(',', '.')


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")


def deep_lake(int_array):
    if not int_array:
        return 0

    current_depth = 0
    max_depth = 0
    hill_height = 0

    for height in int_array:
        if hill_height == 0 or height > hill_height:
            hill_height = height
            current_depth = 0
        else:
            current_depth = hill_height - height
            if current_depth > max_depth:
                max_depth = current_depth

    return max_depth


# intarray = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]
# print(deep_lake(intarray))
# a. task analysis, outcome analysis, start of writing first version
# b. +- 1.5 h
