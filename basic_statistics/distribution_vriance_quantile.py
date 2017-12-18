import math

# input data
num_friends = [100, 15, 10, 10, 9, 4, 3, 3, 2, 1]


# define data rage function
def data_rage(x):
    return max(x) - min(x)


print("range of between min and max : ", data_rage(num_friends))


# define quantile function
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


# define interquantile function
def interquantile(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


print("difference between 75% and 25% of input data: ", interquantile(num_friends))

#############################
# variance calculation part #
#############################


def mean(x):
    return sum(x) / len(x)


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


# difference of between element and mean value
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)


variance_value = variance(num_friends)
print("variance : ", variance_value)


def standard_deviation(x):
    return math.sqrt(variance(x))


standard_deviation_value = standard_deviation(num_friends)
print("standard deviation value : ", standard_deviation(num_friends))