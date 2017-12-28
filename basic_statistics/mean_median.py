# improve calculation performance
from __future__ import division

# input data
num_friends = [100, 40, 30, 30, 30, 30, 30, 30, 30, 30, 54, 54, 54, 54, 54, 54, 54, 54, 25, 3, 100, 100, 100, 3, 3]


# define mean function
def mean(x):
    return sum(x) / len(x)


# get mean of friends
mean_of_friends = mean(num_friends)
print("mean of friends: ", mean_of_friends)


# define median function
def median(x):
    n = len(x)
    sorted_v = sorted(x)

    # if divided by // then result is integer or using / then result is float
    midpoint = n // 2

    if n % 2 == 1:
        # if length is odd number
        return sorted_v[midpoint]
    else:
        # if length is even number
        lo = midpoint - 1
        hi = midpoint + 1
        return (sorted_v[lo] + sorted_v[hi]) / 2


median_of_friends = median(num_friends)
print("median of friends: ", median_of_friends)