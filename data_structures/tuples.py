# tuples are immutable

# A tuple is a collection of values just like list

my_tuple = (10,20,30)
# or
my_tuple = 10 ,20 ,30

t = 12345 , 543221 , "hello"
print(t)    #  python automatically creates (12345, 543221, 'hello')

# Notice:
# The comma creates the tuple.
# The parentheses are optional in many cases.


#nested tuples
u = t, (1,2,3,4,5)
print(u)

# important point
v = ([1,2,3],[3,2,1])

# v[0] = 100  # error bcz tuple are immutable

v[0].append(4)  # allow bcz list inside the tuple changed
print(v)

# Why use tuples

# Lists are usually Homogenous means same type of data
# e.g marks = [10,20,25]  all integers

# Tuples are usually heterogenous means different types
# e.g student = ("Abdullah",21,3.7)


# One Element Tuple
string = ("hello")
print(type(string))    # str -> bcz because parentheses alone don't create a tuple.

t = ("hello" ,)  # Notice the comma 
print(type(t))

# remember the comma creates a tuple Not the paranthesis


# tuple packing
t = 12345,54321,"hello"

#python packs this into one tuple this is called tuple packing


# tuple unpacking
x , y ,z = t
t = (10 , 20 , 30)

print(x)  # -> 10  #This is call sequence unpacking


# only count and index methods
# less memory then lists

# a tuple can contain mutable objects