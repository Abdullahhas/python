# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))



# Code that modifies a collection while iterating over that same collection can be tricky to get right. Instead, it is usually more straight-forward to loop over a copy of the collection or to create a new collection:

# 1 -  Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# 2 -  Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status   # key user rakh do or us ki value status rakh do



# range()

# If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

for i in range(5):
    print(i)


print(list(range(5, 10)))
print(list(range(-10, -100, -30)))


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


range(10) == range(0, 10)


# range does not create list
# does not store all numbers in the memory

# List vs range
# list memory use karta he

#"range() behaves like a list but isn’t a list"


# Matlab:

# Tum us par loop chala sakte ho (list jaisa behavior)
# Lekin internally ye list nahi ha -> ik ik  number genrate karta he


#"On-demand generation" concept

#range() numbers tab banata hai jab zarurat ho:
