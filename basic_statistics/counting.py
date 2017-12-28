import collections

# make list of number of friends
num_friends = [100, 40, 30, 54, 25, 3, 100, 100, 100, 3, 3]

# count number of people who have same number of friends
friend_counts = collections.Counter(num_friends)

# shown counting result
print('friends: ', friend_counts)

