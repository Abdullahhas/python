word = 'python'
print(word[-1])  # last character
print(word[-2])  # 2nd last character

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

print(word[:2])    # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end)

print(word[:2] + word[2:])  # py + thon
print(word[:4] + word[4:])  # pyth + on


#Attempting to use an index that is too large will result in an error
# print(word[42])


# However, out of range slice indexes are handled gracefully when used for slicing:
print(word[4:42])


# word[0] = 'J'  wrong bcz strings are immutable

#The built-in function len() returns the length of a string:
print(len(word))

