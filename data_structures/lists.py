# Lists are mutable

list.append() # add item at the end

# Similar to a[len(a):] = [x].


# example
a = [10, 20, 30, 40, 50, 60]
print(len(a))

a[len(a):] = [70]


# What does a[6:] mean ?

# Normally, slicing is:

# a[start:end]

# If end is omitted:

# a[start:]

# means "Take everything from start to the end."

# Now here:

# a[6:]

# The valid indices are:

# Index:   0   1   2   3   4   5
# Value:  10  20  30  40  50  60


# Index 6 is one position after the last element.

# so a[6:] returns []

# because there are no elements from index 6 onward.


# Then why does this work?

# Because this is not reading a slice.

# This is slice assignment.

a[6:] = [70]

# means:"Replace the empty slice starting at index 6 with [70]."
# So Python inserts 70 there.

# same as a.append(70)



2- list.extend(iterable)
# Adds all the element from another iterable (list , tuple , string etc) to the end of the list


a = [1, 2, 3]
b = [4, 5]

a.extend(b)

print(a)

output = [1,2,3,4,5]

# python internally behave like 
a[len(a) : ] = [b]




# Difference between append and extend

a = [1,2]

a.append([3,4])

print(a)

output = [1,2,[3,4]]

a.extend([3,4])
output = [1,2,3,4]

# extend() adds each element separately.


3- list.insert(index, value)

# Adds an element before the given index.

a = [10,20,30]

a.insert(1,15)
 
print(a)   [10,15,20,30]


4- list.remove(value)

# Removes the first occurrence of a value.

a = [1,2,3,2]

a.remove(2)

print(a)  [1,3,2]



5- list.pop(index=-1)
# Removes by index and returns the removed element.

a = [10,20,30]

x = a.pop()  # default index is -1

print(x) #30
print(a) [10,20]


# remove() use value
# pop() use index


6- list.clear()
# removes everything

a = [1,2,3]

a.clear() # == to del a[:]

print(a)  #[]

7- list.index(value) # returns the index

8- list.count(value) #Counts how many times a value appears

9- list.sort() # sorts the orignal list

a = [5,2,1,4]

a.sort()

print(a)  # [1,2,4,5] asscending


# descending
a.sort(reverse = True)

10 - list.reverse() #just reverse the order

11- list.copy()
# creates a shallow 





# List as stack

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
stack

stack.pop()

stack

stack.pop()

stack.pop()

stack


# Lists as queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

queue                           # Remaining queue in order of arrival``




# List comprehensions

# A list comprehension is simply a shorter and cleaner way to create a list.

# Use them when you want to build a new list from an iterable in a concise and readable way.

# syntax
# [expression for variable in iterable]
numbers = [x for x in range(5)]  # Take x for every x in range 5
squares = [x**2 for x in range(10)] # Take x square for every x in range 10
even = [x for x in range(10) if x % 2 == 0]
pairs = [(x,y) for x in [1,2] for y in [3,4]]

# Instead of writing
numbers = []
for x in range(5):
    numbers.append(x)

# we can write
numbers = [x for x in range(5)]  # for every x in range(5) put x in the new list

# map(lambda)

list(map(lambda x : x**2 , range(10))) # same result but it is difficult to readable

# filtering
vec = [-4,-2,0,2,4]
[x for x in vec if x>=0]

# Applying functions
[abs(x) for x in vec]

# calling methods
freshfruit = [
    " banana",
    " apple ",
    " mango "
]

[x.strip() for x in freshfruit]


# Tuples
[(x,x**2) for x in range(6)]

[
(0,0),
(1,1),
(2,4),
(3,9),
(4,16),
(5,25)
]


# Filtering a nested list

vec = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

# normal 
result=[]

for row in vec:

    for num in row:

        result.append(num)

# list comprehension
[num for row in vec for num in row]



# read it like that
# For every row
# For every number in that row
# Put number into new list

