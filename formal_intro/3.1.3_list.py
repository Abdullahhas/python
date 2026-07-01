squares = [1, 4, 9, 16, 25]

# Lists also support operations like concatenation:
print(squares + [36, 49, 64, 81, 100])

# Lists are mutable
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
print(cubes)

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)

#Simple assignment in Python never copies data. When you assign a list to a variable, the variable refers to the existing list. Any changes you make to the list through one variable will be seen through all other variables that refer to it.:

# 1- Assignment doesnot create new copy refer to existing
rgb = ["Red", "Green", "Blue"]
rgba = rgb
print(id(rgb) == id(rgba))  # they reference the same object

rgba.append("Alph")
print(rgb)


# 2- Copy create copy of the list and create new list

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
correct_rgba = rgba[:]

correct_rgba[-1] = "Alpha"
print(correct_rgba)

print(rgba)


# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']
print(letters)

# now remove them
letters[2:5] = []
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)

# len also applies to list
letters = ['a', 'b', 'c', 'd']
len(letters)

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])

print(x[0][1])