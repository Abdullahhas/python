# 1 - Positional Arguments
# Ye arguments position (order) ke hisaab se assign hote hain.
def greet(name, age):
    print(name, age)

greet("Abdullah", 21)


# 2. Keyword Arguments
# Yahan tum parameter ka naam likhte ho.
# Order doesnot matters
def greet(name, age):
    print(name, age)

greet(age=21, name="Abdullah")

#3. Default Arguments
def greet(name, city="Lahore"):
    print(name, city)
greet("Abdullah")

# Documentation Example

def parrot(
    voltage,    # positional argument
    state='a stiff',  # default
    action='voom',    # //
    type='Norwegian Blue'  # //
):
    pass

# invalid calls
parrot() # require positonal argu
# parrot(voltage=5.0, "dead") # positional argu always come first


parrot(110, voltage=220)  # Same parameter ko 2 values mil gayi.

# Note
# Positional arguments first, keyword arguments after.



#  *args
# Suppose tum nahi jante kitne arguments aayenge.

def add(*numbers):
    print(numbers)

add(1,2,3,4)
# numbers tuple ban gaya.


# **kwargs

# Suppose tum nahi jante kitne keyword arguments aayenge.

def student(**info):
    print(info)

student(
    name="Abdullah",
    age=21
)

# kwargs dictionary ban gaya



# Documentation Example
def cheeseshop(
    kind,
    *arguments,
    **keywords
):
    pass

cheeseshop(
    "Limburger",
    "It's very runny.",
    "It's delicious.",
    shopkeeper="Michael",
    client="John"
)


# Default argument → belongs to the function definition.
# Keyword argument → belongs to the function call.


# A default argument is a parameter that already has a value in the function definition.
def greet(name, city="Lahore"):
    print(name, city)



# A keyword argument is when you pass a value using the parameter name while calling the function.
greet(name="Abdullah", city="Kasur")



# Positional-Only Parameters (/)
def pos_only_arg(arg, /):
    print(arg)

# Everything before / must be passed by position only.

pos_only_arg(10)  # correct

pos_only_arg(arg=10)  # wrong



# Keyword-Only Parameters (*)
def kwd_only_arg(*, arg):
    print(arg)

# Everything after * must be passed as a keyword.

kwd_only_arg(10) # wrong


kwd_only_arg(arg=10) # correct

# Combined Example

def combined_example(
    pos_only,
    /,
    standard,
    *,
    kwd_only
):
    print(pos_only, standard, kwd_only)


# pos_only

# Before /

# Positional only

# ....

# standard

# Between / and *

# Positional OR Keyword

# ....
# kwd_only

# After *

# Keyword only
