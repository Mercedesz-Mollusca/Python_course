import random

#1st option
friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred"]
random_name = random.choice(friends)
print(random_name)

#2nd option
random_index = random.randint(0, 5)
print(friends[random_index])
