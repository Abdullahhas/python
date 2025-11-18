print("I am reading the file")
username = "Abdullah"
print(username)



# f = open('hello.py')
# >>> f.readline()
# 'print("I am reading the file")\n'
# >>>
# >>> f.readline()
# 'username = "Abdullah"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>>


# f = open('hello.py') 
# >>> f.__next__() 
# 'print("I am reading the file")\n'
# >>> f.__next__()
# 'username = "Abdullah"\n'
# >>> f.__next__()
# 'print(username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>





# for line in open('hello.py'):
# ...     print(line)
# ... 
# print("I am reading the file")

# username = "Abdullah"

# print(username)







# f = open('hello.py')

# >>> f.readline()

# 'print("I am reading the file")\n'

# >>>

# >>> f.readline()

# 'username = "Abdullah"\n'

# >>> f.readline()

# 'print(username)'

# >>> f.readline()

# ''

# >>>





# f = open('hello.py')

# >>> f.__next__()

# 'print("I am reading the file")\n'

# >>> f.__next__()

# 'username = "Abdullah"\n'

# >>> f.__next__()

# 'print(username)'

# >>> f.__next__()

# Traceback (most recent call last):

#   File "<stdin>", line 1, in <module>

# StopIteration

# >>>
# >>>


#  mylist = [1,2,3,4]
# >>> I = iter(mylist)
# >>> I
# <list_iterator object at 0x0000025ACB461810>
# >>> I.__next__()
# 1
# >>>
# >>> 
# >>> I
# <list_iterator object at 0x0000025ACB461810>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>