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


# Methods to write strings

# 1- Single Quotes
name = 'Abdullah'

# 2-Double Quotes
name = "Abdullah"

# 3 - Triple Quotes  Use for multi line text
text = """Hello
How are you?
I am fine."""

# What is unicode

# Python duniya ki lagbhag har language support karta hai.

# These are all strings
english = "Hello"
urdu = "السلام علیکم"
chinese = "你好"

# Adjacent Strings Automatically Join 

text = ("Hello "
        "World")

# python will take it as
text = "Hello World"


# String Constructor str()
# convert any object into string

age = 21
a = str(age)
print(type(a))


# efficient way to join strings
words = ["Hello", "World"]

result = " ".join(words)

print(result)


# bytes

b = b'Hello'
print(type(b))


# bytes to string
b = b'Hello'

text = str(b, encoding='utf-8')

print(text)

# or

text = b.decode('utf-8')    


# f strings

name = "Abdullah"
age = 21

print(f"My name is {name} and I am {age}")


# It is possible to nest f-strings:
name = 'world'
print(f'Repeated:{f' hello{name}' * 3}')




