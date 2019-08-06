def binary_search(input_array, value):
    first = 0
    last = len(input_array) - 1
    while first <= last:
        m = int((first + last) / 2)
        if value == input_array[m]:
            return m
        elif value < input_array[m]:
            last = m - 1
        else:
            first = m + 1
    return -1

test_list = [1,5,10,13,17,19,29]
test_val1 = 25
test_val2 = 17
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))