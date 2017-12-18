# input data
num_friends = [100, 40, 30, 30, 30, 30, 30, 30, 30, 30, 54, 54, 54, 54, 54, 54, 54, 54, 25, 3, 100, 100, 100, 3, 3]

# generate list that input data are sorted by Ascending
sorted_value = sorted(num_friends)
print("sorted value: ", sorted_value)

# get second smallest value
# index number is begin 0, so second smallest value index is 1
second_smallest_value = sorted_value[1]
print("second_smallest_value: ", second_smallest_value)

# get second largest value
# if the python index number has a '-' appended, the index number start backwards.
# '-1' is mean last index number in list
second_largest_value = sorted_value[-2]
print("second_largest_value: ", second_largest_value)
