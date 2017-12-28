import collections
import matplotlib.pyplot as plt

# make list of number of friends
num_friends = [100, 40, 30, 30, 30, 30, 30, 30, 30, 30, 54, 54, 54, 54, 54, 54, 54, 54, 25, 3, 100, 100, 100, 3, 3]

# count number of people who have same number of friends
friend_counts = collections.Counter(num_friends)

# visualization as histogram using by matplotlib module

# number of consecutive numbers before stop value
# follow stop value is 101, then 0...100
xs = range(101)

# generate list object ( list comprehension )
ys = [friend_counts[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.xlabel(" # of friends")
plt.ylabel(" # of people")
plt.show()
