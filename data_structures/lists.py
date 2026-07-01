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
# creates a shallow copy


